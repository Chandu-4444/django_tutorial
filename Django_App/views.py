from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        entered_name = request.POST['user_name']
        email = request.POST['email']
        
        print(entered_name, email)
        # return render(request, 'contacts.html')
        return redirect(reverse('contacts'))



    



def contacts_page(request):
    return render(request, 'contacts.html')





