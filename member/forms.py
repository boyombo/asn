from django import forms

from member.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email']
