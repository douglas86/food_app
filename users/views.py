from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """TODO: Docstring for register.

    :request: TODO
    :returns: TODO

    """
    form = UserCreationForm()

    return render(request, 'user/register.html', {'form':form})
