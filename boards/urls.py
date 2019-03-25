from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home,name = "boards-home"),
    url(r'^test/$',views.test,name="test"),
    url(r'^boards/(?P<pk>\d+)/$',views.board_topics,name = "board_topics"),
    url(r'^boards/(?P<pk>\d+)/new/$',views.new_topic,name = "new_topic")
]