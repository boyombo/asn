from django import forms

from member.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email']

    def clean_email(self):
        if 'email' in self.cleaned_data:
            try:
                Member.objects.get(email=self.cleaned_data['email'])
            except Member.DoesNotExist:
                return self.cleaned_data['email']
            else:
                raise forms.ValidationError(
                    'This email has been registered already')
