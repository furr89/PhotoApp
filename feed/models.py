from django.db import models
from sorl.thumbnail import ImageField

# Creation of a model (a model will store data depending on the models.***)
# The text varaible is going to store it and in running 'makemigrations cmd' it will add it to the initial.py
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField(upload_to='uploads') # NOTE whenever adding a new 'feature' to a class, must makemigrations 

    # This will give the name of the object as input
    def __str__(self):
        return self.text