from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Team
from Player.models import Player

@login_required
def create_team(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        description = request.POST.get('description')
        logo = request.FILES.get('logo')
        established = request.POST.get('established')

        # Create Team instance
        team = Team.objects.create(
            name=name,
            description=description,
            logo=logo,
            established=established
        )

        # Associate the created team with the current player
        player = Player.objects.get(user=request.user)
        player.team = team
        player.save()

        return redirect('player_profile')  # Redirect to player profile page after team creation

    return render(request, 'create_team.html')


def team_profile(request, team_id):
    # Fetch the team object using the team_id from URL parameter
    team = get_object_or_404(Team, pk=team_id)

    data = {
        "team":team
    }
    
    # Render the team profile template with the team object
    return render(request, 'myteam.html', data)