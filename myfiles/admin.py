from django.contrib import admin
from myfiles.models import Category, Portfolio, Clients, Services,Team, Add
# Register your models here.
class AdminPortfolio(admin.ModelAdmin):
	list_display = ['id','name','owner','deadline','rasm1','rasm2',
	'rasm3','type','desc','date']
admin.site.register(Portfolio,AdminPortfolio)

class AdminCategory(admin.ModelAdmin):
	list_display = ['id','name']
admin.site.register(Category,AdminCategory)

class AdminClients(admin.ModelAdmin):
	list_display = ['id','rasm']
admin.site.register(Clients,AdminClients)

class AdminServices(admin.ModelAdmin):
	list_display = ['id','title','text']
admin.site.register(Services,AdminServices)

class AdminTeam(admin.ModelAdmin):
	list_display = ['id','ism','lavozim','rasm']
admin.site.register(Team,AdminTeam)

class AdminAdd(admin.ModelAdmin):
	list_display = ['id','name','email','subject','message']
admin.site.register(Add,AdminAdd)