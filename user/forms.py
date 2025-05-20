from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25, label="Kullanıcı Adı")
    password = forms.CharField(max_length=25, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=25, label="Parola(Tekrar)", widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parola Uyuşmuyor.")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label="Kullanıcı Adı")
    password = forms.CharField(max_length=25, label="Parola", widget=forms.PasswordInput)