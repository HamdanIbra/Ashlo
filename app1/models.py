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

class AddressManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['phone']) < 10:
            errors["phone"] = "phone number should be at least 10 characters"
        if len(postData['city']) < 2:
            errors["city"] = "city should be at least 2 characters"
        if len(postData['street']) < 2:
            errors["street"] = "street should be at least 2 characters"
        return errors

class Address(models.Model):
    phone_num = models.IntegerField()
    city= models.CharField(max_length=45)
    street =  models.CharField(max_length=45)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddressManager()

class ClothManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['size']) < 0:
            errors["size"] = "Please enter the size"
        if len(postData['pic_source']) < 6:
            errors["pic_source"] = "Pic source should be at least 6 characters"
        if len(postData['description']) < 10:
            errors["description"] = "description should be at least 10 characters"
        if int(postData['price']) <= 0:
            errors["price"] = "price should be greater than zero"
        if int(postData['quantity']) <= 0:
            errors["quantity"] = "quantity should be greater than zero"
        return errors

class Cloth(models.Model):
    size= models.CharField(max_length=45)
    gender =  models.CharField(max_length=45)
    pic_src = models.CharField(max_length=45)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    quantity= models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClothManager()


# class Order(models.Model):
#     user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE) #relation?????
#     total_amount= models.DecimalField(max_digits=10 , decimal_places=2,null=True)
#     cloth =  models.ManyToManyField(Cloth, through='OrderCloth')

class Clothorder(models.Model):
    user = models.ForeignKey(User,related_name="clothorders", on_delete=models.CASCADE) # related name !!!
    cloth = models.OneToOneField(Cloth, on_delete=models.CASCADE,primary_key=True) 
    quantity= models.PositiveIntegerField(default=1)
    

    # def save(self, *args, **kwargs):
    #     if self.pk is None: # If this is a new OrderClothes object
    #         # Set the price to the price of the corresponding Clothes object
    #         self.price = self.clothes.price
    #     super().save(*args, **kwargs)
    

