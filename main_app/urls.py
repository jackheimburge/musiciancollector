from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bands/', views.bands_index, name='bands_index'),
    path('bands/<int:band_id>/', views.bands_detail, name='detail'),
    path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
    path('bands/<int:pk>/update', views.BandUpdate.as_view(), name='band_update'),
    path('bands/<int:pk>/delete', views.BandDelete.as_view(), name='band_delete'),
    path('bands/<int:band_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
    path('bands/<int:band_id>/unassoc_award/<int:award_id>/', views.unassoc_award, name='unassoc_award'),
    path('bands/<int:band_id>/add_musician/', views.add_musician, name='add_musician'),
    path('awards/', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name='awards_update'),
    path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name='awards_delete'),
    path('awards/create/', views.AwardCreate.as_view(), name='awards_create')
]