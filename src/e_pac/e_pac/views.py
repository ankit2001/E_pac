from django.shortcuts import render 
from django.http import HttpResponse
from .forms import ContactForm

def home_page(request):
	context={
	"title":"homepage",
	"content":"its homepage"
	}
	return render(request,"home_pages.html",context)
def about_page(request):
	context={
	"title":"aboutpage",
	"content":"its aboutpage"
	}
	return render(request,"home_page.html",context)
def contact_page(request):
	contact_form=ContactForm(request.POST or None)
	context={
	"title":"contactpage",
	"content":"its contactpage",
	"form":contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	if request.method=="POST":
		print(request.POST)
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))
	return render(request,"contact/view.html",context)		