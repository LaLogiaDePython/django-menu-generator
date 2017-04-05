from django.apps import AppConfig


class MenuAppConfig(AppConfig):
    name = 'menu_generator'
    label = 'menu_generator'
    verbose_name = 'Menu Application'

    def ready(self):
        pass
