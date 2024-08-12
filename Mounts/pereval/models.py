from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude},{self.longitude},{self.height}'

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


LEVEL = [
    ('1a', '1A'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('4a', '4А'),
    ('4b', '4Б'),
    ('5a', '5А'),
    ('5b', '5Б'),
]


class Level(models.Model):
    winter = models.CharField(max_length=2, choices=LEVEL, verbose_name='Зима', null=True, blank=True, )
    summer = models.CharField(max_length=2, choices=LEVEL, verbose_name='Лето', null=True, blank=True, )
    autumn = models.CharField(max_length=2, choices=LEVEL, verbose_name='Осень', null=True, blank=True, )
    spring = models.CharField(max_length=2, choices=LEVEL, verbose_name='Весна', null=True, blank=True, )

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = 'Уровень сложности перевала'
        verbose_name_plural = 'Уровни сложности перевала'


class Mount(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'
    STATUS = [
        (new, 'новая информация'),
        (pending, 'модератор взял в работу'),
        (accepted, 'модерация прошла успешно'),
        (rejected, 'модерация прошла, информация не принята'),
    ]

    beauty_title = models.CharField(max_length=255, verbose_name='Общее название', default=None)
    title = models.CharField(max_length=255, verbose_name='Название горы', null=True, blank=True)
    other_titles = models.CharField(max_length=255, verbose_name='Альтернативное название горы')
    connect = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default=new)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.pk} {self.beauty_title}'

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'


class Photo(models.Model):
    mount = models.ForeignKey(Mount, related_name='photo', on_delete=models.CASCADE)
    data = models.URLField(verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'


