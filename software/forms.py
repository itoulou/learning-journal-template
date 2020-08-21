from django import forms
from create_resource.models import Language, Framework, Database, Technology

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('language',)

class FrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ('framework',)


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ('database',)


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('technology',)