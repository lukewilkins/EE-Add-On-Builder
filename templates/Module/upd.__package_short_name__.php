<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
 * ${package_full_name} Module Install/Update File
 *
 * @category	Module
 * @author		${package_author}
 * @link		${package_author_url}
 */

class ${package_class_name}_upd {

	public $version = '${package_version}';

	private $EE;

	// --------------------------------------------------------------------

	/**
	 * Constructor
	 */
	public function __construct()
	{
		$this->EE =& get_instance();
	}

	// --------------------------------------------------------------------

	/**
	 * Installation Method
	 *
	 * @return 	boolean 	TRUE
	 */
	public function install()
	{
		$mod_data = array(
			'module_name'			=> '${package_class_name}',
			'module_version'		=> $this->version,
			'has_cp_backend'		=> "${package_has_control_panel_page}",
			'has_publish_fields'	=> 'n'
		);

		$this->EE->db->insert('modules', $mod_data);

		// $this->EE->load->dbforge();
		/**
		 * In order to setup your custom tables, uncomment the line above, and
		 * start adding them below!
		 */

		return TRUE;
	}

	// --------------------------------------------------------------------

	/**
	 * Uninstall
	 *
	 * @return 	boolean 	TRUE
	 */
	public function uninstall()
	{
		$mod_id = $this->EE->db->select('module_id')
								->get_where('modules', array(
									'module_name'	=> '${package_class_name}'
								))->row('module_id');

		$this->EE->db->where('module_id', $mod_id)
					 ->delete('module_member_groups');

		$this->EE->db->where('module_name', '${package_class_name}')
					 ->delete('modules');

		// $this->EE->load->dbforge();
		// Delete your custom tables & any ACT rows
		// you have in the actions table

		return TRUE;
	}

	// --------------------------------------------------------------------

	/**
	 * Module Updater
	 *
	 * @return 	boolean 	TRUE
	 */
	public function update($current = '')
	{
		// If you have updates, drop 'em in here.
		return TRUE;
	}
}

/* End of file upd.${package_short_name}.php */
/* Location: /system/expressionengine/third_party/${package_short_name}/upd.${package_short_name}.php */
