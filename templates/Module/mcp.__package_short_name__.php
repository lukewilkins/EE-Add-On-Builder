<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
 * ${package_full_name} Module Control Panel File
 *
 * @category	Module
 * @author		${package_author}
 * @link		${package_author_url}
 */

class ${package_class_name}_mcp {

	public $return_data;

	private $_base_url;

	// --------------------------------------------------------------------

	/**
	 * Constructor
	 */
	public function __construct()
	{
		$this->EE =& get_instance();

		$this->_base_url = BASE.AMP.'C=addons_modules'.AMP.'M=show_module_cp'.AMP.'module=${package_short_name}';

		$this->EE->cp->set_right_nav(array(
			'module_home'	=> $this->_base_url,
			// Add more right nav items here.
		));
	}

	// --------------------------------------------------------------------

	/**
	 * Index Function
	 *
	 * @return 	void
	 */
	public function index()
	{
		$this->EE->cp->set_variable('cp_page_title',
								lang('${package_short_name}_module_name'));

		/**
		 * This is the addons home page, add more code here!
		 */
	}

	// --------------------------------------------------------------------

	/**
	 * Start on your custom code here...
	 */

}

/* End of file mcp.${package_short_name}.php */
/* Location: /system/expressionengine/third_party/${package_short_name}/mcp.${package_short_name}.php */
