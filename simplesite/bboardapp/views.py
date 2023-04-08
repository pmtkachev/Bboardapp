from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bb, Rubric
from .forms import BbForm


class BbCreateView(CreateView):
    template_name = 'bboardapp/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class MainPage(TemplateView):
    template_name = 'bboardapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['bbs'] = Bb.objects.all()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbByRubView(TemplateView):
    template_name = 'bboardapp/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        return context


class BbDetailView(DetailView):
    model = Bb
    template_name = 'bboardapp/bb_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    template_name = 'bboardapp/update.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDelete(DeleteView):
    model = Bb
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        return context
