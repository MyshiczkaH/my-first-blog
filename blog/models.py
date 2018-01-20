from django.db import models
from django.utils import  timezone
# Create your models here.

class Post(models.Model):
    #prispevky jak se chovaji v blogu - maji nadpis a obsah
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    #cascade - smazeme autora smazou se vsechny jeho prispevky
    title = models.CharField(max_length=200)
    #titulek muze byt dlouhy max tolik znaku
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #kdy to byo napsane, timezone vraci aktualni datum a casu
    published_date = models.DateTimeField(blank=True, null=True)
    #kdy byl napsan vs kdy byl publikován, null tue jeste nebyl publikovan nemel by se ukazat
#vytvaret mazat publikovat chceme
    def publish(self):
        #self objekt na kterem zrovna pracuji
        self.published_date = timezone.now()
        self.save()#save dedime z modelu, kazdy model ma save

    def __str__(self):
        return self.title
