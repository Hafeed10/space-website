

from django.urls import path
from web.views import index

app_name = 'space1'

urlpatterns = [
    
    path("",index , name="web")
]
