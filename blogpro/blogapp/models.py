from django.db import models

class Blog_Data(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField()
    text=models.TextField()

    def __str__(self):
        return self.name


class Email_msg(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=200)
    msg=models.TextField()

    def __str__(self):
        return self.name
