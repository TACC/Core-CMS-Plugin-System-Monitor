## Texas Advanced Computing Center
# Django CMS Plugin: "System Monitor"

This plugin renders a visual display of simple stats for a chosen system.

- __`__dist-name__`__: `djangocms-tacc-system-monitor`
- __`__package_name__`__: `djangocms_tacc_system_monitor`
- __`__ClassName__`__: `TaccsiteSystemMonitor`
- __"Plugin Name"__: "System Monitor"

## Quick Start

1. Follow https://github.com/TACC/Django-App/wiki/Usage-Quick-Start.

## Usage

1. Add instance of plugin to a page.
1. Choose the system to monitor.
1. See plugin render system information.

## Features

1. Renders available data from chosen system.
1. Supports systems Vista, Frontera, Stampede2, Maverick2, [and more][system-list].
1. Can render sample data.
    <details><summary>To load sample data…</summary>

    1. Load CMS on a `localhost` URL.
    2. Via plugin, choose Frontera or Stampede system.

    </details>

## Caveats

1. The markup assumes the availability of styles for two third-party components:
    - [`iconworks`](https://icon-works.com/)
    - [`badge`](https://getbootstrap.com/docs/4.0/components/badge/)
1. The script assumes the availability of an API endpoint that returns JSON:
    - URL: `/api/system-monitor`
    - JSON: [live](https://frontera-portal.tacc.utexas.edu/api/system-monitor/) ([sample](taccsite_system_monitor/static/taccsite_system_monitor/js/system_monitor.js#L36))
2. This plugin could use server-side logic instead. For details, see [app README.md](https://github.com/wesleyboar/Core-CMS-Plugin-System-Monitor/blob/main/djangocms_tacc_system_monitor/README.md).



[system-list]: https://github.com/wesleyboar/Core-CMS-Plugin-System-Monitor/blob/main/djangocms_tacc_system_monitor/models.py
