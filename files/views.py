from django.shortcuts import get_object_or_404

from home.utils import *
from .models import Files
from django.views.generic import DetailView


class FilesDetailView(DataMixin, DetailView):
    model = Files
    template_name = 'files/detail_views.html'
    context_object_name = 'file'

    def get_context_data(self, **kwargs):
        context = super(FilesDetailView, self).get_context_data(**kwargs)

        context['fav'] = 'far'
        file = self.get_object()
        if file.favourite.filter(id=self.request.user.id).exists():
            context['fav'] = 'fas'

        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        slug = self.kwargs.get('slug', '')
        q = super().get_queryset()
        return q.filter(slug=slug).select_related('version').select_related('type')
