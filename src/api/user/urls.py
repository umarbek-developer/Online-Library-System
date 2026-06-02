from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views import book_views, borrow_views, wishlist_views

router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
    path('book/list/', book_views.BookListApiView.as_view(), name='book-list'),
    path('borrow/list/', borrow_views.BorrowListApiView.as_view(), name='borrow-list'),
    path('wishlist/list/', wishlist_views.WishlistListApiView.as_view(), name='wishlist-list'),

    path('book/create/', book_views.BookCreateApiView.as_view(), name='book-Create'),
    path('borrow/create/', borrow_views.BorrowCreateApiView.as_view(), name='borrow-Create'),
    path('wishlist/create/', wishlist_views.WishlistCreateApiView.as_view(), name='wishlist-Create'),

    path('book/update/<int:pk>/', book_views.BookUpdateApiView.as_view(), name='book-Update'),
    path('borrow/update/<int:pk>/', borrow_views.BorrowUpdateApiView.as_view(), name='borrow-Update'),

    path('book/delete/<int:pk>/', book_views.BookDeleteApiView.as_view(), name='book-Delete'),
    path('borrow/delete/<int:pk>/', borrow_views.BorrowDeleteApiView.as_view(), name='borrow-Delete'),
    path('wishlist/delete/<int:pk>/', wishlist_views.WishlistDeleteApiView.as_view(), name='wishlist-Delete'),

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]
