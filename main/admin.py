from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Author)
admin.site.register(models.Books)
admin.site.register(models.Category)
admin.site.register(models.Quotes)
admin.site.register(models.Review)