from django.db import models
from legislators.models import Legislator

# Create your models here.
class Bill(models.Model):
    BILL_TYPES = (
            ('hr', 'House of Representatives'),
            ('hres', 'House Resolution'),
            ('hjres', 'House Joint Resolution'),
            ('hconres', 'House Concurrent Resolution'),
            ('s', 'Senate'),
            ('sres', 'Senate Resolution'),
            ('sjres', 'Senate Joint Resolution'),
            ('sconres', 'Senate Concurrent Resolution'),
        )

    CHAMBERS = (
            ('house', 'House of Representatives'),
            ('senate', 'Senate'),
            ('other', 'Other'),
        )

    bill_id = models.CharField(max_length=(255))
    bill_type = models.CharField(max_length=(255), choices=BILL_TYPES)
    chamber = models.CharField(max_length=(255), choices=CHAMBERS)
    congress = models.IntegerField()
    cosponsors_count = models.IntegerField()
    enacted_as = models.CharField(max_length=(255), null=True, blank=True)
    introduced_on = models.DateField()
    last_action_at = models.DateField()
    last_version_on = models.DateField()
    last_vote_at = models.DateField(null=True, blank=True)
    number = models.IntegerField()
    official_title = models.TextField()
    popular_title = models.CharField(max_length=(255), null=True, blank=True)
    short_title = models.CharField(max_length=(255), null=True, blank=True)
    sponsor = models.ForeignKey(Legislator)

    def __str__(self):
        if self.popular_title:
            return self.popular_title
        elif self.short_title:
            return self.short_title
        return self.official_title
