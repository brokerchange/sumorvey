from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_random, name='question_random'),
    url(r'^questions/$', views.question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
]
