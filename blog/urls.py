#blog/urls.py

from django.conf.urls import url
from . import views #tecka je aktualni adresar

urlpatterns = [ url ('^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url('^post/new$', views.post_new, name='post_new'),

]
#striska dolar je regularni vyraz, moznost jak popsat retezce
#jenom acka 'a*' nebo prazdny ' ' 'aaaa' 'aaaaaaa'
#striska zacatek retezce a konec dolr.. takze zacatek konec o sobe takze nic :)
