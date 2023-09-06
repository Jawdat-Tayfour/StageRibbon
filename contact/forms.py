from django import forms


class ContactForm(forms.Form):
    name= forms.CharField(max_length=255, required=True,label="",
                          widget=forms.TextInput(attrs={
                              "placeholder":"Enter Your Name."
                          }))
    
    email = forms.EmailField(required=True,label="",
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Enter Your Email Correctly So We Can Get Back To You.',
                                   'class': 'form-control'}))
    
    content = forms.CharField(label="",
                              widget=forms.Textarea(attrs={
                                  "placeholder":"Enter Your Message To The Team Here."
                                  ,'class': 'form-control'}))
    '''
    help_text=
    help_text="Write Your Message To The Team Here
    help_text="Write Your Email Here (make sure it's correct to we can get back to you)"
    '''