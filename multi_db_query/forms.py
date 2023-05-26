from django import forms


class SearchForm(forms.Form):
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        self.fields["name"].required = True
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].label = "Name"
