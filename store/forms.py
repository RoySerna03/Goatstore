from django import forms
from store.models import Product, UserProfile, MoneyRequest




class addproductform(forms.ModelForm):
 

	class Meta:
		model = Product
		fields = ('product_name', 'product_cost', 'product_description', 'product_image' )

class addbalanceform(forms.ModelForm):
 

	class Meta:
		model = UserProfile
		fields = ('balance',)


class moneyrequestform(forms.ModelForm):
 

	class Meta:
		model = MoneyRequest
		fields = ('money_amount',)


