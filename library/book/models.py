from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
        	
    origin_year = models.IntegerField(default="")
    author = models.CharField(max_length=300)
    plot = models.TextField(max_length=300, default="")
                
    def get_absolute_url(self):
	    return f"/{self.pk}"
