from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())
def about(request):
    return render(request, 'about.html', locals())
def contact(request):
    return render(request, 'contact.html', locals())
def feature(request):
    return render(request, 'feature.html', locals())
def appointment(request):
    return render(request, 'appointment.html', locals())
def project(request):
    return render(request, 'project.html', locals())
def team(request):
    return render(request, 'team.html', locals())
def testimonial(request):
    return render(request, 'testimonial.html', locals())
def service(request):
    return render(request, 'service.html', locals())