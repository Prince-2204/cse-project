from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('home/',views.landing_page,name='landing_page'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('marks/',views.marks,name='marks'),
    path('register/',views.register_student,name='register_student'),
    path('register_select/',views.register_select,name='register_select'),
    path('result-input/',views.result_input,name="result_input"),
    # path('user/',views.User_profile,name="user_profile"),






]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)