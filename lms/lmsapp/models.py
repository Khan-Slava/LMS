from django.db import models


class Task (models.Model):
    mainTitle = models.CharField('Title', max_length=50)
    mainContent = models.TextField('Opisanie')

    def __str__(self):
        return self.mainTitle

    class Meta:
        verbose_name = 'Notes'
        verbose_name_plural = 'Note'