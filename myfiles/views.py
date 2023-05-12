from django.shortcuts import render
from .models import Portfolio, Clients, Services, Team, Add
# Create your views here.
def index(malumot):
	malumotlar = Portfolio.objects.all()
	clients = Clients.objects.all()
	services = Services.objects.all()
	team = Team.objects.all()
	return render(malumot,'index.html',{'portfolio':malumotlar,'clients':clients,
		'services':services,'team':team})

def portfolio(malumot,id):
	data = Portfolio.objects.get(id=id)
	return render(malumot,'portfolio-details.html',{'port':data})

def add(malumot):
	if malumot.method == 'POST':
		name = malumot.POST.get('name')
		email = malumot.POST.get('email')
		subject = malumot.POST.get('subject')
		message = malumot.POST.get('message')

		add = Add(name=name,email=email,subject=subject,message=message).save()

	return render(malumot, 'index.html',{'add':add})