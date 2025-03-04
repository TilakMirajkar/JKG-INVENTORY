from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', views.SupplierView.as_view(), name='supplier_detail'),
    path('suppliers/create/', views.SupplierView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', views.SupplierView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.SupplierView.as_view(), name='supplier_delete'),

    path('categories/', views.CategoryView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category_detail'),
    path('categories/create/', views.CategoryView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryView.as_view(), name='category_delete'),

    path('', views.ItemView.as_view(), name='item_list'),
    path('<int:pk>/', views.ItemView.as_view(), name='item_detail'),
    path('create/', views.ItemView.as_view(), name='item_create'),
    path('<int:pk>/update/', views.ItemView.as_view(), name='item_update'),
    path('<int:pk>/delete/', views.ItemView.as_view(), name='item_delete'),

    path('purchase-orders/', views.PurchaseOrderView.as_view(), name='purchase_order_list'),
    path('purchase-orders/<int:pk>/', views.PurchaseOrderView.as_view(), name='purchase_order_detail'),
    path('purchase-orders/create/', views.PurchaseOrderView.as_view(), name='purchase_order_create'),
    path('purchase-orders/<int:pk>/update/', views.PurchaseOrderView.as_view(), name='purchase_order_update'),
    path('purchase-orders/<int:pk>/delete/', views.PurchaseOrderView.as_view(), name='purchase_order_delete'),

    path('sales-orders/', views.SalesOrderView.as_view(), name='sales_order_list'),
    path('sales-orders/<int:pk>/', views.SalesOrderView.as_view(), name='sales_order_detail'),
    path('sales-orders/create/', views.SalesOrderView.as_view(), name='sales_order_create'),
    path('sales-orders/<int:pk>/update/', views.SalesOrderView.as_view(), name='sales_order_update'),
    path('sales-orders/<int:pk>/delete/', views.SalesOrderView.as_view(), name='sales_order_delete'),
]