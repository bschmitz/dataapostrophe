from django.db import models

class Address(models.Model):
    """
    Address
    """
    address1 = models.CharField(max_length=64)
    address2 = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=24)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s, %s, %s' % (self.address1, self.city, self.state)

class Contact(models.Model):
    """
    Contact
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


