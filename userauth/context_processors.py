from django.conf import settings


def site_variable(request):
    return {
        'SITE_URL': settings.SITE_URL,
    }
