from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm


class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # password1, потому что в параметрах формы он обозначен именно так
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('cafe:coffee_house_list')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
