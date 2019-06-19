from django.shortcuts import render
from django.http import Http404
from apps.authentication.babysitters.models import Babysitter
from apps.navigation.search.forms import SearchForm


def home(request):
    user = None
    is_logged = request.user.is_authenticated
    if request.user.is_authenticated:
        user = request.user
    return render(request, 'navigation/home.html', {'user': user, 'is_logged': is_logged})


def search(request):
    form = SearchForm()
    return render(request, 'navigation/search.html', {'form': form})


def results(request):
    try:
        forms = SearchForm(request.POST)
        qs = Babysitter.objects.filter(
            member__full_name__contains=forms['name'].data,
            # we are picking the 'full_name' attribute from the OneToOneField member
            age_target__contains=forms['age_target'].data,
            time_target__contains=forms['time_target'].data,
            location__contains=forms['location'].data
        )
    except ValueError:
        raise Http404(
            "Oops ! La recherche semble avoir échoué. Veuillez réessayer.")

    return render(request, 'navigation/results.html', {'qs': qs, 'forms': forms})