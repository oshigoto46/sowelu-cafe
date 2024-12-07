from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    辞書からキーに基づいて値を取得します。
    キーが存在しない場合、空のリストを返します。
    """
    return dictionary.get(key, [])
