from django import newforms as forms

PREFBOOK = ([('xml', 'XML How to program'), ('python', 'Python How to Program'),
             ('e', 'E-business and E-commerce How to Program'),
             ('internet', 'Internet and WWW How to Program 3e'),
             ('cplusplus', 'C++ How to Program 4e'),
             ('visualbasic', 'Visual Basic How to Program'), ])
             
PREFOS = ([('xp', 'Windows XP'), ('win2000', 'Windows 2000'),
             ('me', 'Windows 95/98/ME'),
             ('linux', 'Linux'),
             ('other', 'Other'), ])
             
class ChoiceForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone')
    pref_book = forms.ChoiceField(widget=forms.Select(),choices=PREFBOOK, label='Book')
    osys = forms.ChoiceField(widget=forms.Select(),choices=PREFOS, label='Your OS')
    #created_on
