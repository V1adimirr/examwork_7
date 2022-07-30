from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class CreatePollView(CreateView):
    template_name = 'Poll/create_poll.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('detail_polls_view', kwargs={'pk': self.object.pk})


class UpdatePollView(UpdateView):
    model = Poll
    template_name = 'Poll/update_poll.html'
    form_class = PollForm
    context_key = 'poll'

    def get_success_url(self):
        return reverse('detail_polls_view', kwargs={'pk': self.object.pk})


class DeletePollView(DeleteView):
    template_name = 'Poll/delete_poll.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('polls_view')
