from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False, null=True, blank=True)
    number=models.CharField(max_length=100, blank=False, null=False)
    create_at= models.DateTimeField("Create time", auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name= models.CharField(max_length=200, null=True, blank=True)
    country=models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=100, blank=False, null=False)
    images = models.ImageField(upload_to="images/", null=True, blank=True)
    create_at = models.DateTimeField("Create time", auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    chat_id =  models.IntegerField(blank=True, null=True)
    name= models.CharField(max_length=200, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    create_at = models.DateTimeField("Create_at", auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user_id = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.body)

