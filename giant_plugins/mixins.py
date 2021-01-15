from cms.plugin_base import CMSPluginBase
from django.utils.module_loading import import_string

from django.conf import settings


class ExtendedPluginBase(CMSPluginBase):
    """
    An extension of the plugin base to allow us to
    use getattr calls for some of the fields such as 
    form/formfields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form = self.get_form_class()

    @classmethod
    def get_form_class(cls):
        return import_string(getattr(settings, f"{cls.__name__.upper()}_FORM", None))