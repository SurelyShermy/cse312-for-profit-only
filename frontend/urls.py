from django.urls import path
from .views import index, register, user_dashboard, CustomLoginView, pvp, pve_session_setup, mp_session_setup, files
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('userdashboard/', user_dashboard, name='userdashboard'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('userdashboard/mp_session_setup/', mp_session_setup, name='mp_session_setup'),
    path('pvp/<str:game_id>/', pvp, name='pvp_game'),
    path('engine/<str:game_id>/', pve_session_setup, name='engine'),
    path('favicon.ico', files, name='favicon'),
    path('manifest.json', files, name='manifest'),
    path('logo192.png', files , name='logo192'),
    path("chessPieces/white/K.svg", files, name='whiteK'),
    path("chessPieces/white/Q.svg", files, name='whiteQ'),
    path("chessPieces/white/R.svg", files, name='whiteR'),
    path("chessPieces/white/N.svg", files, name='whiteN'),
    path("chessPieces/white/B.svg", files, name='whiteB'),
    path("chessPieces/white/P.svg", files, name='whiteP'),
    path("chessPieces/black/k.svg", files, name='blackK'),
    path("chessPieces/black/q.svg", files, name='blackQ'),
    path("chessPieces/black/r.svg", files, name='blackR'),
    path("chessPieces/black/n.svg", files, name='blackN'),
    path("chessPieces/black/b.svg", files, name='blackB'),
    path("chessPieces/black/p.svg", files, name='blackP'),
]