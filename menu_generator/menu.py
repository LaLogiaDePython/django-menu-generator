import copy


from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
from django.core.exceptions import ImproperlyConfigured

from . import utils as util


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
        """
        self.request = request
        self.path = request.path

    def is_validated(self, item_dict):
        """
        Given a menu item dictionary, it returns true if menu item should be only shown
        to users if a set validators are true. (e.g. show if user is remember of admin group)
        """
        validators = item_dict.get('validators')
        if not validators:
            return True

        if not isinstance(validators, (list, tuple)):
            raise ImproperlyConfigured("validators must be a list")

        for validate in validators:
            if isinstance(validate, tuple):
                if len(validate) <= 1:
                    raise ImproperlyConfigured("You are passing a tuple validator with no params %s" % str(validate))
                func = util.get_callable(validate[0])
                # Using a python slice to get all items after the first to build function args
                args = validate[1:]
                return func(self.request, *args)
            else:
                func = util.get_callable(validate)
                return func or func(self.request) # pragma: no cover

    def has_name(self, item_dict):
        """
        Given a menu item dictionary, it returns true if attribute `name` is set.
        """
        yep = True
        if not item_dict.get('name', False):
            yep = False
        return yep

    def get_url(self, item_dict):
        """
        Given a menu item dictionary, it returns the URL or an empty string.
        """
        final_url = ''
        url = item_dict.get('url', '')
        try:
            final_url = reverse(**url) if type(url) is dict else reverse(url)
        except NoReverseMatch:
            final_url = url
        return final_url

    def has_url(self, item_dict):
        """
        Given a menu item dictionary, it returns true if attribute `url` is set.
        """
        if not self.get_url(item_dict):
            return False
        return True

    def is_selected(self, item_dict):
        """
        Given a menu item dictionary, it returns true if `url` is on path.
        """
        url = self.get_url(item_dict)
        if len(url) and url == self.path:
            return True
        return False

    def process_breadcrums(self, menu_list):
        """
        Given a menu list, it marks the items on the current path as selected, which
        can be used as breadcrumbs
        """
        for item in menu_list:
            if item['submenu']:
                item['selected'] = self.process_breadcrums(item['submenu'])
            if item['selected']:
                return True
        return False

    def get_submenu_list(self, parent_dict, depth):
        """
        Given a menu item dictionary, it returns a submenu if one exist, or
        returns None.
        """
        submenu = parent_dict.get('submenu', None)
        if submenu is not None:
            for child_dict in submenu:
                child_dict['validators'] = list(set(list(parent_dict.get('validators', [])) +
                    list(child_dict.get('validators', []))))
            submenu = self.generate_menu(submenu, depth)
            if not submenu:
                submenu = None
        return submenu

    def get_menu_list(self, list_dict):
        """
        A generator that returns only the visible menu items.
        """
        for item in list_dict:
            if self.has_name(item) and self.has_url(item):
                if self.is_validated(item):
                    yield copy.copy(item)

    def generate_menu(self, list_dict, depth=None):
        """
        Given a list of dictionaries, returns a menu list.
        """
        visible_menu = []
        current_depth = depth or 0
        for item in self.get_menu_list(list_dict):
            item['depth'] = current_depth
            item['url'] = self.get_url(item)
            item['selected'] = self.is_selected(item)
            item['submenu'] = self.get_submenu_list(item, depth=current_depth + 1)
            visible_menu.append(item)

        self.process_breadcrums(visible_menu)

        return visible_menu


class Menu(MenuBase):
    """
    Class that generates menu list.
    """
    def __call__(self, request, list_dict):
        self.save_user_state(request)
        return self.generate_menu(list_dict)

generate_menu = Menu()
