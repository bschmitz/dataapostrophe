from django.db import models

ROMAN_MONTHS = {
    1:'I',
    2:'II',
    3:'III',
    4:'IV',
    5:'V',
    6:'VI',
    7:'VII',
    8:'VIII',
    9:'IX',
    10:'X',
    11:'XI',
    12:'XII'
}


class ArtWork(models.Model):
    """
    Model of a piece of art.  
    Width and height are measured in inches.
    Date completed is the date the work was completed.
    """
    MEDIUM_CHOICES = (
        (u'W', u'Watercolor'),
        (u'E', u'Etching'),
        (u'O', u'Oil'),
        (u'S', u'Sculpture'),
    )

    name = models.CharField(max_length=64, unique=True)
    medium = models.CharField(max_length=2, choices=MEDIUM_CHOICES)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    depth = models.FloatField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    raw_image = models.ImageField(upload_to='artwork/')
    price = models.IntegerField(null=True, blank=True)

    def get_roman_date(self):
        return "%s %s" % (ROMAN_MONTHS[self.date_completed.month], self.date_completed.year)

    def __unicode__(self):
        return self.name


