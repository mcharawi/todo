from django.conf.urls import patterns, include, url
from todolist import views
from django.contrib import admin
import os.path

admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main_page),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add-todo$', views.add_todo),
    url(r'^edit-todo/(?P<todo_id>\d+)$', views.edit_todo),
    url(r'^delete-todo/(?P<todo_id>\d+)$', views.delete_todo),
]