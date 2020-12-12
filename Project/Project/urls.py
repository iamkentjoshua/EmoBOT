from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emobot/', include('emobot.urls', namespace='emobot')),

]
	