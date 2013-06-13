import sublime, sublime_plugin, os, shutil, re

PLUGIN_PATH = os.path.dirname(os.path.abspath(__file__))

class EeAddOnBuilderCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.templates_path = os.path.join(PLUGIN_PATH, "templates")
        self.settings = sublime.load_settings('EeAddOnBuilder.sublime-settings')
        self.template_names = []
        self.choose_template()

    def choose_template(self):
        if self.settings.get('package_custom_template_path') != '' and os.path.isdir(self.settings.get('package_custom_template_path')):
            self.templates_path = self.settings.get('package_custom_template_path');
        files = self.get_templates()
        for file_name in files:
            if os.path.isdir(os.path.join(self.templates_path, file_name)):
                self.template_names.append(file_name)
        self.window.show_quick_panel(self.template_names, self.on_template_chosen)

    def get_templates(self):
        files = os.listdir(self.templates_path)
        files = [(f.lower(), f) for f in files]
        return [f[1] for f in sorted(files)]

    def on_template_chosen(self, index):
        if index == -1:
            return
        self.chosen_template_name = self.template_names[index]
        self.chosen_template_path = os.path.join(self.templates_path, self.chosen_template_name)
        self.get_package_name()

    def get_package_name(self):
        self.window.show_input_panel("Package Name:", '', self.on_package_name, None, None)

    def on_package_name(self, name):
        self.package_full_name = name
        self.package_short_name = self.generatate_short_name(self.package_full_name)
        self.get_package_path()

    def generatate_short_name(self, value):
        return re.sub('[^0-9a-zA-Z_]+', '', value.replace(' ', '_')).lower()

    def get_package_path(self):
        if self.window.folders():
            default_package_path = os.path.expanduser(self.window.folders()[0] + self.settings.get('package_default_path') + '/' + self.package_short_name)
        elif sublime.platform() == "windows":
            default_package_path = os.path.expanduser("~\\My Documents\\" + self.package_short_name)
        else:
            default_package_path = os.path.expanduser("~/Documents/" + self.package_short_name)
        self.window.show_input_panel("Package Location:", default_package_path, self.on_package_path, None, None)

    def on_package_path(self, path):
        self.package_path = path
        if os.path.exists(self.package_path) is False:
            self.build_tokens()
        else:
            dialog = sublime.ok_cancel_dialog("Something already exists in this package path. If you're simply adding to an existing Add-On, we'll merge in to that.\n\nAny duplicate files encountered will just be renamed with a .bak extension.\n\nWould you like to continue?", 'Yes, merge it in!')
            if dialog:
                self.build_tokens()
            else:
                self.get_package_path()

    def build_tokens(self):
        self.token_index = 0
        self.tokens = ['package_author', 'package_author_url', 'package_version', 'package_doc_url', 'package_description']
        self.token_name = ['Author', 'Author URL', 'Version Number', 'Documentation URL', 'Description']
        self.token_values = {'package_full_name': self.package_full_name, 'package_short_name': self.package_short_name, 'package_path': self.package_path, 'package_class_name': self.package_short_name.capitalize()}
        self.boolean_tokens = ['package_has_control_panel_page', 'package_has_control_panel_settings']
        self.ext_list_tokens = ['package_ext_hook']
        self.auto_build_url_title = {'package_section': 'package_section_short_name'}
        if (self.chosen_template_name.lower() == 'module'):
            self.tokens.append('package_has_control_panel_page')
            self.token_name.append('Should this module have a Control Panel page?')
        elif (self.chosen_template_name.lower() == 'extension'):
            self.tokens.append('package_has_control_panel_settings')
            self.token_name.append('Should this extension have a Control Panel Settings page?')
            self.tokens.append('package_ext_hook')
            self.token_name.append('Initial Extension Hook')
            self.tokens.append('package_ext_hook_method')
            self.token_name.append('Method name that first extension hook maps to')
        elif (self.chosen_template_name.lower() == 'accessory'):
            self.tokens.append('package_section')
            self.token_name.append('Name of first Accessory Section (tab name)')
        self.get_next_token_value()

    def get_next_token_value(self):
        if self.token_index < len(self.tokens):
            token_name = self.token_name[self.token_index]
            if self.tokens[self.token_index] in self.boolean_tokens:
                dialog = sublime.ok_cancel_dialog(self.token_name[self.token_index], 'Yes')
                self.on_token_value(dialog)
            elif self.tokens[self.token_index] in self.ext_list_tokens:
                extension_hooks_display = ['-- ' + self.token_name[self.token_index] + ' --'] + self.settings.get('extension_hooks')
                self.window.show_quick_panel(extension_hooks_display, self.on_token_value)
            else:
                self.window.show_input_panel(self.token_name[self.token_index], self.settings.get(self.tokens[self.token_index], ""), self.on_token_value, None, None)
        else:
            self.create_package()

    def on_token_value(self, token_value):
        if self.tokens[self.token_index] in self.boolean_tokens:
            if token_value is True:
                self.token_values[self.tokens[self.token_index]] = 'y'
            else:
                self.token_values[self.tokens[self.token_index]] = 'n'
        elif self.tokens[self.token_index] in self.ext_list_tokens:
            if token_value == -1:
                return
            ext_hooks = self.settings.get('extension_hooks')
            self.token_values[self.tokens[self.token_index]] = ext_hooks[token_value]
        elif self.tokens[self.token_index] in self.auto_build_url_title:
            self.token_values[self.tokens[self.token_index]] = token_value
            self.token_values[self.auto_build_url_title[self.tokens[self.token_index]]] = self.generatate_short_name(token_value)
        else:
            self.token_values[self.tokens[self.token_index]] = token_value
        self.token_index += 1
        self.get_next_token_value()

    def create_package(self):
        if os.path.exists(self.package_path) is False:
            shutil.copytree(self.chosen_template_path, self.package_path)
        else:
            for src_dir, dirs, files in os.walk(self.chosen_template_path):
                dst_dir = src_dir.replace(self.chosen_template_path, self.package_path)
                if not os.path.exists(dst_dir):
                    os.mkdir(dst_dir)
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        os.rename(dst_file, dst_file + '.bak')
                    shutil.copy2(src_file, dst_dir)

        self.replace_tokens()

    def replace_tokens(self):
        for root, subFolders, files in os.walk(self.package_path):
            for filename in files:
                file_ref = open(os.path.join(root, filename), "rU")
                template = file_ref.read()
                file_ref.close()

                for token, value in self.token_values.iteritems():
                    r = re.compile(r"\${" + token + "}")
                    template = r.sub(value, template)

                file_ref = open(os.path.join(root, filename), "w")
                file_ref.write(template)
                file_ref.close()

                for token, value in self.token_values.iteritems():
                    tokened_file = filename.replace('__' + token + '__', value);
                    if (tokened_file != filename):
                        if os.path.exists(os.path.join(root, tokened_file)):
                            os.rename(os.path.join(root, tokened_file), os.path.join(root, tokened_file) + '.bak')
                        os.rename(os.path.join(root, filename), os.path.join(root, tokened_file))

        self.finish_up()

    def finish_up(self):
        sublime.message_dialog("Your " + self.chosen_template_name.lower() + ", " + self.package_full_name + ", has been successfully created!")
        self.window.run_command("open_dir", {"dir": self.package_path});
