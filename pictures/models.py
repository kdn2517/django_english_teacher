from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=20, unique=True, verbose_name='Слово')
    translation = models.TextField(verbose_name='Перевод')
    studied = models.BooleanField(default=False, verbose_name='Изучено')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'


class Images(models.Model):
    image = models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='Картинка')
    translation = models.TextField(verbose_name='Перевод текста')
    words = models.ManyToManyField('Words', verbose_name='Связанные слова')

    def __str__(self):
        return self.translation[:25] + '...'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

