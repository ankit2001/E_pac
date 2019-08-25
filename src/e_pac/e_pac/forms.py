from django import forms
class ContactForm(forms.Form):
	fullname=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"your full name"}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form_control","placeholder":"your email "}))
	content=forms.CharField(widget=forms.Textarea(attrs={"class":"form_control","placeholder":"your content"}))
    def clean_email(self):
    	email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
        	raise forms.ValidationError("email has to gmail.com")
        return email