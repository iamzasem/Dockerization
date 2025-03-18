from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from home.views import german_view, grammarlevels, a1Topics, otherTopics # Import german_view from home.views

admin.site.site_header = "Zasem Admin"
admin.site.site_title = "Zasem Admin Portal"
admin.site.index_title = "Welcome to Zasem Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('myadmin/', include(('home.urls', 'home'), namespace='home')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('german.html', german_view, name='german'),  # Now uses imported german_view
    path('grammar-levels.html', grammarlevels, name='grammar-levels'), 
    path('a1-topics.html', a1Topics, name='a1-topics'), 
    path('other-topics.html', otherTopics, name='otherTopics'), 
     
      ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)