
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from videos import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    
    #Auth
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    
    #list
    path('videolist/create', views.CreateList.as_view(), name='create_list'),
    path('videolist/<int:pk>', views.DetailList.as_view(), name='detail_list'),
    path('videolist/<int:pk>/update', views.UpdateList.as_view(), name='update_list'),
    path('videolist/<int:pk>/delete', views.DeleteList.as_view(), name='delete_list'),
    #YT Video
    path('videolist/<int:pk>/addYTvideo', views.add_YT_video, name='add_YT_video'),
    path('video/search', views.video_search, name='video_search'),
    path('videolist/<int:pk>/deleteYTvideo', views.DeleteVideo.as_view(), name='delete_yt_video'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
