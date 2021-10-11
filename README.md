## Texas Advanced Computing Center
# Django CMS Plugin: "Plugin Name"

This plugin [does something].

- __`__plugin_name__`__: `taccsite_example`
- __`__PluginName__`__: `TaccsiteExample`
- __"Plugin Name"__: "Example"

## For Plugin Developer

After cloning this repository for your plugin:

1. Follow https://github.com/tacc-wbomar/Core-CMS-Plugin/wiki/Core-CMS-Plugin-Development-Quick-Start.
2. Remove this section from your repository's `README.md`.


## Quick Start

1. Follow https://github.com/tacc-wbomar/Core-CMS-Plugin/wiki/Core-CMS-Plugin-Usage-Quick-Start.

> The next steps are sample steps that should be replaced with plugin-specific steps, if any.

2. Any step that is specific to the plugin, such as the steps after this.

    ```
    # provide minimal example code that may help the reader
    ```

3. Add a URLconf in your Django project's `urls.py` like this:

    ```
        url(r'^sysmon/', include('__plugin_name__.urls')),
    ```

4. Add `__plugin_name_some_prop__` property and value to your Django project's settings:

    ```
    __plugin_name_some_prop__ = 'specific_value'
    ```

5. Visit [http://your.project.url.host/some_plugin_url_path/](http://127.0.0.1:8000/ "The URL for your environment may be different than this.").
