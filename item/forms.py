from django import forms
from .models import Item

# Define common classes for styling
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
CHECKBOX_CLASSES = 'border'
SELECT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('Category', 'name', 'location', 'description', 'price', 'image', 'is_available', 'is_negotiable')

        widgets = {
        'Category': forms.Select(attrs={'class': SELECT_CLASSES}),
        'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter item name'}),
        'location': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter location'}),
        'description': forms.Textarea(attrs={'class': f'{INPUT_CLASSES} resize-none', 'placeholder': 'Enter post description'}),  
        'price': forms.TextInput(attrs={'class': f'{INPUT_CLASSES} text-green-500', 'placeholder': 'Enter price'}),
        'image': forms.ClearableFileInput(attrs={'class': f'{INPUT_CLASSES} bg-blue-500 text-white'}),
        'is_available': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASSES}),
        'is_negotiable': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASSES}),
    }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'location', 'description', 'price', 'image', 'is_available', 'is_negotiable')

        widgets = {
        'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter item name'}),
        'location': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter location'}),
        'description': forms.Textarea(attrs={'class': f'{INPUT_CLASSES} resize-none', 'placeholder': 'Enter post description'}),  
        'price': forms.TextInput(attrs={'class': f'{INPUT_CLASSES} text-green-500', 'placeholder': 'Enter price'}),
        'image': forms.ClearableFileInput(attrs={'class': f'{INPUT_CLASSES} bg-blue-500 text-white'}),
        'is_available': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASSES}),
        'is_negotiable': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASSES}),
    }