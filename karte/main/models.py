from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Назва" ,max_length=100)
    description = models.TextField(verbose_name="Опис")
    parent_id = models.ForeignKey('self', verbose_name="Батьківська категорія", on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    active = models.BooleanField(verbose_name="Статус" ,default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'