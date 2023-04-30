from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from exp import models as exp_models


@admin.register(exp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]