## Texas Advanced Computing Center
# Django CMS Plugin: "System Monitor"

This plugin [does something].

- __`__plugin_name__`__: `taccsite_system_monitor`
- __`__PluginName__`__: `TaccsiteSystemMonitor`
- __"Plugin Name"__: "System Monitor"

## Quick Start

1. Follow https://github.com/tacc-wbomar/Core-CMS-Plugin/wiki/Core-CMS-Plugin-Usage-Quick-Start.

## Usage

1. Add instance of plugin to a page.
1. Choose the system to monitor.
1. See plugin render system information.

## Features

1. Renders available data from chosen system.
1. Supports systems Frontera, Stampede2, Maverick2, [and more][system-list].

## Caveats

The markup assumes the availability of styles for two third-party components:

- [`iconworks`](https://icon-works.com/)
- [`badge`](https://getbootstrap.com/docs/4.0/components/badge/)



[system-list]: https://github.com/tacc-wbomar/Core-CMS-Plugin-System-Monitor/blob/main/taccsite_system_monitor/models.py
