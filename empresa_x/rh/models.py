from django.db import models

# Create your models here.

class Employer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    adress = models.CharField(max_length= 200)
    # cep
    # birthday = 
    # cpf = 
    # phone =
    # date_started =
    # dados bancários

    
    
    file_docs = models.FileField(upload_to='uploads/docs', blank=True)
    # photo_file = models.ImageField(upload_to= 'uploads/photo')





