from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product

wrong_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево",
    "бесплатно", "обман", "полиция","радар"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название товара'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание товара'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену'})


    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for wrong_word in wrong_words:

            if wrong_word in name.lower() :
                self.add_error('name', f"Наименование товара не может содержать слово {wrong_word}")

            if wrong_word in description.lower():
                self.add_error('description', f"Описание товара не может содержать слово {wrong_word}")
