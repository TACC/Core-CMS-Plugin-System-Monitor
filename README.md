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

1. [Assumes Dependencies: Iconworks, Bootstrap](https://github.com/TACC/Core-CMS-Plugin-System-Monitor/issues/2)
2. [Assumes API Endpoint: `/api/system-monitor/`](https://github.com/TACC/Core-CMS-Plugin-System-Monitor/issues/3)
3. [Should Use Python Not JavaScript](https://github.com/TACC/Core-CMS-Plugin-System-Monitor/issues/4)


[system-list]: https://github.com/TACC/Core-CMS-Plugin-System-Monitor/blob/v0.1.5/djangocms_tacc_system_monitor/models.py#L12-L25
