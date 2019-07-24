from django.urls import path
from cms import views

urlpatterns = [
	path('',views.login_home),
	path('logout',views.logout),

	path('dashboard',views.dashboard),
	path('dashboard1',views.dashboard1),

	path('signup',views.signUp),
	path('discussion',views.discussion),
	path('quiz',views.quiz),
	path('marks',views.marks),
	path('marks1',views.marks1),
	
	path('course',views.course),
	path('schedule',views.schedule),
	path('enroll_coure',views.enroll_course),
	path('feedback',views.feedback),
	path('dashboard',views.dashboard),
]