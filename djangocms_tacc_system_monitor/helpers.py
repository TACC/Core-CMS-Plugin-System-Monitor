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
