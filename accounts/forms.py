from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()



class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username'
                })
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password'
                })
    )






class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirm Password'
                })
    )

    class Meta:
        model = User        
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last Name'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Userame'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password'
                }
            ),
        }




    def save(self, commit):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user
    
    

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data['username']).exists()
        if not user:
            password = self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match')
        else:
            raise forms.ValidationError('Username already exists')










