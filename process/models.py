from django.db import models

LABEL_CHOICES = (
    ('0','0'),
    ('1','1'),
)

class InputData(models.Model):
    text = models.TextField(null=True,blank=True)
    title = models.TextField(null=True,blank=True)
    result = models.CharField(max_length=50,choices=LABEL_CHOICES,null=True,blank=True)

    def __str__(self):
        return f"{self.text}"

class Contribution(models.Model):
    text = models.TextField(null=True,blank=True)
    title = models.TextField(null=True,blank=True)
    label = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.text   