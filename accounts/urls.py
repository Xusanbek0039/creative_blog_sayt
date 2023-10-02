from django.urls import path
from . import views

# auth views ni import qilish 
from django.contrib.auth import views as auth_views 

urlpatterns = [

  path('signup/', views.SignUpView.as_view(), name='signup'),

  path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),

  path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

  path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

  path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]