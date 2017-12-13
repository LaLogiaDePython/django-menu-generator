from django import template
from django.conf import settings

from .utils import get_menu_from_apps
from .. import defaults
from ..menu import generate_menu

register = template.Library()


@register.simple_tag(takes_context=True)
def get_menu(context, menu_name):
    """
    Returns a consumable menu list for a given menu_name found in settings.py.
    Else it returns an empty list.

    Update, March 18 2017: Now the function get the menu list from settings and append more items if found on the
    menus.py's 'MENUS' dict.
    :param context: Template context
    :param menu_name: String, name of the menu to be found
    :return: Generated menu
    """
    menu_list = getattr(settings, menu_name, defaults.MENU_NOT_FOUND)
    menu_from_apps = get_menu_from_apps(menu_name)
    # If there isn't a menu on settings but there is menu from apps we built menu from apps
    if menu_list == defaults.MENU_NOT_FOUND and menu_from_apps:
        menu_list = menu_from_apps
    # It there is a menu on settings and also on apps we merge both menus
    elif menu_list != defaults.MENU_NOT_FOUND and menu_from_apps:
        menu_list += menu_from_apps
    return generate_menu(context['request'], menu_list)
