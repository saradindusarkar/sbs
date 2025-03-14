from django import forms
from dlog.models import Dlog

class DlogForm(forms.ModelForm):
    class Meta:
        model = Dlog
        exclude = ['log_date']  # Exclude the log_date field


