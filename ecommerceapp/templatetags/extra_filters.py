from django import template

register = template.Library()

@register.filter(name='sumQty')
def sumQty(value):
    array =  list(value.split(","))
    q =  [int(i) for i in array]
    a = sum(q)
    return a

@register.filter(name='convertToArray')
def convertToArray(value):
    array =  list(value.split(","))
    q =  [int(i) for i in array]
    return q

@register.filter(name='lookup')
def lookup(d,key):
    return d[key]
