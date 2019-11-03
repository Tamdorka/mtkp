from django.contrib.auth.models import User
from main.models import Student

from django.contrib.auth import authenticate, login
from django import forms

# Create your forms here.

class CreateStudentForm(forms.Form):
    username = forms.CharField(
        label = 'Никнейм',
        min_length = 4,
        strip = True,
        required = True,
    )
    code = forms.CharField(
        label = 'Код для регистрации',
        min_length = 5,
        strip = True,
        required = True,
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput,
        label = 'Пароль',
        min_length = 8,
        required = True,
        
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput,
        label = 'Подтверждение пароля',
        min_length = 8,
        required = True
    )

    error_list = []

    def save(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        if password1 == password2:
            if len(User.objects.filter(username=username)) == 0:
                user = User(username=username)
                user.set_password(password1)
                user.save()
                
                student = Student(
                    user = user,
                    code = self.cleaned_data.get('code')
                )
                student.save()
                return student
        
        self.error_list.append('Пароли не совпадают')
        return None

class LoginUserForm(forms.Form):
    name_email_phone = forms.CharField(
        label = 'Никнейм, почта или номер телефона',
        min_length = 4,
        required = True
    )
    password = forms.CharField(
        widget = forms.PasswordInput,
        label = 'Пароль',
        min_length = 8,
        required = True
    )
    
    error_list = []
    
    def get_user(self):
        type = None
        string = self.cleaned_data.get('name_email_phone')
        
        # Check email
        query = User.objects.filter(email = string)
        if len(query) > 0:
            return query[0]
        
        # Check name
        query = User.objects.filter(username = string)
        if len(query) > 0:
            return query[0]

        # If None - assume that phone
        query = Student.objects.filter(phone = string)
        if len(query) > 0:
            return query[0].user
        
        return None
    
    def user_login(self, request):
        user = self.get_user()
        if user is not None:
            if user.check_password(self.cleaned_data.get('password')):
                login(request, user)
                return True

        self.error_list.append('Неверный логин или пароль, проверьте правильность ввода данных')
        return False