from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from files.models import Files
from .utils import *

themes = {
    'light': 'fa-sun',
    'dark': 'fa-moon',
    'super_dark': 'fa-moon-stars',
}


class Home(DataMixin, ListView):
    model = Files
    template_name = 'home/index.html'
    context_object_name = 'files'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['type'] = "none"
        context['version'] = "none"
        if self.request.method == "GET" and self.request.GET:
            context['type'] = self.request.GET.get("type")
            context['version'] = self.request.GET.get("version")

        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    local_themes = themes.copy()
    local_themes.pop(get_theme(request))
    return render(request, 'home/about.html', {'theme': get_theme(request), 'themes': local_themes})


def faq(request):
    local_themes = themes.copy()
    local_themes.pop(get_theme(request))
    return render(request, 'home/faq.html', {'theme': get_theme(request), 'themes': local_themes})


def change_theme(request, theme):
    response = render(request, "redirect_to_home.html")
    set_cookie(response, 'fawn-files_cookie_theme', theme, 365)
    return response
