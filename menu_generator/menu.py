import copy

import django
from django.core.exceptions import ImproperlyConfigured
from .utils import get_callable, parse_url, path_startswith

if django.VERSION >= (1, 10):  # pragma: no cover
    from django.urls import reverse, NoReverseMatch
else:
    from django.core.urlresolvers import reverse, NoReverseMatch


class MenuBase(object):
    """
    Base class that generates menu list.
    """

    def __init__(self):
        self.path = ''
        self.request = None

    def save_user_state(self, request):
        """
        Given a request object, store the current user attributes
        :param request: HttpRequest
        """
        self.request = request
        self.path = request.path

    def _is_validated(self, item_dict):
        """
        Given a menu item dictionary, it returns true if the user passes all the validator's conditions, it means,
        if the user passes all the conditions, the user can see the menu
        """
        validators = item_dict.get('validators')
        if not validators:
            return True

        if not isinstance(validators, (list, tuple)):
            raise ImproperlyConfigured("validators must be a list")

        result_validations = []
        for validator in validators:
            if isinstance(validator, tuple):
                if len(validator) <= 1:
                    raise ImproperlyConfigured("You are passing a tuple validator without args %s" % str(validator))
                func = get_callable(validator[0])
                # Using a python slice to get all items after the first to build function args
                args = validator[1:]
                # Pass the request as first arg by default
                result_validations.append(func(self.request, *args))
            else:
                func = get_callable(validator)
                result_validations.append(func(self.request))  # pragma: no cover
        return all(result_validations)

    def _has_attr(self, item_dict, attr):
        """
        Given a menu item dictionary, it returns true if an attr is set.
        """
        if item_dict.get(attr, False):
            return True
        return False

    def _get_icon(self, parent_dict):
        """
        Given a menu item dictionary, this returns an icon class if one exist, or
        returns an empty string.
        """
        return parent_dict.get('icon_class', '')

    def _get_url(self, item_dict):
        """
        Given a menu item dictionary, it returns the URL or an empty string.
        """
        url = item_dict.get('url', '')
        return parse_url(url)

    def _get_related_urls(self, item_dict):
        """
        Given a menu item dictionary, it returns the relateds URLs or an empty list.
        """
        related_urls = item_dict.get('related_urls', [])
        return [parse_url(url) for url in related_urls]

    def _is_selected(self, item_dict):
        """
        Given a menu item dictionary, it returns true if `url` is on path,
        unless the item is marked as a root, in which case returns true if `url` is part of path.

        If related URLS are given, it also returns true if one of the related URLS is part of path.
        """
        url = self._get_url(item_dict)
        if self._is_root(item_dict) and path_startswith(self.path, url):
            return True
        elif url == self.path:
            return True
        else:
            # Go through all related URLs and test 
            for related_url in self._get_related_urls(item_dict):
                if path_startswith(self.path, related_url):
                    return True
        return False

    def _is_root(self, item_dict):
        """
        Given a menu item dictionary, it returns true if item is marked as a `root`.
        """
        return item_dict.get('root', False)

    def _process_breadcrums(self, menu_list):
        """
        Given a menu list, it marks the items on the current path as selected, which
        can be used as breadcrumbs
        """
        for item in menu_list:
            if item['submenu']:
                item['selected'] = self._process_breadcrums(item['submenu'])
            if item['selected']:
                return True
        return False

    def _get_submenu_list(self, parent_dict):
        """
        Given a menu item dictionary, it returns a submenu if one exist, or
        returns None.
        """
        submenu = parent_dict.get('submenu', None)
        if submenu:
            for child_dict in submenu:
                # This does a join between the menu item validators and submenu item validators and stores it on the
                # submenu's validators
                child_dict['validators'] = list(
                    set(list(parent_dict.get('validators', [])) + list(child_dict.get('validators', [])))
                )
            submenu = self.generate_menu(submenu)
            if not submenu:
                submenu = None
        return submenu

    def _get_menu_list(self, list_dict):
        """
        A generator that returns only the visible menu items.
        """
        for item in list_dict:
            if self._has_attr(item, 'name') and self._has_attr(item, 'url'):
                if self._is_validated(item):
                    yield copy.copy(item)

    def generate_menu(self, list_dict):
        """
        Given a list of dictionaries, returns a menu list.
        """
        visible_menu = []
        for item in self._get_menu_list(list_dict):
            item['url'] = self._get_url(item)
            item['selected'] = self._is_selected(item)
            item['submenu'] = self._get_submenu_list(item)
            item['icon_class'] = self._get_icon(item)
            visible_menu.append(item)
        self._process_breadcrums(visible_menu)

        return visible_menu


class Menu(MenuBase):
    """
    Class that generates menu list.
    """

    def __call__(self, request, list_dict):
        self.save_user_state(request)
        return self.generate_menu(list_dict)


generate_menu = Menu()
