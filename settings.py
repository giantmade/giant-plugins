
SECRET_KEY = "giant-plugins"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

INSTALLED_APPS = [
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    "easy_thumbnails",
    "filer",
    "mptt",
    "django_summernote",
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "mixins",
    "giant_plugins",
]
ROOT_URLCONF = "giant_plugins.tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["giant_plugins/templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

LANGUAGES = [
    ('en-gb', 'English'),
]