from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import RedirectView

# Simple welcome page for root URL
def welcome(request):
    return HttpResponse("""
        <h1>Breathe ESG Carbon Tracking System</h1>
        <p>Welcome to the Carbon Emissions Tracking API!</p>
        <ul>
            <li><a href='/api/'>API Root</a> - View all API endpoints</li>
            <li><a href='/api/normalized-records/'>Normalized Records</a> - View calculated emissions</li>
            <li><a href='/api/dashboard/1/'>Dashboard</a> - Review workflow statistics</li>
            <li><a href='/admin/'>Admin Panel</a> - Login with admin/admin123</li>
        </ul>
        <hr>
        <p><strong>Login Credentials:</strong> admin / admin123</p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ingestion.urls')),
    path('', welcome),  # This fixes the root URL 404
]