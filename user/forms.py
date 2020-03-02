from django import forms

STATES = (
    ('','State'),
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AR', 'AR'),	
    ('AZ', 'AZ'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DC', 'DC'),
    ('DE', 'DE'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('IA', 'IA'),	
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('MA', 'MA'),
    ('MD', 'MD'),
    ('ME', 'ME'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MO', 'MO'),	
    ('MS', 'MS'),
    ('MT', 'MT'),
    ('NC', 'NC'),	
    ('NE', 'NE'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),			
    ('NV', 'NV'),
    ('NY', 'NY'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WI', 'WI'),	
    ('WV', 'WV'),
    ('WY', 'WY')
)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    retype_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())
    firstName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=150)
    address_1 = forms.CharField(widget=forms.TextInput())
    address_2 = forms.CharField(widget=forms.TextInput(), required=False)
    city = forms.CharField(widget=forms.TextInput())
    state = forms.ChoiceField(choices=STATES)
    zipcode = forms.CharField(widget=forms.TextInput())