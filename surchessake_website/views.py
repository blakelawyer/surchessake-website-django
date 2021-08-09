from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	return render(request, 'static_pages/index.html')

def downloads(request):
	return render(request, 'downloads.html')

def tournaments(request):
	return render(request, 'tournaments.html')

def login(request):
	return render(request, 'login.html')

class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/profile.html'