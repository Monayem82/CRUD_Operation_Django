from django.urls import path
from . import views

urlpatterns = [
    path('insert/',views.insertFunc,name='joinTopic'),
    path('show/',views.showData,name='showJoin'),
    path('update/<id>/',views.updateDataValue),
    path('delete/<id>/',views.deleteData),
    path('gallery/',views.gallaryLink,name='gellery'),
    path('news/',views.newsLink,name='news'),
    path('deleteN/<news_id>/',views.newsDelete),
    path('updateN/<news_id>/',views.newsUpdate),

]
