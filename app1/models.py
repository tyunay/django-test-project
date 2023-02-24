from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class Syndic(models.Model):
    surname = models.CharField(unique = True, max_length = 30)
    address = models.CharField(max_length = 60)
    license_number = models.IntegerField(unique = True)
    contact_number = models.IntegerField(unique = True)
    email = models.EmailField(max_length = 254, unique = True)

    def get_absolute_url(self):
        return reverse('syndic_detail', kwargs = {'pk': self.pk})


class Secretary(models.Model):
    name = models.CharField(max_length = 30)
    syndic = models.OneToOneField(Syndic, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('secretary_detail', kwargs = {'pk': self.pk})


class Property(models.Model):
    identification_number = models.IntegerField(unique = True)
    price = models.IntegerField()
    syndic = models.ForeignKey(Syndic, on_delete = models.CASCADE)
    date_of_release = models.DateField()

    def get_absolute_url(self):
        return reverse('property_detail', kwargs = {'pk': self.pk})

class CarModel(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    syndics = models.ManyToManyField(Syndic, through = 'CarModelSyndic')

    def get_absolute_url(self):
        return reverse('carmodel_detail', kwargs = {'pk': self.pk})


class CarModelSyndic(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete = models.CASCADE)
    syndic = models.ForeignKey(Syndic, on_delete = models.CASCADE)
    average_speed = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(360)])

    class Meta:
        unique_together = [['car_model', 'syndic']]

    def get_absolute_url(self):
        return reverse('carmodelsyndic_detail', kwargs = {'pk': self.pk})
