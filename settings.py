
SECRET_KEY = "giant-plugins"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "giant-plugins",
    }
}

PLUGINS = [
    "giant_plugins.content_width_image",
    "giant_plugins.content_width_video",
    "giant_plugins.donate",
    "giant_plugins.featured_cta",
    "giant_plugins.hero_image",
    "giant_plugins.logo_grid",
    "giant_plugins.page_card",
    "giant_plugins.pullquote",
    "giant_plugins.rich_text",
    "giant_plugins.share_this_page",
    "giant_plugins.gallery",
    "giant_plugins.key_stats",
]

INSTALLED_APPS = [
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    "easy_thumbnails",
    "filer",
    "mptt",
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "mixins",
    "giant_plugins",
] + PLUGINS

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["giant_plugins/templates"],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

LANGUAGES = [
    ('en-gb', 'English'),
]
SUMMERNOTE_CONFIG = (
    {
        "iframe": True,
        "summernote": {
            "airMode": False,
            # Change editor size
            "width": "100%",
            "height": "480",
            "lang": None,
            "toolbar": [
                ["style", ["style"]],
                ["font", ["bold", "underline", "clear"]],
                ["fontname", ["fontname"]],
                ["color", ["color"]],
                ["para", ["ul", "ol", "paragraph"]],
                ["table", ["table"]],
                ["insert", ["link", "picture", "video"]],
                ["view", ["fullscreen", "codeview", "help"]],
            ],
        },
    },
)
