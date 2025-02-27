from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    
    class Meta:
        ordering = ["name"]
    
    def __str__(self) -> str:
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
    
    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen_managment:cook-detail",
                       kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dishtype = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook,
                                   related_name="dishes",
                                   blank=True)
    
    
    class Meta:
        ordering = ["name"]
    
    def __str__(self) -> str:
        return f"{self.name} {self.price}"
