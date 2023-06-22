from django.db import models

# Create your models here.


class regmodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class logmodel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)



class shopregmodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class shoplogmodel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)


class productmodel(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.FileField(upload_to="supplyapp/static")
    def __str__(self):
        return self.name


class wishlistmodel(models.Model):
    uid = models.IntegerField()
    pid = models.IntegerField()
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.FileField(upload_to="supplyapp/static")
    def __str__(self):
        return self.name



class cartmodel(models.Model):
    uid = models.IntegerField()
    pid = models.IntegerField()
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.FileField(upload_to="supplyapp/static")
    def __str__(self):
        return self.name



class buymodel(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    fname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    paymode = models.CharField(max_length=50)
    quantity = models.IntegerField()


    def __str__(self):
        return self.name


class feedmodel(models.Model):
    content = models.CharField(max_length=100)
    image = models.FileField(upload_to="supplyapp/static")

    def __str__(self):
        return self.content