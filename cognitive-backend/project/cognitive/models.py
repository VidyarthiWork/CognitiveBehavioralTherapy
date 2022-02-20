from django.db import models

# Create your models here.


class CognitiveModel(models.Model):
    text = models.CharField(max_length=200)

    def _str_(self):
        return self.text
