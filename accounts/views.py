from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token


from django.contrib.auth import get_user_model

from accounts.forms import RegisterForm, LoginForm

User = get_user_model()



def login(request):
    form  = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = authenticate(request,
                         username=form.cleaned_data['username'],
                         password=form.cleaned_data['password']
                         )
            if user is not None:
                django_login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login successful!')
                return redirect(reverse_lazy('core:home_page'))

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)



def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data = request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.add_message(request, messages.SUCCESS, 'Account created successfully!')
            return redirect(reverse_lazy('accounts:login'))


    context = {
        'form': form,
    }
    return render(request, 'register.html', context)



@login_required
def logout(request):
    django_logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logged out successfully!')
    return redirect(reverse_lazy('accounts:login'))



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect(reverse_lazy('accounts:login'))
    else:
        return render(request, 'account_activation_invalid.html')
    


