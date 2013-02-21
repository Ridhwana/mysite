# This also imports the include function
#allowed the removal of poll specific apps, by adding a url file in the application 'poll'
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')), #reference the specific app 'poll', include references another URLconf
    url(r'^admin/', include(admin.site.urls)),
)