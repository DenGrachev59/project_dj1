from django import forms

from main.models import Student


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_active":
                field.widget.attrs['class'] = 'form-control'

class StudentForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'avatar', 'is_active', 'email',)
        # fields = '__all__',
        # exclude  = ( 'is_active',)






    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('Почта должна относиться к домену sky.pro')

        return cleaned_data



