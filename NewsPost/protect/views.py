from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from news.models import Responses, Post
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from news.models import User


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.id
        resp_list = [Responses.objects.filter(status='NW')]
        resp_list1 = [Responses.objects.filter()]
        post_list = [Post.objects.filter(author=user)]
        x, *b = post_list
        c, *a = resp_list
        h, *j = resp_list1
        context['nw'] = 'NW'
        context['dl'] = 'DL'
        context['test'] = False
        if len(x) > 0:
            context['test'] = True
            context['posts'] = x
            context['res'] = c
            context['res1'] = h
        return context


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'users/invalid_code.html')
        return redirect('/')