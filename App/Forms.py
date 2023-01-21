from django import forms

from .models import product

class productform(forms.ModelForm):
    title   =forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(attrs={
                                                'placeholder':'Your description',
                                                'class':'new-class-name two',
                                                'id':'my-id-for-textarea',
                                                'rows':20,
                                                'cols':60
                        })
    )
    price   = forms.DecimalField(initial=19.9)
    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    def clean_title(self,*arg,**kwargs):
        title=self.cleaned_data.get('title')
        if 'CFE' in title:
            return title
        else:
            raise forms.ValidationError('This is not a valid title')

class RawProductForm(forms.Form):
    title   =  forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(attrs={
                                                'placeholder':'Your description',
                                                'class':'new-class-name two',
                                                'id':'my-id-for-textarea',
                                                'rows':20,
                                                'cols':60
                        })
    )
    price   = forms.DecimalField()