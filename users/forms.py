from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove username tips.
        self.fields['username'].help_text = None

        # Remove password tips.
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None