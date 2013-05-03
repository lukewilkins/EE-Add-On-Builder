import sublime, sublime_plugin, os, shutil, re

class EePackageGeneratorCommand(sublime_plugin.WindowCommand):

    extension_hooks = ['channel_entries_query_result', 'channel_entries_row', 'channel_entries_tagdata', 'channel_entries_tagdata_end', 'channel_module_calendar_start', 'channel_module_categories_start', 'channel_module_category_heading_start', 'channel_module_create_pagination', 'channel_module_fetch_pagination_data', 'comment_entries_comment_format', 'comment_entries_tagdata', 'comment_form_end', 'comment_form_hidden_fields', 'comment_form_tagdata', 'comment_preview_comment_format', 'comment_preview_tagdata', 'cp_css_end', 'cp_js_end', 'cp_member_login', 'cp_member_logout', 'cp_members_member_create', 'cp_members_member_create_start', 'cp_members_member_delete_end', 'cp_members_validate_members', 'create_captcha_start', 'delete_comment_additional', 'delete_entries_loop', 'delete_entries_start', 'edit_template_start', 'edit_wiki_article_end', 'edit_wiki_article_form_end', 'edit_wiki_article_form_start', 'email_module_send_email_end', 'email_module_tellafriend_override', 'entry_submission_absolute_end', 'entry_submission_end', 'entry_submission_ready', 'entry_submission_redirect', 'entry_submission_start', 'foreign_character_conversion_array', 'form_declaration_modify_data', 'form_declaration_return', 'forum_submission_form_end', 'forum_submission_form_start', 'forum_submission_page', 'forum_submit_post_end', 'forum_submit_post_start', 'forum_thread_rows_absolute_end', 'forum_thread_rows_loop_end', 'forum_thread_rows_loop_start', 'forum_thread_rows_start', 'forum_threads_template', 'forum_topics_absolute_end', 'forum_topics_loop_end', 'forum_topics_loop_start', 'forum_topics_start', 'insert_comment_end', 'insert_comment_insert_array', 'insert_comment_preferences_sql', 'insert_comment_start', 'login_authenticate_start', 'main_forum_table_rows_template', 'member_edit_preferences', 'member_manager', 'member_member_login_multi', 'member_member_login_single', 'member_member_login_start', 'member_member_logout', 'member_member_register', 'member_member_register_start', 'member_register_validate_members', 'member_update_preferences', 'publish_form_channel_preferences', 'publish_form_entry_data', 'sessions_end', 'sessions_start', 'simple_commerce_evaluate_ipn_response', 'simple_commerce_perform_actions_end', 'simple_commerce_perform_actions_start', 'typography_parse_type_end', 'typography_parse_type_start', 'update_comment_additional', 'update_multi_entries_loop', 'update_multi_entries_start', 'update_template_end', 'wiki_article_end', 'wiki_article_start', 'wiki_special_page', 'wiki_start']

    def run(self):
        self.plugin_path = os.path.join(sublime.packages_path(), "EePackageGenerator")
        self.templates_path = os.path.join(self.plugin_path, "templates")
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
        self.get_package_path()

    def get_package_path(self):
        self.package_name = "my_" + self.chosen_template_name.lower()
        if sublime.platform() == "windows":
            default_package_path = os.path.expanduser("~\\My Documents\\" + self.package_name)
        else:
            default_package_path = os.path.expanduser("~/Documents/" + self.package_name)
        self.window.show_input_panel("Package Location:", default_package_path, self.on_package_path, None, None)

    def on_package_path(self, path):
        self.package_path = path
        self.package_name = os.path.basename(self.package_path)
        self.create_package()

    def create_package(self):
        if os.path.exists(self.package_path) is False:
            shutil.copytree(self.chosen_template_path, self.package_path)
        for root, subFolders, files in os.walk(self.package_path):
            for filename in files:
                if (filename.replace('__package_name__', self.package_name) != filename):
                    os.rename(os.path.join(root, filename), os.path.join(root, filename.replace('__package_name__', self.package_name)))
        self.build_tokens()

    def build_tokens(self):
        self.token_index = 0
        self.tokens = ['package_full_name', 'package_author', 'package_author_url', 'package_version', 'package_doc_url', 'package_description']
        self.token_name = ['Package Full Name', 'Author', 'Author URL', 'Version Number', 'Documentation URL', 'Description']
        self.token_values = {'package_name': self.package_name, 'package_path': self.package_path, 'package_class_name': self.package_name.capitalize()}
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
                extension_hooks_display = [' -- ' + self.token_name[self.token_index] + ' --'] + self.extension_hooks
                self.window.show_quick_panel(extension_hooks_display, self.on_token_value)
            else:
                self.window.show_input_panel(self.token_name[self.token_index], "", self.on_token_value, None, None)
        else:
            self.replace_tokens()

    def on_token_value(self, token_value):
        print token_value
        if self.tokens[self.token_index] in self.boolean_tokens:
            if token_value == 'Yes':
                self.token_values[self.tokens[self.token_index]] = 'y'
            else:
                self.token_values[self.tokens[self.token_index]] = 'n'
        elif self.tokens[self.token_index] in self.ext_list_tokens:
            self.token_values[self.tokens[self.token_index]] = self.extension_hooks[token_value]
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
