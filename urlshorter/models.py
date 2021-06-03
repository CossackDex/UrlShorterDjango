from django.db import models
from django.urls import reverse_lazy

from .utils import create_random_url


class UrlShortener(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    click_counter = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=False)

    class Meta:
        ordering = ["-create_date"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def click(self):
        self.click_counter += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_random_url(self)
        super().save(*args, **kwargs)
