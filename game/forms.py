from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from game.models import Page, Category, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)
    
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Game.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the Game.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    picture = forms.ImageField(help_text="Please upload a picture about this game.", required=False)
    rate = forms.CharField(max_length=128, help_text="Please enter the rate of this Game.", required=False)

    class Meta:
        model = Page
        exclude = ('category','image')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://') and not url.startswith('https://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {'website', 'picture',}

class ChangePassword(forms.ModelForm):
    oldpassword = forms.CharField(label='oldpassword', max_length=30, widget=forms.PasswordInput(attrs={'size':20}))
    newpassword = forms.CharField(label='newpassword', max_length=30, widget=forms.PasswordInput(attrs={'size':20}))
    reppassword = forms.CharField(label='reppassword', max_length=30, widget=forms.PasswordInput(attrs={'size':20}))