from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PointOfSale(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Visit {self.datetime}"
