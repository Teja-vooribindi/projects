"""
URL configuration for COMPANY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from login_management import views  # Import views from the login_management app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('employee-login/add/', views.add_employee_login, name='add_employee_login'),  # Add login credentials
    path('employee-login/update/<int:user_id>/', views.update_employee_login, name='update_employee_login'),  # Update login credentials
    path('employee-login/fetch/<int:user_id>/', views.fetch_employee_login, name='fetch_employee_login'),  # Fetch login credentials
    path('employee-login/show-all/', views.show_all_logins, name='show_all_logins'),  # Show all login credentials
    path('', views.add_employee_login, name='home'),  # Define the root URL (home page) to redirect to 'add_employee_login'
]
