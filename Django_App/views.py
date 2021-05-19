from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Blog

# Create your views here.
# results = 0

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        # global results
        # user_name = request.POST['user_name']
        # new_obj = Detail()
        # new_obj.name = user_name
        # new_obj.save()
        # results = Detail.objects.filter(name__icontains = search_input)
        return redirect(reverse('contacts'))


def contacts_page(request):
    # global results
    # objects_list = Detail.objects.all()
    return render(request, 'contacts.html', {'list': objects_list})




