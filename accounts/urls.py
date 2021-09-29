from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserView, apiOverview, ShowAll, ViewProduct, CreateProduct, updateProduct, deleteProduct


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('', apiOverview, name='apiOverview'),
    path('product-list/', ShowAll, name='product-list'),
    path('product-detail/<int:pk>/', ViewProduct, name='product-detail'),
    path('product-create/', CreateProduct, name='product-create'),
    path('product-update/<int:pk>/', updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', deleteProduct, name='product-delete'),
]