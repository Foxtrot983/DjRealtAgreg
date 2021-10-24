from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


'''def image_directory_field(instance, filename):
    return f'{instance.record.id}/{filename}'
'''
class ThePlace(models.Model):
    #Место скраппинга
    site = models.CharField(max_length=20)

    def __str__(self):
        return self.site

class AgenciesClub(models.Model):
    #список агенств
    name = models.CharField(max_length=50)
    num = models.CharField(max_length=20)
    account = models.CharField(max_length=100)

    def __str__(self):
        return self.site

class Record(models.Model):
    #Запись о квартире
    site = models.ForeignKey(ThePlace, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date = models.DateTimeField()
    rooms = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    '''
    for rooms:
    {
        0: room
        1: 1 room flat
        2: 2 room flat
        3: 3 room flat
        4: 4 room flat
    }
    '''
    roomOrFlat = models.BooleanField(default=True)
    #images = models.ImageField
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    owner = models.CharField(max_length=50)
    isAgent = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Photos(models.Model):
    photo = models.ForeignKey(Record, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')