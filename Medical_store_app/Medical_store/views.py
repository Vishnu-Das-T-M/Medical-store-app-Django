from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Medicine
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.list import ListView

def index(request):
    num_medicine = Medicine.objects.all().count()
    return render(request, 'index.html', {'num_medicine': num_medicine})


class MedicineList(LoginRequiredMixin,ListView):
    model=Medicine     

class MedicineCreate(LoginRequiredMixin,CreateView):
    model = Medicine
    fields = '__all__'
    success_url = reverse_lazy('index')
    
class MedicineUpdate(LoginRequiredMixin,UpdateView):
    model = Medicine
    fields = '__all__' 
    success_url= reverse_lazy('index')

class MedicineDelete(LoginRequiredMixin,DeleteView):
    model = Medicine
    success_url = reverse_lazy('index')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Medicine.objects.filter(name__icontains=query_name)
            return render(request, 'product-search.html', {"results":results})

    return render(request, 'product-search.html')

 


