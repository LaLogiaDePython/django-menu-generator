from importlib import import_module

from django.apps import apps
from django.core.exceptions import ImproperlyConfigured


def get_callable(func_or_path):
    """
    Receives a dotted path or a callable, Returns a callable or None
    """
    if callable(func_or_path):
        return func_or_path

    module_name = '.'.join(func_or_path.split('.')[:-1])
    function_name = func_or_path.split('.')[-1]
    _module = import_module(module_name)
    func = getattr(_module, function_name)
    return func


def clean_app_config(app_path):
    """
    Removes the AppConfig path for this app and returns the new string
    """
    apps_names = [app.name for app in apps.get_app_configs()]
    if app_path in apps_names:
        return app_path
    else:
        app_split = app_path.split('.')
        new_app = '.'.join(app_split[:-2])
        if new_app in apps_names:
            return new_app
        else:  # pragma: no cover
            raise ImproperlyConfigured(
                "The application {0} is not in the configured apps or does" +
                "not have the pattern app.apps.AppConfig".format(app_path)
            )
