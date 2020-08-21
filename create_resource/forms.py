from django import forms
from create_resource.models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('name', 'link', 'attachment', 'attachment', 'language', 'framework', 'database', 'technology')