from django import forms

# doktor kayıt ekranı
class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label = 'Kullanıcı Adı:',
    widget = forms.TextInput(attrs = {'placeholder': 'Kullanıcı adı', 'class':'form-control'}))
    email = forms.EmailField(max_length = 50, label = 'E-mail:',
    widget = forms.EmailInput(attrs = {'placeholder': 'E-mail', 'class':'form-control'}))
    password = forms.CharField(max_length = 20, label = 'Parola:',
    widget = forms.PasswordInput(attrs = {'placeholder': 'Parola', 'class':'form-control'}))
    confirm = forms.CharField(max_length = 20, label = 'Parola Doğrula:',
    widget = forms.PasswordInput(attrs = {'placeholder': 'Parola doğrula', 'class':'form-control'}))
    
    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('Parolalar Eşleşmiyor!')
        
        values = {
            'username': username,
            'email': email,
            'password': password
        }
        return values
    
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Kullanıcı Adı:')
    password = forms.CharField(label = 'Parola:', widget = forms.PasswordInput)
    
    
    