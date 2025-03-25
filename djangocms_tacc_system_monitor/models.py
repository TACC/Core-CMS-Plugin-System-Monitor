from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext as _

from django.db import models

from djangocms_attributes_field import fields

from .helpers import get_choices
from .constants import DEFAULT_SYSTEM

SYSTEM_DICT = {
    'vista.tacc.utexas.edu': {
        'description': 'Vista'
    },
    'frontera.tacc.utexas.edu': {
        'description': 'Frontera'
    },
    'stampede3.tacc.utexas.edu': {
        'description': 'Stampede2'
    },
    'lonestar6.tacc.utexas.edu': {
        'description': 'Lonestar6'
    },
}
SYSTEM_CHOICES = get_choices(SYSTEM_DICT)

class TaccsiteSystemMonitor(CMSPlugin):
    """
    Components > "System Monitor" Model
    """
    system = models.CharField(
        verbose_name=_('System'),
        choices=SYSTEM_CHOICES,
        blank=False,
        max_length=255,
        default=DEFAULT_SYSTEM,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        system_choice = SYSTEM_DICT[self.system]
        return system_choice['description']
