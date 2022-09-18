from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class ResumeModel(models.Model):
    BookName = models.CharField("Book Name",max_length=50)
    AuthorName = models.CharField("Author name", max_length=50)
    file = models.FileField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    class Meta:
        db_table = "student"
        