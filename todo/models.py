from django.db import models

# Create your models here.

PRIORITY = (("primary", "優先"), ("success", "普通"), ("info", "後回し可"),)
class TodoModel(models.Model):

    title = models.CharField(
        max_length=100,
    )

    memo = models.TextField()

    priority = models.CharField(
        max_length = 150,
        choices = PRIORITY
    )

    duedate = models.DateField(null=True)

    
    def __str__(self):
        return self.title
