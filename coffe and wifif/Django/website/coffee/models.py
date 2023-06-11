from django.db import models

class CafeData(models.Model):
    
    coffee_rating = [(''.join(['☕️' for _ in range(b)]), ''.join(['☕️' for _ in range(b)])) for b in range(1, 6) ]
    wifi_rating = [(''.join(['💪' for _ in range(b)]), ''.join(['💪' for _ in range(b)])) for b in range(1, 6) ]
    power_rating = [(''.join(['🔌' for _ in range(b)]), ''.join(['🔌' for _ in range(b)])) for b in range(1, 6) ]
    
    name = models.CharField(max_length = 100, unique = True)
    location = models.URLField()
    opens = models.TimeField()
    closes = models.TimeField()
    coffee = models.CharField(max_length = 10, choices = coffee_rating, default = '✘')
    wifi = models.CharField(max_length = 10, choices = wifi_rating, default = '✘')
    power = models.CharField(max_length = 10, choices = power_rating, default = '✘')
    
    def __str__(self):
        return self.name