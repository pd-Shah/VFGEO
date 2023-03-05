from os import getenv

env = getenv("DJANGO_ENV", default="development")

if env == "production" or env == "testing":
    from .prod import *
else:
    from .dev import *
