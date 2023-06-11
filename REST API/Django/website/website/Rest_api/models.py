from django.db import models

class Cafes(models.Model):
    
    name = models.CharField(max_length = 100)
    map_url = models.CharField(max_length = 100)
    img_url = models.URLField(null = True, blank = True)
    location = models.URLField()
    has_sockets = models.BooleanField()
    has_toilet = models.BooleanField()
    has_wifi = models.BooleanField()
    can_take_calls = models.BooleanField()
    seats = models.CharField(max_length = 100)
    coffee_price = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        managed = False
        db_table = 'cafe'
