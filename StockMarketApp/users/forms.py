from django.contrib.auth import forms as auth_forms, get_user_model


usermodel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta:
        model = usermodel
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)

        return self.user


class AppUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = usermodel
