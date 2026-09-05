# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InfluencerProfile

@login_required
def edit_profile(request):
    profile, created = InfluencerProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.display_name = request.POST.get('display_name')
        profile.bio = request.POST.get('bio')
        
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
            
        profile.save()
        return redirect('view_profile')
        
    return render(request, 'profile/edit_profile.html', {'profile': profile})