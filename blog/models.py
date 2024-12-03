from django.db import models

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    """Класс для описания модели блога"""

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name="Slug", **NULLABLE)
    content = models.TextField(verbose_name="содержимое статьи", **NULLABLE)
    preview = models.ImageField(
        upload_to="blog/preview", verbose_name="изображение", **NULLABLE
    )
    created_at = models.DateField(**NULLABLE, verbose_name="дата публикации")
    number_of_views = models.IntegerField(
        verbose_name="Количество просмотров", default=0
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")

    def __str__(self):
        return f"{self.title} {self.content} {self.created_at} {self.number_of_views}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
