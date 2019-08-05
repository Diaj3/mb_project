from django.db import models

# Create your models here.
#Since we wanna store the textual content of a message board post, we will use the following:
class Post(models.Model):
    text = models.TextField()  #created a database model called Post wich has the db field text whose type = TextField(), there are many models for different types like char, dates, int, ...

    def __str__(self):
        return self.text[:50] #this will display the 50 char of the text field