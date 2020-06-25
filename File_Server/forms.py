from django import forms


class Upload_Form(forms.Form):
    uploaded_file = forms.FileField(label="upload your file here", 
        required=True ,
        widget=forms.FileInput(attrs={'class': 'form-control-file-sm' , 'id':'form_input'})
    )
