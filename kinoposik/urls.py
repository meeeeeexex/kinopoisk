"""kinoposik URL Configuration
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('kinopoisk_app.urls.User')),
    path('api/', include('kinopoisk_app.urls.Movie')),
    path('api/', include('kinopoisk_app.urls.Cinema')),
    path('api/', include('kinopoisk_app.urls.Actor')),
    path('api/', include('kinopoisk_app.urls.Director')),
    path('api/', include('kinopoisk_app.urls.Review')),
    path('api/', include('kinopoisk_app.urls.Review')),

    # AUTH
    path('api/auth/', include('rest_framework.urls')),
    path('', include('accounts.urls')),

]
