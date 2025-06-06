from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .forms import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:val>',Categoryview.as_view(),name='category'),
    path('category-title/<val>',CategoryTitle.as_view(),name='category-title'),
    path('product-detail/<int:pk>',ProductDetail.as_view(),name='product-detail'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('register', RegistrationView.as_view(), name='register'),
    path('login',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('password-reset',auth_view.PasswordResetView.as_view(template_name='reset.html',form_class=PasswordResetForm),name='reset'),
    path('profile',ProfileView.as_view(),name='profile'),
    path('address',ProfileView.as_view(),name='address'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)