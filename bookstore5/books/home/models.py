from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @staticmethod
    def get_email(email):
        try:
            return Signup.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_pass(password):
        try:
            return Signup.objects.get(password=password)
        except:
            return False

    @staticmethod
    def get_detail(email):
        return Signup.objects.get(email=email)


class Product(models.Model):
    author = models.CharField(max_length=100, default='')
    img = models.ImageField()
    title = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=1000, default='')
    pdf = models.FileField(max_length=1000,null=True,default=None)


    def __str__(self):
        return (str(self.id) + " " + self.title)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_detail(id=0):
        return Product.objects.get(id=id)








