<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
 * ${package_full_name} Fieldtype File
 *
 * @category    Fieldtype
 * @author      ${package_author}
 * @link        ${package_author_url}
 */

class ${package_class_name}_ft extends EE_Fieldtype {

    var $info = array(
        'name'      => '${package_full_name}',
        'version'   => '${package_version}'
    );

    // --------------------------------------------------------------------

    /**
     * Post delete custom logic after an entry is deleted
     *
     * @access  public
     * @param   array of the deleted entry_ids
     * @return
     *
     */
    function delete($ids)
    {

    }


    // --------------------------------------------------------------------

    /**
     * Display Field on Publish Page
     *
     * @access  public
     * @param   existing data
     * @return  field html
     *
     */
    function display_field($data)
    {

    }


    // --------------------------------------------------------------------

    /**
     * Display Global Settings
     *
     * @access  public
     * @return  form contents
     *
     */
    function display_global_settings()
    {

    }

    // --------------------------------------------------------------------

    /**
     * Display Settings Screen for single field
     *
     * @access  public
     * @return  default settings
     *
     */
    function display_settings($data)
    {
        /*
        $prefix = 'myfield';

        $this->field_formatting_row($data, $prefix);
        $this->text_direction_row($data, $prefix);
        $this->field_show_formatting_btns_row($data, $prefix);
        $this->field_show_smileys_row($data, $prefix);
        $this->field_show_glossary_row($data, $prefix);
        $this->field_show_spellcheck_row($data, $prefix);
        $this->field_show_writemode_row($data, $prefix);
        $this->field_show_file_selector_row($data, $prefix);
        */
    }


    // --------------------------------------------------------------------

    /**
     * Install Fieldtype
     *
     * @access  public
     * @return  array of default global settings
     *
     */
    function install()
    {

    }

    // --------------------------------------------------------------------

    /**
     * Preprocess data on frontend
     *
     * @access  public
     * @param   field data
     * @return  prepped data
     *
     */
    function pre_process($data)
    {

    }

    // --------------------------------------------------------------------

    /**
     * Post save custom logic after an entry is saved
     *
     * @access  public
     * @param   submitted field data and entry_id
     * @return
     *
     */
    function post_save($data)
    {

    }

    // --------------------------------------------------------------------

    /**
     * Post save settings additional processing after the field is created/modified
     *
     * @access  public
     * @param   submitted settings for the field
     * @return
     *
     */
    function post_save_settings($data)
    {

    }


    // --------------------------------------------------------------------

    /**
     * Replace tag
     *
     * @access  public
     * @param   field data
     * @param   field parameters
     * @param   data between tag pairs
     * @return  replacement text
     *
     */
    function replace_tag($data, $params = array(), $tagdata = FALSE)
    {

    }

    // --------------------------------------------------------------------

    /**
     * Save Data
     *
     * @access  public
     * @param   submitted field data
     * @return  string to save
     *
     */
    function save($data)
    {

    }



    // --------------------------------------------------------------------

    /**
     * Save Global Settings
     *
     * @access  public
     * @return  global settings
     *
     */
    function save_global_settings()
    {
        return array_merge($this->settings, $_POST);
    }


    // --------------------------------------------------------------------

    /**
     * Save Settings
     *
     * @access  public
     * @param   submitted settings for single field
     * @return  field settings
     *
     */
    function save_settings($data)
    {

    }

    // --------------------------------------------------------------------

    /**
     * Uninstall Fieldtype
     *
     * @access  public
     * @param   field settings and action indicator
     * @return  fields to modify
     *
     */
    function settings_modify_column($params)
    {

    }

    // --------------------------------------------------------------------

    /**
     * Uninstall Fieldtype - channel_data is dropped automatically
     *
     * @access  public
     * @return
     *
     */
    function uninstall()
    {

    }

    // --------------------------------------------------------------------

    /**
     * Validate field input
     *
     * @access  public
     * @param   submitted field data
     * @return  TRUE or an error message
     *
     */
    function validate($data)
    {

    }

}

/* End of file ft.${package_short_name}.php */
/* Location: /system/expressionengine/third_party/${package_short_name}/ft.${package_short_name}.php */
