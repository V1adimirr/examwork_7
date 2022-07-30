from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from Interview.forms import PollForm
from Interview.models import Poll


class IndexPollView(ListView):
    template_name = 'Poll/polls_view.html'
    context_object_name = 'polls'
    ordering = ('-created_at',)
    paginate_by = 4

    def get_queryset(self):
        return Poll.objects.all()


class DetailPollView(DetailView):
    template_name = "Poll/detail_polls_view.html"
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Polls'] = self.object.For_polls.all()
        return context
