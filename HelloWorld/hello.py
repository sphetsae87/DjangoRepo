# Hello World Django App
#views,urls,settings,runserver

# Import statements

# for settings
from django.conf import settings
# for runserver
import sys

# settings
settings.configure(
    DEBUG = True,
    SECRET_KEY = 'thisisthesecretkey',
    ROOT_URLCONF = __name__,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

# for URL linking
from django.conf.urls import url
# Web Server Gateway Interface (WSGI)
from django.core.wsgi import get_wsgi_application
# for the view
from django.http import HttpResponse

# Creating the view
def index(request):
    return HttpResponse('Hello world')

urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
    


