from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render, redirect  
from donation.forms import DonationForm  
from donation.models import Donation  

def donation(request):  
    if request.method == "POST":  
        form = DonationForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = DonationForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    donations = Donation.objects.all()  
    return render(request,"show.html",{'donations':donations})  
def edit(request, id):  
    donation = Donation.objects.get(id=id)  
    return render(request,'edit.html', {'donation':donation})  
def update(request, id):  
    donation = Donation.objects.get(id=id)  
    form = DonationForm(request.POST, instance = donation)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'donation': donation})  
def destroy(request, id):  
    donation = Donation.objects.get(id=id)  
    donation.delete()  
    return redirect("/show")