import datetime

from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import redirect
from django.template.defaulttags import register

themes = {
    'light': 'fa-sun',
    'dark': 'fa-moon',
    'super_dark': 'fa-moon-stars',
}


class DataMixin:
    request: HttpRequest

    def get_user_context(self, **kwargs):
        context = kwargs
        context['theme'] = get_theme(self.request)
        if context['theme']:
            local_themes = themes.copy()
            local_themes.pop(context['theme'])
            context['themes'] = local_themes
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


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

