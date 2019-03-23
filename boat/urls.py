from django.urls import path

from . import views

app_name = 'boat'

urlpatterns = [
    path('constantine/', views.boat_view, name='constantine'),

    
    path('', views.home_view, name='home'),
    path('iguana/', views.iguana_game_view, name='iguana'),
    path('save_game/', views.save_game, name='save_game'),
    path('save_state/', views.save_state, name='save_state'),
    path('scores/', views.scores_view, name='scores'),
    path('instructions/', views.instructions_view, name='instructions')
]


    # path('level_2/', views.level_2_view, name='level_2'),