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
2. Choose the system to monitor.
3. See plugin render system information.

## Features

1. Renders available data from chosen system.
2. Supports [specific systems][system-list] e.g. Vista, Frontera.
3. Can render sample data on `localhost` (assumes API is unavailable).

## Caveats

1. [Assumes Dependencies: Iconworks, Bootstrap](https://github.com/TACC/Core-CMS-Plugin-System-Monitor/issues/2)
2. [Assumes API Endpoint: `/api/system-monitor/`](https://github.com/TACC/Core-CMS-Plugin-System-Monitor/issues/3)


[system-list]: https://github.com/TACC/Core-CMS-Plugin-System-Monitor/blob/v0.3.0/djangocms_tacc_system_monitor/models.py#L12-L25
