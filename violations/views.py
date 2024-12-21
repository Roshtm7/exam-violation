from django.shortcuts import render,redirect
from violations.forms import ViolationForm
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm

class ViolationView(View):
    template_name="register.html"
    form_class=ViolationForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
            print("form created")
            return redirect("register")
        print("failed")
        return redirect(request,self.template_name,{"form":form_instance})

class LoginView(View):
    template_name = "login.html" 

    def get(self, request, *args, **kwargs):
        form_instance = AuthenticationForm() 
        return render(request, self.template_name, {"form": form_instance})

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        form_instance = AuthenticationForm(data=form_data)
        if form_instance.is_valid():
            username = form_instance.cleaned_data.get("username")
            password = form_instance.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully")
                return redirect("home") 
            else:
                print("Invalid credentials")
        return render(request, self.template_name, {"form": form_instance})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        print("User logged out")
        return redirect("login")







