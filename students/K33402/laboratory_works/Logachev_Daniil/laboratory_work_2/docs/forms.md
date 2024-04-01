```python
from .models import Gamer, Comment, University
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


# Определяем форму для регистрации пользователей с дополнительным полем электронной почты
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


# Определяем форму для регистрации игроков с полями для описания и опыта
class GamerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Gamer
        fields = ['description', 'experience']


# Определяем форму для комментариев пользователей с полями для типа комментария, рейтинга и текста
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_type", "rating", "text"]
        widgets = {
            'comment_type': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


# Определяем форму для участия игрока в соревновании
class GameEntryForm(forms.Form):
    gamer = forms.ModelChoiceField(queryset=Gamer.objects.all(), empty_label=None)



# Определяем форму для обновления профиля пользователя с полями для университета, описания и опыта
class ProfileUpdateForm(UserChangeForm):
    team_choices = [(r.id, r.name) for r in Team.objects.all()]
    team = forms.ChoiceField(choices=[("", "Выберите команду")] + team_choices,
                             widget=forms.Select(attrs={'class': 'form-control'}), required=False, label="Команда")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False,
                                  label="Описание")
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}), required=False,
                                    label="Опыт")
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}), required=False,
        label="Текущий пароль")
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}), required=False,
        label="Новый пароль")
    new_password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}), required=False,
        label="Подтвердите новый пароль")class ProfileUpdateForm(UserChangeForm):
    university = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}), required=False, label="Университет")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label="Описание")
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}), required=False, label="Опыт")
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}), required=False, label="Текущий пароль")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}), required=False, label="Новый пароль")
    new_password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}), required=False, label="Подтвердите новый пароль")


    class Meta:
        model = User
        fields = ('username', 'email', 'university', 'description', 'experience')


    # Инициализируем поля формы текущими данными пользователя
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            try:
                gamer = instance.gamer
                if gamer:
                    if gamer.university:
                        self.fields['university'].initial = gamer.university.id
                    self.fields['description'].initial = gamer.description
                    self.fields['experience'].initial = gamer.experience
            except Gamer.DoesNotExist:
                pass

    # Проверяем корректность данных формы для изменения пароля
    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        new_password_confirm = cleaned_data.get('new_password_confirm')

        if new_password or new_password_confirm:
            if not current_password:
                raise forms.ValidationError("To change the password, please provide the current password.")

            user = self.instance
            if not user.check_password(current_password):
                raise forms.ValidationError("The current password you provided is incorrect.")

            if new_password != new_password_confirm:
                raise forms.ValidationError("The new passwords do not match.")
        return cleaned_data


# Определяем кастомную форму для изменения пароля с форматированными полями ввода пароля
class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}),
        label="Текущий пароль")
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        label="Новый пароль")
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        label="Подтвердите новый пароль")

```