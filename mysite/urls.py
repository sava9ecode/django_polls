import os

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from polls import views

from dotenv import load_dotenv


load_dotenv()

urlpatterns = [
    path("", RedirectView.as_view(url="polls/", permanent=True)),
    path("polls/", include("polls.urls")),
    path(f"{os.getenv('ADMIN_SECRET_KEY', default='')}admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register_request, name="register"),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
