import sublime, sublime_plugin, os, shutil, re

class EePackageGeneratorCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.plugin_path = os.path.join(sublime.packages_path(), "EePackageGenerator")
        self.templates_path = os.path.join(self.plugin_path, "templates")
        self.settings = sublime.load_settings('EePackageGenerator.sublime-settings')
        self.template_names = []
        self.choose_template()

    def choose_template(self):
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
        self.chosen_template_name = self.template_names[index]
        self.chosen_template_path = os.path.join(self.templates_path, self.chosen_template_name)
        self.get_package_name()

    def get_package_name(self):
        self.window.show_input_panel("Package Name:", '', self.on_package_name, None, None)

    def on_package_name(self, name):
        self.package_full_name = name
        self.package_short_name = self.package_full_name.lower().replace(' ', '_')
        self.get_package_path()

    def get_package_path(self):
        if self.window.folders():
            default_package_path = os.path.expanduser(self.window.folders()[0] + '/' + self.package_short_name)
        elif sublime.platform() == "windows":
            default_package_path = os.path.expanduser("~\\My Documents\\" + self.package_short_name)
        else:
            default_package_path = os.path.expanduser("~/Documents/" + self.package_short_name)
        self.window.show_input_panel("Package Location:", default_package_path, self.on_package_path, None, None)

    def on_package_path(self, path):
        self.package_path = path
        self.create_package()

    def create_package(self):
        if os.path.exists(self.package_path) is False:
            shutil.copytree(self.chosen_template_path, self.package_path)
        for root, subFolders, files in os.walk(self.package_path):
            for filename in files:
                if (filename.replace('__package_short_name__', self.package_short_name) != filename):
                    os.rename(os.path.join(root, filename), os.path.join(root, filename.replace('__package_short_name__', self.package_short_name)))
        self.build_tokens()

    def build_tokens(self):
        self.token_index = 0
        self.tokens = ['package_author', 'package_author_url', 'package_version', 'package_doc_url', 'package_description']
        self.token_name = ['Author', 'Author URL', 'Version Number', 'Documentation URL', 'Description']
        self.token_values = {'package_full_name': self.package_full_name, 'package_short_name': self.package_short_name, 'package_path': self.package_path, 'package_class_name': self.package_short_name.capitalize()}
        self.boolean_tokens = ['package_has_control_panel_page', 'package_has_control_panel_settings']
        self.ext_list_tokens = ['package_ext_hook']
        if (self.chosen_template_name.lower() == 'module'):
            self.tokens.append('package_has_control_panel_page')
            self.token_name.append('Has Control Panel Page?')
        elif (self.chosen_template_name.lower() == 'extension'):
            self.tokens.append('package_has_control_panel_settings')
            self.token_name.append('Has Control Panel Settings?')
            self.tokens.append('package_ext_hook')
            self.token_name.append('Initial Extension Hook')
            self.tokens.append('package_ext_hook_method')
            self.token_name.append('Method First Extension Hook Maps To')
        self.get_next_token_value()

    def get_next_token_value(self):
        if self.token_index < len(self.tokens):
            token_name = self.token_name[self.token_index]
            if self.tokens[self.token_index] in self.boolean_tokens:
                self.window.show_quick_panel([' -- ' + self.token_name[self.token_index] + ' --', 'No', 'Yes'], self.on_token_value)
            elif self.tokens[self.token_index] in self.ext_list_tokens:
                extension_hooks_display = [' -- ' + self.token_name[self.token_index] + ' --'] + self.settings.get('extension_hooks')
                self.window.show_quick_panel(extension_hooks_display, self.on_token_value)
            else:
                self.window.show_input_panel(self.token_name[self.token_index], self.settings.get(self.tokens[self.token_index], ""), self.on_token_value, None, None)
        else:
            self.replace_tokens()

    def on_token_value(self, token_value):
        if self.tokens[self.token_index] in self.boolean_tokens:
            if token_value == 'Yes':
                self.token_values[self.tokens[self.token_index]] = 'y'
            else:
                self.token_values[self.tokens[self.token_index]] = 'n'
        elif self.tokens[self.token_index] in self.ext_list_tokens:
            ext_hooks = self.settings.get('extension_hooks')
            self.token_values[self.tokens[self.token_index]] = ext_hooks[token_value]
        else:
            self.token_values[self.tokens[self.token_index]] = token_value
        self.token_index += 1
        self.get_next_token_value()

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
        self.clean_up()

    def clean_up(self):
        self.window.run_command("open_dir", {"dir":self.package_path});
