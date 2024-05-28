from django.urls import path
from . import views
urlpatterns=[
    path('',views.add,name='add'),
    # path('',views.TasklistView.as_view(),name='cbvhome'),
    path('cbvhome/', views.TasklistView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskdetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskupdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskdeleteView.as_view(),name='cbvdelete'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    # path('details',views.details,name='details')
]