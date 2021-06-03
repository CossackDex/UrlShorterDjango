from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404

from .models import UrlShortener

from .forms import UrlShortenerForm


def home_view(request):
    template = 'home.html'
    context = dict()
    context['form'] = UrlShortenerForm()
    if request.method == "GET":
        return render(request, template, context)
    elif request.method == "POST":
        used_form = UrlShortenerForm(request.POST)
        if used_form.is_valid():
            short_obj = used_form.save()
            context["new_url"] = request.build_absolute_uri('/') + short_obj.short_url
            context["long_url"] = short_obj.long_url
            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request, template, context)


def redirect_view(request, short_part):
    try:
        shortener = UrlShortener.objects.get(short_url=short_part)
        shortener.click()
        return HttpResponseRedirect(shortener.long_url)
    except:
        template = 'home.html'
        context = dict()
        context['errors'] = "Provided link is broken"
        return render(request, template, context)
