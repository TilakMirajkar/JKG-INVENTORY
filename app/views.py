from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Supplier, Category, Item, PurchaseOrder, SalesOrder
from .forms import SupplierForm, CategoryForm, ItemForm, PurchaseOrderForm, SalesOrderForm

@method_decorator(login_required, name='dispatch')
class SupplierView(View):
    def get(self, request, pk=None):
        if pk:
            supplier = get_object_or_404(Supplier, pk=pk)
            return render(request, 'app/supplier_detail.html', {'supplier': supplier})
        else:
            suppliers = Supplier.objects.all()
            return render(request, 'app/supplier_list.html', {'suppliers': suppliers})

    def post(self, request, pk=None):
        if pk:
            supplier = get_object_or_404(Supplier, pk=pk)
            form = SupplierForm(request.POST, instance=supplier)
            if form.is_valid():
                form.save()
                return redirect('supplier_list')
        else:
            form = SupplierForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('supplier_list')
        return render(request, 'app/supplier_form.html', {'form': form})

    def delete(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        supplier.delete()
        return redirect('supplier_list')

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            return render(request, 'app/category_detail.html', {'category': category})
        else:
            categories = Category.objects.all()
            return render(request, 'app/category_list.html', {'categories': categories})

    def post(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('category_list')
        else:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('category_list')
        return render(request, 'app/category_form.html', {'form': form})

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('category_list')

@method_decorator(login_required, name='dispatch')
class ItemView(View):
    def get(self, request, pk=None):
        if pk:
            item = get_object_or_404(Item, pk=pk)
            return render(request, 'app/item_detail.html', {'item': item})
        else:
            items = Item.objects.all()
            return render(request, 'app/item_list.html', {'items': items})

    def post(self, request, pk=None):
        if pk:
            item = get_object_or_404(Item, pk=pk)
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('item_list')
        else:
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('item_list')
        return render(request, 'app/item_form.html', {'form': form})

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('item_list')

@method_decorator(login_required, name='dispatch')
class PurchaseOrderView(View):
    def get(self, request, pk=None):
        if pk:
            purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
            return render(request, 'app/purchase_order_detail.html', {'purchase_order': purchase_order})
        else:
            purchase_orders = PurchaseOrder.objects.all()
            return render(request, 'app/purchase_order_list.html', {'purchase_orders': purchase_orders})

    def post(self, request, pk=None):
        if pk:
            purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
            form = PurchaseOrderForm(request.POST, instance=purchase_order)
            if form.is_valid():
                form.save()
                return redirect('purchase_order_list')
        else:
            form = PurchaseOrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('purchase_order_list')
        return render(request, 'app/purchase_order_form.html', {'form': form})

    def delete(self, request, pk):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        purchase_order.delete()
        return redirect('purchase_order_list')

@method_decorator(login_required, name='dispatch')
class SalesOrderView(View):
    def get(self, request, pk=None):
        if pk:
            sales_order = get_object_or_404(SalesOrder, pk=pk)
            return render(request, 'app/sales_order_detail.html', {'sales_order': sales_order})
        else:
            sales_orders = SalesOrder.objects.all()
            return render(request, 'app/sales_order_list.html', {'sales_orders': sales_orders})

    def post(self, request, pk=None):
        if pk:
            sales_order = get_object_or_404(SalesOrder, pk=pk)
            form = SalesOrderForm(request.POST, instance=sales_order)
            if form.is_valid():
                form.save()
                return redirect('sales_order_list')
        else:
            form = SalesOrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('sales_order_list')
        return render(request, 'app/sales_order_form.html', {'form': form})

    def delete(self, request, pk):
        sales_order = get_object_or_404(SalesOrder, pk=pk)
        sales_order.delete()
        return redirect('sales_order_list')