from django.conf.urls import url, include
from . import views

app_name = 'alarm'


article_patterns = [
    url(r'^$', view=views.landing, name='landing'),
    url(r'^clean$', view=views.clean, name='clean'),
    url(r'^add$', view=views.add, name='add')
]

urlpatterns = [url(r'^', include(article_patterns, namespace=app_name))]
