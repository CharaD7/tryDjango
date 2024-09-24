from django import forms


SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening"),
)


class InputForm(forms.form):
    first_name = forms.CharField(maax_length=200)
    last_name = forms.CharField(maax_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()
