from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Video, YT
from django.forms import formset_factory
from .forms import YTForm, SearchForm
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
import urllib
import requests


import os
from dotenv import load_dotenv
load_dotenv()


YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

@login_required
def home(request):
	channels = Video.objects.all()
	recents = Video.objects.all().order_by('-id')[:3]
	return render(request, 'videos/home.html', {'channels':channels, 'recents':recents})

@login_required
def dashboard(request):
	videos = Video.objects.filter(user=request.user)
	print(videos)
	return render(request, 'videos/dashboard.html', {'videos':videos})

@login_required
def add_YT_video(request, pk):
	
	form = YTForm()
	search_form = SearchForm()

	videos = Video.objects.get(pk=pk)
	if not videos.user == request.user:
		raise Http404

	if request.method == 'POST':
		filled_form = YTForm(request.POST)
		if filled_form.is_valid():
			YTvideo = YT()
			YTvideo.url = filled_form.cleaned_data['url']
			parsed_url = urllib.parse.urlparse(YTvideo.url)
			video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
			#This gets what ever V is equal to in the YT URL i.e. the YT ID
			if video_id:
				
				try:
					YTvideo.youtube_id = video_id[0]
					response = requests.get(f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={video_id[0]}&key={YOUTUBE_API_KEY}')
					json = response.json()
					title = json['items'][0]['snippet']['title']
					YTvideo.title = title
					YTvideo.save()

					messages.success(request, f'YouTube video: {video_id[0]} added.')
					return redirect('detail_list', pk)
				except IndexError as e:
					errors = form.errors.setdefault('url', ErrorList())
					errors.append(f'YouTube ID not recognised. This likely means the URL is incorrect or the video does not exist.')
			
			else:
				errors = form.errors.setdefault('url', ErrorList())
				errors.append('Please use a YouTube URL only.')


	return render(request, 'videos/add_YT_video.html', {'form': form, 
														'search_form':search_form,
														'videos':videos})


@login_required														
def video_search(request):
	search_form = SearchForm(request.GET)
	if search_form.is_valid():
		
		encoded_search_term = urllib.parse.quote(search_form.cleaned_data['search_term'])
		response = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={encoded_search_term}&key={YOUTUBE_API_KEY}')
		return JsonResponse(response.json())
	return JsonResponse({'Error':'Not able to validate form'})

class DeleteVideo(LoginRequiredMixin, generic.DeleteView):
	model = YT
	template_name = 'videos/delete_YT_video.html'
	success_url = reverse_lazy('dashboard')
	# might need cleaning here
	def get_object(self):
		video = super(DeleteVideo, self).get_object()
		if not video.user == self.request.user:
			raise Http404
		return video

class SignUp(LoginRequiredMixin, generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('dashboard')
	template_name = 'registration/signup.html'

	def form_valid(self, form):
		view = super(SignUp, self).form_valid(form)
		username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return view


class CreateList(LoginRequiredMixin, generic.CreateView):
	model = Video
	fields = ['title']
	template_name = 'videos/create_list.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.user = self.request.user
		super(CreateList, self).form_valid(form)
		return redirect('dashboard')


class DetailList(LoginRequiredMixin, generic.DetailView):
	model = Video
	template_name = 'videos/detail_list.html'


class UpdateList(LoginRequiredMixin, generic.UpdateView):
	model = Video
	template_name = 'videos/update_list.html'
	fields = ['title']
	success_url = reverse_lazy('dashboard')

class DeleteList(generic.DeleteView):
	model = Video
	template_name = 'videos/delete_list.html'
	fields = ['title']
	success_url = reverse_lazy('dashboard')
