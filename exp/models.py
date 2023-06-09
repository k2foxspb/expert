from django.contrib.auth import get_user_model
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title")
    preamble = models.CharField(max_length=1024, verbose_name="Preamble")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ("-created",)
