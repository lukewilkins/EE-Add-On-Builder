#ExpressionEngine Package Generator

Simple Package Builder for ExpressionEngine. Easily generate a base template for any type of ExpressionEngine Add-On.

### Installation
#### Package Control
The easiest way to install is with [Package Control][package-control].

 * Open the Command Palette (`Command+Shift+p` on OS X, `Control+Shift+p` on Linux/Windows).
 * Select "Package Control: Install Package"
 * Select EE Package Generator when the list appears.

#### Manual
If you wish to manually install this plugin, simply clone this repo in to your Sublime Text 2/Packages directory.

### Settings

Settings are accessed via the <kbd>Preferences</kbd> > <kbd>Package Settings</kbd> > <kbd>EE Package Generator</kbd> > <kbd>Settings - User</kbd> menu. Default settings should not be modified, as they are overwritten when the plugin updates. Instead, you should copy the relevant settings into EE Package Generator's user settings file.

By default, EE Package Generator is triggered by pressing `Control-Shift-N`. This can be customized by setting a specific combination in <kbd>Preferences</kbd> > <kbd>Package Settings</kbd> > <kbd>EE Package Generator</kbd> > <kbd>Key Bindings - User</kbd>

    [
        { "keys": ["ctrl+shift+n"], "command": "ee_package_generator" }
    ]

### Usage

Simply press `Control-Shift-N` while working in your desired project to view a list of all Add-On options. Options include:

 * Accessory
 * Extension
 * Fieldtype
 * Module
 * Plugin

After choosing your Add-On type, you will be asked for the relevant pieces of data to get things set up. From there it's just a matter of adding your logic to the generated Add-On! You can refer to the [Expression Engine Docs][ee-docs] for more details on Add-On development.

[package-control]: http://wbond.net/sublime_packages/package_control
[ee-docs]: http://ellislab.com/expressionengine/user-guide/development
