from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('users/', include('apps.user.api.v1.user_url', namespace='users')),
]
