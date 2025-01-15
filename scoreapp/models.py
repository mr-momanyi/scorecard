from django.db import models
from django.utils.timezone import now as timezone_now

class TreeDataEntry(models.Model):
    REGION_CHOICES = [
        ('Mau', 'Mau'),
        ('Aberdare', 'Aberdare'),
        ('Mt. Kenya', 'Mt. Kenya'),
        ('Cherangany hills', 'Cherangany hills'),
        ('Mt. Elgon', 'Mt. Elgon'),
    ]

    COUNTY_CHOICES = [
        ('Kiambu', 'Kiambu'),
        ('Murang\'a', 'Murang\'a'),
        ('Nyeri', 'Nyeri'),
        ('Mombasa', 'Mombasa'),
        ('Kwale', 'Kwale'),
        ('Kilifi', 'Kilifi'),
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Bomet', 'Bomet'),
        ('Kericho', 'Kericho'),
        ('Trans-Nzoia', 'Trans-Nzoia'),
        ('Bungoma', 'Bungoma'),
        ('Kakamega', 'Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Homa Bay', 'Homa Bay'),
        ('Kisii', 'Kisii'),
        ('Migori', 'Migori'),
        ('Meru', 'Meru'),
        ('Embu', 'Embu'),
        ('Kitui', 'Kitui'),
        ('Garissa', 'Garissa'),
        ('Wajir', 'Wajir'),
        ('Mandera', 'Mandera'),
    ]

    SUBCOUNTY_CHOICES = [
        ('Thika', 'Thika'),
        ('Ruiru', 'Ruiru'),
        ("Murang'a South", "Murang'a South"),
        ("Murang'a North", "Murang'a North"),
        ('Mombasa Town', 'Mombasa Town'),
        ('Likoni', 'Likoni'),
        ('Kinango', 'Kinango'),
        ('Lunga Lunga', 'Lunga Lunga'),
        ('Naivasha', 'Naivasha'),
        ('Nakuru', 'Nakuru'),
        ('Gilgil', 'Gilgil'),
        ('Homa Bay Town', 'Homa Bay Town'),
        ('Rachuonyo South', 'Rachuonyo South'),
    ]

    Region = models.CharField(max_length=50, choices=REGION_CHOICES, default='Mau')  # Default should match choices
    County = models.CharField(max_length=50, choices=COUNTY_CHOICES)
    Subcounty = models.CharField(max_length=50, choices=SUBCOUNTY_CHOICES)
    Field_id = models.CharField(max_length=20)
    Entry_number = models.IntegerField()
    Date_collected = models.DateField(default=timezone_now)  # Add a callable default
    Location = models.CharField(max_length=255)
    Tree_species = models.CharField(max_length=100)
    Field_size = models.FloatField()
    Trees_planted = models.IntegerField()
    tree_cover_increase = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    wildlife_habitat_conservation = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    carbon_sequestration = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    soil_health_improvement = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return f"{self.Region} - {self.County}"



# class TreeData(models.Model):
#     REGION_CHOICES = [
#         ('Mau', 'Mau'),
#         ('Aberdare', 'Aberdare'),
#         ('Mt. Kenya', 'Mt. Kenya'),
#         ('Cherangany hills', 'Cherangany hills'),
#         ('Mt. Elgon', 'Mt. Elgon'),
#     ]

#     COUNTY_CHOICES = [
#         ('Kiambu', 'Kiambu'),
#         ('Murang\'a', 'Murang\'a'),
#         ('Nyeri', 'Nyeri'),
#         ('Mombasa', 'Mombasa'),
#         ('Kwale', 'Kwale'),
#         ('Kilifi', 'Kilifi'),
#         ('Nairobi', 'Nairobi'),
#         ('Nakuru', 'Nakuru'),
#         ('Bomet', 'Bomet'),
#         ('Kericho', 'Kericho'),
#         ('Trans-Nzoia', 'Trans-Nzoia'),
#         ('Bungoma', 'Bungoma'),
#         ('Kakamega', 'Kakamega'),
#         ('Vihiga', 'Vihiga'),
#         ('Homa Bay', 'Homa Bay'),
#         ('Kisii', 'Kisii'),
#         ('Migori', 'Migori'),
#         ('Meru', 'Meru'),
#         ('Embu', 'Embu'),
#         ('Kitui', 'Kitui'),
#         ('Garissa', 'Garissa'),
#         ('Wajir', 'Wajir'),
#         ('Mandera', 'Mandera'),
#     ]

#     SUBCOUNTY_CHOICES = [
#         ('Thika', 'Thika'),
#         ('Ruiru', 'Ruiru'),
#         ("Murang'a South", "Murang'a South"),
#         ("Murang'a North", "Murang'a North"),
#         ('Mombasa Town', 'Mombasa Town'),
#         ('Likoni', 'Likoni'),
#         ('Kinango', 'Kinango'),
#         ('Lunga Lunga', 'Lunga Lunga'),
#         ('Naivasha', 'Naivasha'),
#         ('Nakuru', 'Nakuru'),
#         ('Gilgil', 'Gilgil'),
#         ('Homa Bay Town', 'Homa Bay Town'),
#         ('Rachuonyo South', 'Rachuonyo South'),
#     ]

#     Region = models.CharField(max_length=50, choices=REGION_CHOICES, default='Mau')  # Default should match choices
#     County = models.CharField(max_length=50, choices=COUNTY_CHOICES)
#     Subcounty = models.CharField(max_length=50, choices=SUBCOUNTY_CHOICES)
#     Field_id = models.CharField(max_length=20)
#     Entry_number = models.IntegerField()
#     Date_collected = models.DateField(default=timezone_now)  # Add a callable default
#     Location = models.CharField(max_length=255)
#     Tree_species = models.CharField(max_length=100)
#     Field_size = models.FloatField()
#     Trees_planted = models.IntegerField()
#     def __str__(self):
#         return f"{self.Region} - {self.County}"
