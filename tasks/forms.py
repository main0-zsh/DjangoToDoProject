from django import forms
from django.core.validators import MinLengthValidator

class UserForm(forms.Form):
    name=forms.CharField(max_length=30,min_length=2,label='Имя:',help_text='Введи своё имя.',required=True)
    password = forms.CharField(
        label='Ваш пароль:',
        help_text='Введите минимум 8 символов.',
        required=True,
        widget=forms.PasswordInput(),
        validators=[MinLengthValidator(8)]
    )
    email=forms.EmailField(label='Ваше Email:',help_text='Введите свой Email.',required=False)
    date=forms.DateField(label='Дата рождения:',help_text='Выберите дату своего рождения.',widget=forms.DateInput(attrs={'type':'date'}))
    file=forms.FileField(label='Резюме:',help_text='Загрузите ваше резюме',required=False)