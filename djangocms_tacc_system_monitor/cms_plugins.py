from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from .helpers import concat_classnames, get_system_data
from .models import TaccsiteSystemMonitor

@plugin_pool.register_plugin
class TaccsiteSystemMonitorPlugin(CMSPluginBase):
    """
    Components > "System Monitor" Plugin
    https://url.to/docs/components/system_monitor/
    """
    module = 'TACC Site'
    model = TaccsiteSystemMonitor
    name = _('System Monitor')
    render_template = 'system_monitor.html'

    cache = True
    text_enabled = False
    allow_children = False

    fieldsets = [
        (_('Single System'), {
            # TODO: Support showing multiple systems
            'description': 'Show the status of which single system?',
            'fields': (
                'system',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        classes = concat_classnames([
            's-system-monitor',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        api_url = request.build_absolute_uri('/api/system-monitor/')
        use_sample = request.get_host().split(':')[0] == 'localhost'
        system_data = get_system_data(api_url, instance.system, use_sample_on_failure=use_sample)

        if system_data:
            context['system_data'] = system_data
            context['system_status'] = 'operational' if system_data.get('is_operational') else 'warning'
        else:
            context['system_data'] = None
            context['system_status'] = 'warning'

        return context
