from django.db import models
import re
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Address(models.Model):
    phone_num = models.IntegerField()
    city= models.CharField(max_length=45)
    street =  models.CharField(max_length=45)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cloth(models.Model):
    size= models.CharField(max_length=45)
    gender =  models.CharField(max_length=45)
    pic_src = models.CharField(max_length=45)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    quantity= models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE) #relation?????
    total_amount= models.DecimalField(max_digits=10 , decimal_places=2)
    cloth =  models.ManyToManyField(Cloth, through='OrderCloth')

class OrderCloth(models.Model):
    order = models.ForeignKey(Order, related_name="orderclothes", on_delete=models.CASCADE) # related name !!!
    cloth = models.ForeignKey(Cloth, related_name="orderclothes", on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField()
    

    # def save(self, *args, **kwargs):
    #     if self.pk is None: # If this is a new OrderClothes object
    #         # Set the price to the price of the corresponding Clothes object
    #         self.price = self.clothes.price
    #     super().save(*args, **kwargs)
    

