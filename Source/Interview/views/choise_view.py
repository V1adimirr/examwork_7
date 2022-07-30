from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse, get_object_or_404
from Interview.forms import ChoiceForm
from Interview.models import Choice, Poll


class DetailChoiceView(DetailView):
    template_name = "Choice/detail_choice_view.html"
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Polls'] = self.object.For_polls.all()
        return context


class CreateChoiceView(CreateView):
    template_name = 'Choice/create_choice.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        interview = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.interview = interview
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_polls_view', kwargs={'pk': self.object.interview.pk})


class UpdateChoiceView(UpdateView):
    form_class = ChoiceForm
    template_name = "Choice/update_choice.html"
    model = Choice

    def get_success_url(self):
        return reverse("detail_polls_view", kwargs={"pk": self.object.interview.pk})


class DeleteChoice(DeleteView):
    template_name = "Choice/delete_choice.html"
    model = Choice

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("detail_polls_view", kwargs={"pk": self.object.interview.pk})
