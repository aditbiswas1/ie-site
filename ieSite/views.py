from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def home(request):
    return render(request, 'flatpages/index.html', {})

class GetGame(generic.TemplateView):
    template_name = "html5_games_flappy/index.html"
