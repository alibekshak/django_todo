from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    complate = models.BooleanField(default=False)

    def __str__(self):
        return self.title