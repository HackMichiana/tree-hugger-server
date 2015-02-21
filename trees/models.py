from django.db import models

# Create your models here.

DIAMETER_CHOICES = (
    ('Y',  'Young'),
    ('E',  'Established'),
    ('M',  'Maturing'),
    ('MA', 'Mature'),
    ('U', 'Unknown')
)

HEIGHT_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('U', 'Unknown')
)

CONDITION_CHOICES = (
    ('E', 'Excellent'),
    ('G', 'Good'),
    ('F', 'Fair'),
    ('P', 'Poor'),
    ('D', 'Dying'),
    ('X', 'Dead'),
    ('U', 'Unknown')
)



class Tree(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField()
    diameter = models.CharField(choices=DIAMETER_CHOICES, max_length=2, default='U')
    height = models.CharField(choices=HEIGHT_CHOICES, max_length=1, default='U')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=1, default='U')
    # maintenance
    # species


class Image(models.Model):
    tree = models.ForeignKey(Tree)
    image = models.ImageField()
    type = models.CharField(choices=[('T', 'Tree'), ('L', 'Leaf')], max_length=1, default='tree')
