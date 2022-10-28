import datetime

from django.conf import settings


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        return context


def set_cookie(response, key, value, days_expire=365):
    max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )
    return response


def get_theme(request):
    return request.COOKIES.get('fawn-files_cookie_theme')
