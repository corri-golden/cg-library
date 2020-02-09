from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_user(request):  #method that redirects home once logout 
    logout(request)
    return redirect(reverse('libraryapp:home'))