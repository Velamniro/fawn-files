from django.shortcuts import get_object_or_404, render

from home.utils import *
from .forms import CommentForm
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
        context['comment_form'] = CommentForm()
        context['comments'] = self.get_object().comments.select_related('user').all()

        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        slug = self.kwargs.get('slug', '')
        return super().get_queryset().filter(slug=slug).prefetch_related('version').select_related('type')

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.file = self.get_object()
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
            return redirect('file-detail', slug=self.get_object().slug)
