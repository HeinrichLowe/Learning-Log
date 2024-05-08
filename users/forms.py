from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remover as dicas do Username
        self.fields['username'].help_text = None

        # Remova as dicas de senha
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None