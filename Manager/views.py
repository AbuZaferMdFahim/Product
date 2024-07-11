from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Manager

# Create your views here.
@login_required
def check_manager_profile(request):
    try:
        manager = Manager.objects.get(user=request.user)
        return redirect('manager_profile')
    except Manager.DoesNotExist:
        return render(request, 'check_manager_profile.html')  

@login_required
def create_manager_profile(request):
    return redirect('manager_profile_create')

@login_required
def manager_profile(request):
    manager = Manager.objects.get(user=request.user)
    context = {
        'manager': manager
    }
    return render(request, 'manager_profile.html', context)

def manager_profile_create(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        role = request.POST.get('role')
        age = request.POST.get('age')
        team = request.POST.get('team')
        img = request.FILES.get('img')
        NID_number = request.POST.get('NID_number')
        nationality = request.POST.get('nationality')
        nationality_image = request.FILES.get('nationality_image')

        # Create a new managerProfile instance
        manager_profile = Manager(
            user=request.user,  # Set the user field to the currently logged-in user
            name=name,
            bio=bio,
            role=role,
            age=age,
            team = team,
            img=img,
            NID_number=NID_number,
            nationality=nationality,
            nationality_image=nationality_image,
        )

        # Save the instance to the database
        manager_profile.save()

        messages.success(request, 'Manager profile created successfully.')
        return redirect('home')  # Replace 'home' with your home page URL name or path
    else:
        return render(request, 'manager_profile_create.html')

