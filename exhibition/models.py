from django.db import models
from dataapostrophe.address.models import Address
from dataapostrophe.artwork.models import ArtWork

class ExhibitionLocation(models.Model):
    """
    A place that has an exhibition.  
    """
    name = models.CharField(max_length=64, unique=True)
    address = models.ForeignKey(Address)
    phone_number = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.name

class Exhibition(models.Model):
    """
    An Artshow or Exhibit
    """

    name = models.CharField(max_length=64, unique=True)
    opening = models.DateField()
    closing = models.DateField()
    reception = models.DateField(null=True, blank=True)
    works_exhibited = models.ManyToManyField(ArtWork, blank=True)
    location = models.ForeignKey(ExhibitionLocation)

    def __unicode__(self):
        return self.name


