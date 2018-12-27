from django.urls import path

from music import views


urlpatterns = [
    path('', views.index, name='index'),
]

# urlpatterns += [
#     path('performers/<int:pk>/', views.performer_detail, name='performer-detail')
# ]

urlpatterns += [
    path('performers/', views.PerformerList.as_view(), name='performer-list'),
    path('performers/<int:pk>/', views.PerformerDetail.as_view(), name='performer-detail'),
    path('performers/create/', views.PerformerCreate.as_view(), name='performer-create'),
    path('performers/<int:pk>/update/', views.PerformerUpdate.as_view(), name='performer-update'),
    path('performers/<int:pk>/delete/', views.PerformerDelete.as_view(), name='performer-delete'),
]

urlpatterns += [
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('songs/<int:pk>/', views.SongDetail.as_view(), name='song-detail'),
    path('songs/create/', views.SongCreate.as_view(), name='song-create'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='song-update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='song-delete'),
]

