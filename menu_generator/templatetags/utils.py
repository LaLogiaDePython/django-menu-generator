from django.conf import settings
from ..utils import get_callable, clean_app_config

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
        cleaned_app = clean_app_config(app)
        try:
            all_menus_dict = get_callable(cleaned_app + MENU_DICT)
        except ImportError:
            all_menus_dict = None
        except AttributeError:
            all_menus_dict = None
        if all_menus_dict:
            menu_list += all_menus_dict.get(menu_name, [])
    return menu_list
