from django.db import models

# Create your models here.
class Legislator(models.Model):

    PARTIES = (
        ('R', 'Republican'),
        ('D', 'Democrat'),
        ('I', 'Independent'),
        ('G', 'Green'),
    )

    STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AS', 'American Samoa'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MH', 'Marshall Islands'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('FM', 'Micronesia'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('MP', 'Northern Marianas'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PW', 'Palau'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('VI', 'Virgin Islands'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    CHAMBERS = (
        ('H', 'House'),
        ('S', 'Senate'),
        ('O', 'Other'),
    )

    bioguide_id = models.CharField(max_length=(255))
    birthday = models.CharField(max_length=(255))
    chamber = models.CharField(choices=CHAMBERS, max_length=(255))
    contact_form = models.URLField(null=True, blank=True)
    crp_id = models.CharField(max_length=(255), null=True, blank=True)
    district = models.CharField(max_length=(255), null=True, blank=True)
    facebook_id = models.CharField(max_length=(255), null=True, blank=True)
    fax = models.CharField(max_length=(255), null=True, blank=True)
    first_name = models.CharField(max_length=(255))
    gender = models.CharField(choices=GENDERS, max_length=(255))
    govtrack_id = models.CharField(max_length=(255), blank=True, null=True)
    in_office = models.BooleanField()
    last_name = models.CharField(max_length=(255))
    leadership_role = models.CharField(max_length=(255), null=True, blank=True)
    middle_name = models.CharField(max_length=(255), blank=True, null=True)
    name_suffix = models.CharField(max_length=(255), blank=True, null=True)
    nickname = models.CharField(max_length=(255), blank=True, null=True)
    oc_email = models.EmailField(blank=True, null=True)
    ocd_id = models.CharField(max_length=(255), blank=True, null=True)
    office = models.CharField(max_length=(255), blank=True, null=True)
    party = models.CharField(choices=PARTIES, max_length=(255), blank=True)
    phone = models.CharField(max_length=(255), blank=True)
    state = models.CharField(choices=STATES, max_length=(255))
    state_name = models.CharField(max_length=(255))
    term_end = models.DateField(null=True, blank=True)
    term_start = models.DateField(null=True, blank=True)
    thomas_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=(255), blank=True, null=True)
    twitter_id = models.CharField(max_length=(255), blank=True)
    website = models.URLField(max_length=(255), null=True, blank=True)

    def full_name(self):
        return ' '.join(x for x in (self.title, self.first_name, self.middle_name, self.last_name, self.name_suffix) if x is not None)

    def __str__(self):
        return self.full_name()
