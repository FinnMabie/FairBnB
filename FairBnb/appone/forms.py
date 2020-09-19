from django import forms


class SearchForm(forms.Form):
    search_box = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control mr-sm-2"}))


class SaveHomeForm(forms.Form):
    address = forms.CharField(max_length=100)
    zip_code = forms.IntegerField()
