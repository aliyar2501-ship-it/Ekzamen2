from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    """
    Модель для хранения объявлений пользователей.
    Связана с моделью User (автор объявления).
    """
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание объявления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        """Возвращает строковое представление объявления."""
        return self.title


class Comment(models.Model):
    """
    Модель для хранения комментариев к объявлениям.
    Связана с моделями Ad (к какому объявлению) и User (кто написал).
    """
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments', verbose_name="Объявление")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    content = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        """Возвращает строковое представление комментария."""
        return f"Комментарий от {self.author.username} к {self.ad.title}"