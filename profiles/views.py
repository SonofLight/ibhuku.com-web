from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from profiles.forms import ProfileAvatarUploadForm
from accounts.models import IbkUser, Profile

# Create your views here.
@login_required
def ProfileDashboardView(request, name=None):
	usr_name = IbkUser.objects.get(name=name)
	usr_profile = Profile.objects.select_related('user').get(user_id=usr_name.id)
	context = {
		'user': usr_name,
		'profile': usr_profile,
	}
	return render(request, 'profiles/profile_dashboard.html', context)

@login_required
def ProfileAvatarUploadView(request, name=None, pk=None):
	usr_profile = Profile.objects.select_related('user').get(user_id=pk)
	form = ProfileAvatarUploadForm(request.FILES, request.POST or None)
	context = {
		'profile': usr_profile,
		'form': form,
	}
	return render(request, 'profiles/profile_avatar_upload.html', context)
