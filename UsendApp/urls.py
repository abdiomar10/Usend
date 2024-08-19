from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('runner_dashboard/', views.runner_dashboard, name='runner_dashboard'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('set_price/<int:task_id>/', views.set_price, name='set_price'),
    path('accept_task/<int:task_id>/<str:action>/', views.accept_task, name='accept_task'),
    path('post_task/', views.post_task, name='post_task'),
    path('contact/', views.contact, name='contact'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('oauth_login/', views.oauth_login, name='oauth_login'),
    path('oauth_callback/', views.oauth_callback, name='oauth_callback'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('csrf_failure/', views.csrf_failure, name='csrf_failure'),
    path('pay_runner/<int:task_id>/', views.pay_runner, name='pay_runner'),

]
