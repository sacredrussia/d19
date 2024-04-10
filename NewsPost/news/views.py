from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from datetime import datetime
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.forms import model_to_dict
import requests
from urllib3 import request

from .forms import PostForm, ResponsesForm, ResponsesForm2, NewsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Responses, News, User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class PostsList(ListView):
    model = Post
    ordering = 'time_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.username
        s = context.get('post')
        a = str(s.author)
        res_list = [Responses.objects.filter(post=self.kwargs['pk'], status='CF')]
        x, *b = res_list
        context['c'] = False
        if user == a:
            context['is_user'] = True
        if len(x) > 0:
            context['c'] = True
            context['x'] = x
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.author = User.objects.get(id=self.request.user.id)  # Or explicit model
        app_model.save()
        return super().form_valid(form)


class PostUpdate(UserPassesTestMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'post_edit'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        x = self.request.user.username
        y = self.model.objects.get(pk=self.kwargs['pk'])
        c = str(y.author)
        a = True
        b = False
        if x == c:
            return x == c
        else:
            redirect('/')


class ResponseCreate(CreateView):
    form_class = ResponsesForm
    model = Responses
    template_name = 'response_create.html'

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.author = User.objects.get(id=self.request.user.id)
        app_model.post = Post.objects.get(pk=self.kwargs['pk'])
        app_model.status = 'NW'
        app_model.save()
        send_mail(
            subject=f'Здравствуйте,{app_model.post.author}. Дата создания {app_model.time_creation}',
            message=f'Вам пришел отклик:{app_model.text}',  # сообщение с кратким описанием проблемы
            from_email='SacredRussia@yandex.ru',
            # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=[app_model.post.author.email]
            # здесь список получателей. Например, секретарь, сам врач и т. д.
        )
        return super().form_valid(form)


class ResponseUpdate(UserPassesTestMixin, UpdateView):
    form_class = ResponsesForm2
    model = Responses
    template_name = 'response_create.html'
    context_object_name = 'response_edit'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        x = self.request.user.username
        y = self.model.objects.get(id=self.kwargs['pk'])
        c = str(y.post.author)
        a = True
        b = False
        if x == c:
            return x == c
        else:
            redirect('/')

    def form_valid(self, form):
        app_model = form.save(commit=False)
        if app_model.status == 'CF':
            send_mail(
                subject=f'Здравствуйте, {app_model.author}!',
                message=f'Ваш отклик - {app_model.text}, принят',
                from_email='SacredRussia@yandex.ru',
                recipient_list=[app_model.author.email]
            )

        return super().form_valid(form)


class NewsCreate(UserPassesTestMixin, CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.author = User.objects.get(id=self.request.user.id)
        app_model.save()
        emails = []
        users_list = User.objects.all()
        for i in users_list:
            emails.append(i.email)
            print(emails)
        html_content = render_to_string(
            'news_created.html',
            {
                'app_model': app_model,
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'Вам пришла новость {app_model.title}',
            body='',
            from_email='SacredRussia@yandex.ru',
            to=emails,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super().form_valid(form)

    def test_func(self):
        x = self.request.user.is_superuser
        if x == 1:
            return x == 1
        else:
            redirect('/')


class NewsDetail(DetailView):
    model = News
    template_name = 'news_det.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.is_superuser
        if user == 1:
            context['is_user'] = True
        return context


class NewsList(ListView):
    model = News
    ordering = 'time_creation'
    template_name = 'news_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        user = self.request.user.is_superuser
        if user == 1:
            context['is_user'] = True
        return context
