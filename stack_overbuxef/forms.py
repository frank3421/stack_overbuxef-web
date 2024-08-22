from django import forms
from .models import Consulta, Tag, Respuesta
from django_select2.forms import Select2MultipleWidget
from ckeditor.widgets import CKEditorWidget

#Clase formulario para la creación de una consulta
class AnswerForm(forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = ['mensaje', 'multimedia', 'anonimo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Modificar widgets para personalizar la apariencia
		self.fields['mensaje'] = forms.CharField(widget=CKEditorWidget(config_name='default'))
		self.fields['anonimo'] = forms.BooleanField(label='Publicación anónima', required=False)

#Clase formulario para la creación de una consulta
class ConsultaForm(forms.ModelForm):
	class Meta:
		model = Consulta
		fields = ['titulo', 'mensaje', 'anonimo', 'multimedia']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['tag'] = forms.ModelMultipleChoiceField(
			queryset=Tag.objects.all(),
			widget=Select2MultipleWidget,  # O puedes usar forms.SelectMultiple para un cuadro de selección múltiple
			required=False
		)

		self.fields['tag'].widget.attrs.update({'class': 'select2'})


		# Cambiar el widget del campo anonimo a un checkbox
		self.fields['anonimo'] = forms.BooleanField(label='Publicación anónima', required=False)

		self.fields['mensaje'] = forms.CharField(widget=CKEditorWidget(config_name='default'))


class TagForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['tag'] = forms.ModelMultipleChoiceField(
			queryset=Tag.objects.all(),
			widget=Select2MultipleWidget,
			required=False,
			label='Filtrar por tags',
		)

		self.fields['tag'].widget.attrs.update({'class': 'select2'})
