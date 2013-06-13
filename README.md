#ExpressionEngine Add-On Builder

SublimeText plugin to easily build ExpressionEngine Add-Ons.

### Installation
#### Package Control
The easiest way to install is with [Package Control][package-control].

 * Open the Command Palette (`Command+Shift+p` on OS X, `Control+Shift+p` on Linux/Windows).
 * Select "Package Control: Install Package"
 * Search/Select "ExpressionEngine Add-On Builder" (or EE Add-On Builder) when the list appears.

#### Manual
If you wish to manually install this plugin, simply clone this repo in to your Sublime Text 2/Packages directory.

### Settings

Settings are accessed via the <kbd>Preferences</kbd> > <kbd>Package Settings</kbd> > <kbd>EE Add-On Builder</kbd> > <kbd>Settings - User</kbd> menu. Default settings should not be modified, as they are overwritten when the plugin updates. Instead, you should copy the relevant settings into EE Add-On Builder's user settings file.

By default, EE Add-On Builder is triggered by pressing `Ctrl+Alt+e`. This can be customized by setting a specific combination in <kbd>Preferences</kbd> > <kbd>Package Settings</kbd> > <kbd>EE Add-On Builder</kbd> > <kbd>Key Bindings - User</kbd>

    [
        { "keys": ["ctrl+alt+e"], "command": "ee_add_on_builder" }
    ]

### Usage

Simply press `Ctrl+Alt+e` while working in your desired project to view a list of all Add-On options. Options include:

 * Accessory
 * Extension
 * Fieldtype
 * Module
 * Plugin

After choosing your Add-On type, you will be asked for the relevant pieces of data to get things set up. From there it's just a matter of adding your logic to the generated Add-On! You can refer to the [Expression Engine Docs][ee-docs] for more details on Add-On development.

In the event that you wish to add a new Add-On type to an existing Add-On you've created (for example, you've created a module and now want to add an extension), simply go through the process again with the same Package Name and path and the plugin will allow you to automatically merge that in.

[package-control]: http://wbond.net/sublime_packages/package_control
[ee-docs]: http://ellislab.com/expressionengine/user-guide/development
