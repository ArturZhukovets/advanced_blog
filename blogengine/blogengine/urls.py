from django.contrib import admin
from django.urls import path, include
from .views import redirect_to_blog

urlpatterns = [
    path('', redirect_to_blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('dictionary/', include('dictionary_app.urls')),

]
