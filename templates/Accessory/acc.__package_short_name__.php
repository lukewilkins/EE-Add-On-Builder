<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
 * ${package_full_name} Accessory
 *
 * @category	Accessory
 * @author		${package_author}
 * @link		${package_author_url}
 */

class ${package_class_name}_acc {

	public $name			= '${package_full_name}';
	public $id				= '${package_short_name}';
	public $version			= '${package_version}';
	public $description		= '${package_description}';
	public $sections		= array();

	/**
	 * Set Sections
	 */
	public function set_sections()
	{
		$EE =& get_instance();

		$this->sections['${package_section}'] = $EE->load->view('accessory_${package_section_short_name}', '', TRUE);

		// Add additional sections (columns) here as needed
		// $this->sections['SECTION TITLE'] = $EE->load->view('accessory_section_title', '', TRUE);

	}

}

/* End of file acc.${package_short_name}.php */
/* Location: /system/expressionengine/third_party/${package_short_name}/acc.${package_short_name}.php */
