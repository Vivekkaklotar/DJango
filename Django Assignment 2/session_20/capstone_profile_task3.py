@login_required
def update_flipkart_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST['name']
        request.user.email = request.POST['email']
        request.user.save()
        
        profile = request.user.profile
        profile.address = request.POST['address']
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        return redirect('profile_view')