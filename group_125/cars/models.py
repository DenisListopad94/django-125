from django.db import models

class Company(models.Model):
    compony = models.TextField(verbose_name='компания',null = True)
    year_budjet = models.IntegerField(verbose_name='годовой доход',null = True)
    def __str__(self):
        return self.compony

class Car(models.Model):
    title = models.CharField(max_length=40,verbose_name='машины') # название машинок
    content = models.TextField(verbose_name='описание')
    costs = models.IntegerField(verbose_name='стоимость')
    create = models.IntegerField(default=2010,verbose_name='дата выпуска')
    company = models.ForeignKey('Company',on_delete=models.CASCADE,null=True)


    class Meta():
        verbose_name = 'Мaшины'
        verbose_name_plural = 'машины'

    def __str__(self):
        return self.title


