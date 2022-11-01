from home.utils import *
from .models import Files
from django.views.generic import DetailView


class FilesDetailView(DataMixin, DetailView):
    model = Files
    template_name = 'files/detail_views.html'
    context_object_name = 'file'

    def get_context_data(self, **kwargs):
        context = super(FilesDetailView, self).get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
