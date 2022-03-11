from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('train/', views.train, name="train"),
	path('checkout/', views.checkout, name="checkout"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
	path('main/', views.main, name="main"),

	path('logout/', views.logoutUser, name="logout")

]