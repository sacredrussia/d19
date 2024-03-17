from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
import random
from string import hexdigits
from django.core.mail import send_mail


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        send_mail(
            subject=f'Код активации',
            message=f'Код активации аккаунта: {code}',
            from_email='SacredRussia@yandex.ru',
            recipient_list=[user.email]

        )
        return user
