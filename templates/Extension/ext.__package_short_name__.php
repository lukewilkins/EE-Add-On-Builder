<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
 * ${package_full_name} Extension
 *
 * @category	Extension
 * @author		${package_author}
 * @link		${package_author_url}
 */

class ${package_class_name}_ext {

	public $settings 		= array();
	public $description		= '${package_description}';
	public $docs_url		= '${package_doc_url}';
	public $name			= '${package_full_name}';
	public $settings_exist	= '${package_has_control_panel_settings}';
	public $version			= '${package_version}';

	private $EE;

	// --------------------------------------------------------------------

	/**
	 * Constructor
	 *
	 * @param 	mixed	Settings array or empty string if none exist.
	 */
	public function __construct($settings = '')
	{
		$this->EE =& get_instance();
		$this->settings = $settings;
	}

	// --------------------------------------------------------------------

	/**
	 * Settings Form
	 *
	 * If you wish for ExpressionEngine to automatically create your settings
	 * page, work in this method.  If you wish to have fine-grained control
	 * over your form, use the settings_form() and save_settings() methods
	 * instead, and delete this one.
	 *
	 * @see http://expressionengine.com/user_guide/development/extensions.html#settings
	 */
	public function settings()
	{
		return array(

		);
	}

	// --------------------------------------------------------------------

	/**
	 * Activate Extension
	 *
	 * This function enters the extension into the exp_extensions table
	 *
	 * @see http://codeigniter.com/user_guide/database/index.html for
	 * more information on the db class.
	 *
	 * @return void
	 */
	public function activate_extension()
	{
		// Setup custom settings in this array.
		$this->settings = array();

		$hooks = array(
			'${package_ext_hook}'	=> '${package_ext_hook_method}',
		);

		foreach ($hooks as $hook => $method)
		{
			$data = array(
				'class'		=> __CLASS__,
				'method'	=> $method,
				'hook'		=> $hook,
				'settings'	=> serialize($this->settings),
				'version'	=> $this->version,
				'enabled'	=> 'y'
			);

			$this->EE->db->insert('extensions', $data);
		}
	}

	// --------------------------------------------------------------------

	/**
	 * ${package_ext_hook_method}
	 *
	 * @param
	 * @return
	 */
	public function ${package_ext_hook_method}()
	{
		// Add Code for the ${package_ext_hook} hook here.
	}

	// --------------------------------------------------------------------

	/**
	 * Disable Extension
	 *
	 * This method removes information from the exp_extensions table
	 *
	 * @return void
	 */
	function disable_extension()
	{
		$this->EE->db->where('class', __CLASS__);
		$this->EE->db->delete('extensions');
	}

	// --------------------------------------------------------------------

	/**
	 * Update Extension
	 *
	 * This function performs any necessary db updates when the extension
	 * page is visited
	 *
	 * @return 	mixed	void on update / false if none
	 */
	function update_extension($current = '')
	{
		if ($current == '' OR $current == $this->version)
		{
			return FALSE;
		}
	}
}

/* End of file ext.${package_short_name}.php */
/* Location: /system/expressionengine/third_party/${package_short_name}/ext.${package_short_name}.php */
