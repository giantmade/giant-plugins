from django.conf import settings
from django.utils.module_loading import import_string

imports_list = getattr(
    settings,
    "GIANT_PLUGINS_LIST",
    [
        "content_width_video",
        "content_width_image",
        "page_card",
        "pullquote",
        "rich_text",
    ],
)

for plugin in imports_list:
    import_string(f"giant_plugins.{plugin}.cms_plugins.__all__")
