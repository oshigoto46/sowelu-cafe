from django.db import models

class InventoryItem(models.Model):
    code = models.CharField(max_length=100, unique=True, default='default_code')
    name = models.CharField(max_length=200)  # 商品名
    category = models.CharField(max_length=100)  # カテゴリ
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 単価
    supplier = models.CharField(max_length=200)  # 卸業者
    current_stock = models.IntegerField(default=0)  # 現在在庫数
    min_stock = models.IntegerField(default=10)  # 最小在庫数

    def __str__(self):
        return self.name
