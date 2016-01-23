from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'db_trial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('polls.urls')),
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', admin.site.urls)


]