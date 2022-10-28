from home.utils import get_theme
from .models import Files
from django.views.generic import DetailView


class FilesDetailView(DetailView):
    model = Files
    template_name = 'files/detail_views.html'
    context_object_name = 'file'

    def get_context_data(self, *args, **kwargs):
        context = super(FilesDetailView, self).get_context_data(*args, **kwargs)
        context['theme'] = get_theme(self.request)
        return context
