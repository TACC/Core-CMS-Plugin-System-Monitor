# Fetch system monitor data from API (server-side; no JavaScript)
import json
import logging
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

from .constants import API_SAMPLE_DATA

logger = logging.getLogger(__name__)


# Fetch system monitor data from API
def fetch_system_monitor_data(api_url, timeout=10):
    """Fetch list of system dicts from /api/system-monitor/. Returns None on error."""
    try:
        req = Request(api_url, method='GET')
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except (URLError, HTTPError, ValueError, OSError) as e:
        logger.warning('System monitor API request failed: %s', e)
        return None

# Get system data for a given hostname
def get_system_data(api_url, hostname, use_sample_on_failure=False):
    """
    Return the system dict for the given hostname, or None if not found.
    If use_sample_on_failure is True and the API fails, return data from
    API_SAMPLE_DATA for that hostname if present.
    """
    data = fetch_system_monitor_data(api_url)
    if data is None and use_sample_on_failure:
        data = API_SAMPLE_DATA
    if not data:
        return None
    for system in data:
        if system.get('hostname') == hostname:
            return system
    return None


# Get Django `models.CharField` `choices`
# SEE: https://github.com/TACC/Core-CMS/blob/75b219c/taccsite_cms/contrib/helpers.py
def get_choices(choice_dict):
    """Get a sequence for a Django model field choices from a dictionary.
    :param Dict[str, Dict[str, str]] dictionary: choice as key for dictionary of classnames and descriptions
    :return: a sequence for django.db.models.CharField.choices
    :rtype: List[Tuple[str, str], ...]
    """
    choices = []

    for key, data in choice_dict.items():
        choice = (key, data['description'])
        choices.append(choice)

    return choices

# Concatenate a list of CSS classes
# SEE: https://github.com/TACC/Core-CMS/blob/75b219c/taccsite_cms/contrib/helpers.py
def concat_classnames(classes):
    """Concatenate a list of classname strings (without failing on None)"""
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)
