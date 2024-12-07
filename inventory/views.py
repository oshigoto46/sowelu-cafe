from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import InventoryItem
from .forms import InventoryForm

# 仮のデータ
INVENTORY = {
    1: {"name": "牛肉(カレー用)", "price": 2900, "quantity": 2, "unit": "kg"},
    2: {"name": "カレーフレーク①", "price": 950, "quantity": 1, "unit": "kg"},
}

def inventory_home(request):
    return HttpResponse("<h1>Inventory Home</h1>")

def inventory_list(request):
    items = InventoryItem.objects.all()  # データベースからすべてのアイテムを取得
    return render(request, 'inventory/inventory_list.html', {'items': items})

def inventory_add(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventory/inventory_add.html', {'form': form})

def inventory_detail(request, item_id):
    # データを取得
    item = INVENTORY.get(item_id)
    if item:
        return render(request, 'inventory/inventory_detail.html', {"item": item})
    else:
        return render(request, 'inventory/inventory_detail.html', {"item": None}, status=404)
