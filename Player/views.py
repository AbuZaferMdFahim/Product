from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Player

@login_required
def check_player_profile(request):
    try:
        player = Player.objects.get(user=request.user)
        return redirect('player_profile')
    except Player.DoesNotExist:
        return render(request, 'check_player_profile.html')  

@login_required
def create_player_profile(request):
    return redirect('player_profile_create')

@login_required
def player_profile(request):
    player = Player.objects.get(user=request.user)
    context = {
        'player': player
    }
    return render(request, 'player_profile.html', context)

def player_profile_create(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        kit = request.POST.get('kit')
        position = request.POST.get('position')
        age = request.POST.get('age')
        team = request.POST.get('team')
        img = request.FILES.get('img')
        NID_number = request.POST.get('NID_number')
        nationality = request.POST.get('nationality')
        nationality_image = request.FILES.get('nationality_image')
        rating = request.POST.get('rating')

        # Create a new PlayerProfile instance
        player_profile = Player(
            user=request.user,  # Set the user field to the currently logged-in user
            name=name,
            bio=bio,
            kit=kit,
            position=position,
            age=age,
            team = team,
            img=img,
            NID_number=NID_number,
            nationality=nationality,
            nationality_image=nationality_image,
            rating=rating
        )

        # Save the instance to the database
        player_profile.save()

        messages.success(request, 'Player profile created successfully.')
        return redirect('home')  # Replace 'home' with your home page URL name or path
    else:
        position_choices = Player.POSITION_CHOICES
        rating_choices = Player.RATING_CHOICES
        context = {
            'position_choices': position_choices,
            'rating_choices': rating_choices
        }
        return render(request, 'player_profile_create.html', context)

@login_required
def addplayer_list(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'addplayer_list.html', context)