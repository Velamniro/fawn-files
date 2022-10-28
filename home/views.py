from django.shortcuts import render
from files.models import Files
from .utils import get_theme, set_cookie


def home(request):
    file_type = "none"
    version = "none"
    if request.method == "GET" and request.GET:
        file_type = request.GET.get("type")
        version = request.GET.get("version")

    theme = get_theme(request)

    files = Files.objects.order_by('-datetime')
    response = render(request, 'home/index.html', {'files': files, "version": version, "type": file_type, 'theme': theme})
    if theme is None:
        theme = 'light'
        set_cookie(response, 'fawn-files_cookie_theme', theme, 365 * 360 * 24)
    return response


def about(request):
    return render(request, 'home/about.html', {'theme': get_theme(request)})


def faq(request):
    return render(request, 'home/faq.html', {'theme': get_theme(request)})


def change_theme(request):
    now_theme = get_theme(request)
    if now_theme == 'light':
        new_theme = 'dark'
    else:
        new_theme = 'light'
    response = render(request, "redirect_to_home.html")
    set_cookie(response, 'fawn-files_cookie_theme', new_theme, 365)
    return response
