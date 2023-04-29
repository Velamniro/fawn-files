from django.shortcuts import render, redirect
from django.views.generic import ListView

from files.forms import AddFileForm
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
        context['type'] = self.request.GET.get("type")
        context['version'] = self.request.GET.get("version")

        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.method == "GET" and self.request.GET:
            type = self.request.GET.get("type")
            version = self.request.GET.get("version")
            if type != 'none' and version != 'none':
                return Files.objects.filter(type=type, version=version).order_by('-datetime').prefetch_related('version').select_related('type')
            elif type != 'none':
                return Files.objects.filter(type=type).order_by('-datetime').prefetch_related('version').select_related('type')
            elif version != 'none':
                return Files.objects.filter(version=version).order_by('-datetime').prefetch_related('version').select_related('type')
        return Files.objects.order_by('-datetime').prefetch_related('version').select_related('type')


def addfile(request):
    theme = get_theme(request)
    if theme is None:
        return redirect('change_theme', theme='light')
    else:
        local_themes = themes.copy()
        local_themes.pop(theme)
    if request.method == "POST":
        form = AddFileForm(request.POST)

        if form.is_valid():
            try:
                file = form.save(commit=False)
                file.slug = slugify(form.cleaned_data['title'])
                if file.slug == '':
                    return redirect('home')
                file.creator = request.user
                file.save()
                form.save_m2m()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления файла')
    else:
        form = AddFileForm()
    return render(request, 'home/addfile.html', {'form': form, 'theme': get_theme(request), 'themes': local_themes})


def change_theme(request, theme):
    response = render(request, "redirect_to_home.html")
    set_cookie(response, 'fawn-files_cookie_theme', theme, 365)
    return response
