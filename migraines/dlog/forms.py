from django import forms 
from . import models 


class CreateUser(forms.ModelForm): 
    # Now, add custom widgets inside the form class (outside Meta)
    user_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password' })
    )

    class Meta: 
        model = models.user_login
        fields = ['user_email', 'user_password']  # Keep the model fields as they are



class LoginForm(forms.Form):
    user_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    


#class Create_migraines_log(forms.ModelForm): 
#    class Meta: 
#        model = models.migraines_log
#        fields = ['user_email','log_date'] 



class Create_migraines_log(forms.ModelForm): 
    class Meta: 
        model = models.migraines_log
        fields = ['log_date']

    log_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))