from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    MODALITY_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('hibrido', 'Híbrido'),
    ]
    
    TYPE_CHOICES = [
        ('competencia', 'Competencia'),
        ('difusor', 'Difusor'),
    ]

    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    modality = models.CharField(max_length=20, choices=MODALITY_CHOICES)
    location = models.CharField(max_length=200, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.URLField()
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name