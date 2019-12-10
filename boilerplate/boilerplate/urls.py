from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',          admin.site.urls),
    path('',                include('helloworld.urls')),
    path('staticpage/',     include('i_boilerplate_staticpage.urls')),
    path('dataxfertohtml/', include('ii_boilerplate_dataxfertohtml.urls')),
    path('weather/',        include('iii_boilerplate_getjson_weather.urls')),
    path('model/',          include('iv_model.urls')),
    path('modelforms/',     include('v_modelforms.urls'))

]
