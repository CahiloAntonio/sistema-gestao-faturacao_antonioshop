from django import template

register = template.Library()

@register.filter
def kwanza(value):
    try:
        return f"{float(value):,.2f} Kz".replace(",", " ").replace(".", ",")
    except:
        return value