from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'emobot'
urlpatterns = [ 
	
	# about us 
    path('about', views.EmobotAbout.as_view(), name="about_view"),
   
    #video 
    path('video', views.EmobotVideo.as_view(), name="video_view"), 
   
    #text
    path('text', views.EmobotText.as_view(), name="text_view"),	

    #home   
    path('home', views.EmobotHome.as_view(), name="home_view"),    

    #Signup
    path('signup', views.EmobotSignup, name="signup_view"),    

    #Login 
    path('login', views.EmobotLogin, name="login_view"),  

    #Logout
    path('logout', views.EmobotLogout, name="logout_view"),
    
 ]