from django.shortcuts import render
from Team.models import Team

# Create your views here.
def home(request):
    show_warning = True
    teams = Team.objects.all()
    context = {
        "teams":teams,
        'show_warning':show_warning
    }
    return render(request,'index.html',context)