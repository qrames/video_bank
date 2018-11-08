"""video_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


# Create :
from bank.views import AddMovie, CreateCustomerViews
# Read :
from bank.views import DetailMovie
from bank.views import ListMovies, ListRentedMovies
# Update :
from bank.views import UpdateMovie
# Delete :
from bank.views import DeleteMovie



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customers/', include('userena.urls'), name="user"),



#CRUD Movie :
    url(r'^movie/add/$', AddMovie.as_view(), name="add-movie"),
    url(r'^movie/(?P<slug>[-\w]+)/$', DetailMovie.as_view(), name="detail-movie"),

    url(r'^$', ListMovies.as_view(), name="movies"),
    url(r'^movies/list/$', ListRentedMovies.as_view(), name="admin-movies"),

    url(r'^movie/(?P<slug>[-\w]+)/Update/$', UpdateMovie.as_view(), name="update-movie"),
    url(r'^movie/(?P<slug>[-\w]+)/delete/$', DeleteMovie.as_view(), name="delete-movie"),


    url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(next_page='/'),
        name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
