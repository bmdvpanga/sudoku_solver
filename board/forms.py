from django import forms
from collections import defaultdict

class BoardForm(forms.Form):
    
    # board_form = defaultdict(0)
    num = forms.CharField()
    # for i in range(9):
    #     for j in range(9):
    #         board_form[i][j] 

    # pass