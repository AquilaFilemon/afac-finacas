from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
#Aqui eu importo o User (modelo de usuário padrão do Django, já cria o campo username, password, email...)

class formularioLogin(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Usuário ou senha incorretos'
    }

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Usuário'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )

"""
Aqui eu crio uma classe para sobrecrever um capo do AuthenticationForm
Sobrecrevo o username: 
O CharField é a lógica do campo.
O widget é a aparência/comportamento visual.
forms.CharField -> defino ele como um campo de texto do modulo forms do django
widget -> Serve para definir como o campo vai aparecer no HTML:
forms.TextInput -> Defino que esse campo será do tipo entrada de texto do modulo forms
attrs -> Defino os atributos do html nesse caso o Placeholder
"""

class CadastroForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Usuário'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirmar senha'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        #Depois que eu dou o form.is_valid lá na view o django confere tudo e guarda no cleaned_data
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já exite uma conta com esse Email')
        return email
    """
        Essa classe aparece quando eu crio um formulario que herdar o UserCRationForm
        O "Meta" é uma classe interna do django para configurar o formulário
        Digo por meio dela qual model(banco de dados eu vou usar) e quais campos devem aparecer no formulario
        model = User -> Digo a view que quando ela ela der o form.save deve salvar no model User
    """