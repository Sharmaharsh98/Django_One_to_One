from django import forms
from .models import Ceo, Company

class InfoForm(forms.ModelForm):

    class Meta:
        model = Ceo
        fields = '__all__'

        labels = {
            'full_name' : 'Full Name',
            'age' : 'Age',
            'gender' : 'Gender',
            'salary' : 'Salary',
            'city' : 'City'
        }

        gender = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))

        widgets = {
            'full_name' : forms.TextInput(),
            'age' : forms.NumberInput(),
            'gender' : forms.RadioSelect(choices= gender),
            'salary' : forms.TextInput(),
            'city' : forms.TextInput()
        }

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

        labals = {
            'company_name' : 'Company Name',
            'company_domain' : 'Company Domain',
            'company_revenue' : 'Company Revenue',
            'company_headoffice' : 'Company Headoffice'
        }