from django import forms
from .models import Port
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class IndexForm(forms.Form):
    in_port = forms.ModelChoiceField(label='Порт погрузки', queryset=Port.objects.all())
    out_port = forms.ModelChoiceField(label='Порт выгрузки', queryset=Port.objects.all())
    eqp_len = forms.DecimalField(label='Длина', max_digits=5, decimal_places=2)
    eqp_width = forms.DecimalField(label='Ширина', max_digits=5, decimal_places=2)
    eqp_height = forms.DecimalField(label='Высота', max_digits=5, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('in_port', css_class='form-group col-md-6 mb-0'),
                Column('out_port', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('eqp_len', css_class='form-group col-md-6 mb-0'),
                Column('eqp_width', css_class='form-group col-md-6 mb-0'),
                Column('eqp_height', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign in')
        )

