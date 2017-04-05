from django import template
from django.conf import settings

from ..utils import get_callable
from ..menu import generate_menu
from .. import defaults as defs

register = template.Library()

MENU_DICT = ".menus.MENUS"


def get_menu_from_apps(menu_name):
    """
    Returns a consumable menulist for a given menu_name found in each menus.py file (if exists) on each app on
    INSTALLED_APPS
    :param menu_name: String, name of the menu to be found
    :return: Consumable menu list
    """
    installed_apps = getattr(settings, "INSTALLED_APPS", [])
    menu_list = []
    for app in installed_apps:
        try:
            all_menus_dict = get_callable(app + MENU_DICT)
        except ImportError:
            all_menus_dict = None
        except AttributeError:
            all_menus_dict = None
        if all_menus_dict:
            menu_list += all_menus_dict.get(menu_name, [])
    return menu_list


@register.assignment_tag(takes_context=True)
def get_menu(context, menu_name):
    """
    Returns a consumable menu list for a given menu_name found in settings.py.
    Else it returns an empty list.

    Update, March 18 2017: Now the function get the menu list from settings and append more items if found on the
    menus.py's 'MENUS' dict.
    """
    menu_list = getattr(settings, menu_name, defs.MENU_NOT_FOUND)
    menu_from_apps = get_menu_from_apps(menu_name)
    if menu_list == defs.MENU_NOT_FOUND and menu_from_apps:
        menu_list = menu_from_apps
    elif menu_list != defs.MENU_NOT_FOUND and menu_from_apps:
        menu_list += menu_from_apps
    return generate_menu(context['request'], menu_list)
