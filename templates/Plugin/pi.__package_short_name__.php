<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

/**
 * ${package_full_name} Plugin
 *
 * @category    Plugin
 * @author      ${package_author}
 * @link        ${package_author_url}
 */

$plugin_info = array(
    'pi_name'       => '${package_full_name}',
    'pi_version'    => '${package_version}',
    'pi_author'     => '${package_author}',
    'pi_author_url' => '${package_author_url}',
    'pi_description'=> '${package_description}',
    'pi_usage'      => ${package_class_name}::usage()
);


class ${package_class_name} {

    public $return_data;

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
     * Plugin Usage
     */
    public static function usage()
    {
        ob_start();
?>
<h3>${package_full_name}</h3>
<p>${package_description}</p>
<hr/>
Include your documentation here...
<?php
        $buffer = ob_get_contents();
        ob_end_clean();
        return $buffer;
    }
}


/* End of file pi.${package_short_name}.php */
/* Location: /system/expressionengine/third_party/${package_short_name}/pi.${package_short_name}.php */
