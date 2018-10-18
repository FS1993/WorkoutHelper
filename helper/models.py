from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)
    category_id = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=64)
    level_id = models.IntegerField(default=1)
    def __str__(self):
        return self.name

# class Equipment(models.Model): #sprzęt do ćwiczeń
#     name = models.CharField(max_length=64)
#     level_id = models.IntegerField(default=1)
#     def __str__(self):
#         return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    reps = models.CharField(max_length=64, default="4x 10-12 pwt")
    level = models.ForeignKey(Level, default=1, on_delete=models.CASCADE)
    #sprzęt do ćwiczeń
    bar = models.BooleanField(default=False)
    parallel_bars = models.BooleanField(default=False)
    def __str__(self):
        return self.name

