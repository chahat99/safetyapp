from django.conf.urls import url
from map import views

app_name='map'

urlpatterns=[
url(r'^startjourney/$',views.startjourney,name='startjourney'),
url(r'^rate/$',views.rate,name='rate'),
url(r'^after/$',views.after,name='after'),
url(r'^feedback/$',views.feedback,name='feedback'),
url(r'^thankyou/$',views.thankyou,name='thankyou'),
]
