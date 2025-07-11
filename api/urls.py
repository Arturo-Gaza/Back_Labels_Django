from django.urls import path
from api.views import CatRecordList, CatRecordCreate, SelloListView, CatSelloCreate, PaisListView, CatRecordUpdate, CatSelloUpdate
from api.views import CatArtistaListView, CatArtistaCreate

urlpatterns = [
    path('cat_records/', CatRecordList.as_view(), name='cat-record-list'),
    path('cat_records/create/', CatRecordCreate.as_view(), name='cat-record-create'),
    path('record/update/<int:pk>/', CatRecordUpdate.as_view(), name='record-update'),
    path('sellos/', SelloListView.as_view(), name='sellos-list'),
    path('sellos/create', CatSelloCreate.as_view(), name='cat-sellos-create'),
    path('sellos/update/<int:pk>/', CatSelloUpdate.as_view(), name='cat-sellos-update'),
    path('pais/', PaisListView.as_view(), name='list-pais'),

#endpoints de Artistas 
    path('artistas/', CatArtistaListView.as_view(), name='list-artista'),
    path('artistas/create', CatArtistaCreate.as_view(), name= 'artistas-create')
]
