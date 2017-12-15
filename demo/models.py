from django.db import models

# Create your models here.


class PhoneBrand(models.Model):
    type_list=[('0','Smart Phone'),('1','Home Phone'),('2','Cell Phone')]
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=2,choices=type_list)
    value=models.CharField(max_length=10)
    location=models.CharField(max_length=200)
    foundation_year=models.CharField(max_length=4)

    def __str__(self):
        return str(self.id)+' '+self.name

    def type_name(self):
        return dict(self.type_list)[self.type]


class PhoneModel(models.Model):
    color_list=[('0','White'),('1','Black'),('2','Grey'),('3','Blue')]
    type_list=[('0','Super Amoled'),('1','IPS LCD'),('2','Amoled')]
    brand=models.ForeignKey(PhoneBrand,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    color=models.CharField(max_length=2,choices=color_list)
    screen_size=models.CharField(max_length=20)
    screen_type=models.CharField(max_length=2,choices=type_list)
    camera=models.CharField(max_length=5)
    battery_capacity=models.CharField(max_length=5)
    memory=models.CharField(max_length=5)
    storage=models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)+' '+self.name

    def color_name(self):
        return dict(self.color_list)[self.color]

    def type_name(self):
        return dict(self.type_list)[self.screen_type]
