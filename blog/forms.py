from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter Todo delete",
            "aria-label": "Todo",
            "aria_describedby": "add-btn"
        }
    ))
