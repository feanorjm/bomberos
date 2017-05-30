from django.shortcuts import redirect, render
from bomberos.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views import View

class LoginView(View):
    form_class = LoginForm
    #initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correctamente"
                    return redirect('/admin/')
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto"

        return render(request, self.template_name, {'message': message,'form': form})

login_view = LoginView.as_view()

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/login/')

logout_view = LogoutView.as_view()
