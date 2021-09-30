from django.db import models

# Create your models here.
class Category(models.Model):


 name = models.CharField(max_length=256)
 
 def __str__(self):
     return self.name

class Item(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 date = models.DateField()
 image = models.FileField(null=True , blank=True)

 category = models.ForeignKey(Category,
                             related_name='cats',
                             on_delete=models.CASCADE)

 def __str__(self):
     return self.name


class Basket(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 date = models.DateField()
 image = models.FileField()
 

 def __str__(self):
     return self.name



class Foot(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 date = models.DateField()
 image = models.FileField(null=True , blank=True)

 def __str__(self):
     return self.name


class Chess(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 date = models.DateField()
 image = models.FileField(null=True , blank=True)


 def __str__(self):
     return self.name



class Esport(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 date = models.DateField()
 image = models.FileField(null=True , blank=True)


 def __str__(self):
     return self.name



class Ehlel(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 date = models.DateField()
 image = models.FileField(null=True , blank=True)


 def __str__(self):
     return self.name

class Setgegdel(models.Model):


 name = models.CharField(max_length=256)
 desc = models.CharField(max_length=1000)
 def __str__(self):


    return self.name



