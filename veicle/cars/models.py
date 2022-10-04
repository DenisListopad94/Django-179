from django.db import models

# Create your models here.
class Auto(models.Model):
    title = models.CharField(max_length=20,verbose_name="модель")
    speed = models.FloatField(verbose_name="скорость")
    description = models.TextField(verbose_name="описание")
    year_create = models.IntegerField(verbose_name="год выпуска")
    costs = models.IntegerField(null = True,verbose_name="стоимость")
    country = models.ForeignKey("Country",on_delete=models.CASCADE,null = True)
    provider = models.ManyToManyField("Provider")
    def __str__(self):
        return  self.title

    class Meta():
        verbose_name = "Авто"
        verbose_name_plural = "Авто"

class Country(models.Model):
    manufacture = models.TextField(verbose_name= 'страна производитель')
    city = models.CharField(max_length=20,verbose_name="город")
    director = models.OneToOneField("Director",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return  self.manufacture
    class Meta():
        verbose_name = "Страна производитель"
        verbose_name_plural = "Страна производитель"

class Director(models.Model):
    fio = models.CharField(max_length=20,verbose_name="ФИО")
    email = models.CharField(max_length=50,verbose_name="Почта")

    def __str__(self):
        return  self.fio
    class Meta():
        verbose_name = "Директор"
        verbose_name_plural = "Директор"

class Provider(models.Model):
    name_prov = models.CharField(max_length=20,verbose_name="поставщик")
    adress = models.CharField(max_length=20,verbose_name="aдрес")
    detail = models.TextField(verbose_name="детали")

    def __str__(self):
        return  self.name_prov
    class Meta():
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщик"

class Form_model_comment(models.Model):
    title = models.CharField(max_length=50,verbose_name="заголовок комментария")
    content = models.CharField(max_length=255,verbose_name="Описание комментария")
    published = models.BooleanField()
    def __str__(self):
        return  self.title