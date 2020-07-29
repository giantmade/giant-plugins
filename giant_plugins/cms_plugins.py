from django.conf import settings
from django.utils.module_loading import import_string

include_list = [
        "content_width_video",
        "content_width_image",
        "page_card",
        "pullquote",
        "rich_text",
    ]
exclude_list = getattr(settings, "GIANT_PLUGINS_EXCLUDE_LIST", [])
imports_list = [plugin for plugin in include_list if plugin not in exclude_list]


for plugin in imports_list:
    import_string(f"giant_plugins.{plugin}.cms_plugins.__all__")
