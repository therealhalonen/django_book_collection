from django.contrib import admin
from django.urls import path, include
from book import views
#authentication
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view()),
    path('<int:pk>/', views.BookDetailView.as_view()),
    path('new/', views.BookCreateView.as_view()),
    path('<int:pk>/update', views.BookUpdateView.as_view()),
    path('<int:pk>/delete', views.BookDeleteView.as_view()),
#for authentication
    path('accounts/', include('django.contrib.auth.urls')),
#for registering
    path("register/", views.register, name="register"),
]
