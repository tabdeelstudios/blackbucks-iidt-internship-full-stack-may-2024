from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def gen_resume(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        userEmail = request.POST.get('userEmail', '')
        return render(request, 'resume.html', {'firstName':firstName, 'lastName':lastName, 'userEmail':userEmail})
    return render(request, 'index.html')