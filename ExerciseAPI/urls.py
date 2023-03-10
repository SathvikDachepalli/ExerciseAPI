from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from Exercise.views import ExerciseView
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header="Exercise API"
admin.site.site_title="Exercise page"
admin.site.index_title="Welcome Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Exercise.urls')),
    path("apitoken",obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

