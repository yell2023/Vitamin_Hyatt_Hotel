from django.urls import path, include
from hotels import views

urlpatterns = [

    path('book/',views.BookManage.as_view(), name='book'),
    path('rooms/', views.RoomView.as_view(), name='rooms_view'),
    path('rooms/spot/', views.SpotViewAPI.as_view(), name='spot_view'),
    path('rooms/spot/<int:spot_id>', views.SpotViewAPI.as_view(), name='spot_detail_view'),
    path('rooms/<int:room_id>/', views.DetailRoomViewAPI.as_view(), name='detail_room_view'),
    path('customers/<int:room_id>/', views.BookUsersViewAPI.as_view()),
]
