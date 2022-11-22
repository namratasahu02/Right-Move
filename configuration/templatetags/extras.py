from django import template

register = template.Library() 


@register.filter(name="sort_price")
def sort_price(price):
    l= len(price)
    price = int(price)

    if l==4 or l==5:
        new_price = price / 1000
        new_price = str(new_price) + ' K'

    elif l==6 or l==7:
        new_price = price / 100000
        new_price = str(new_price) + ' L'

    elif l==8 or l==9:
        new_price = price / 10000000
        new_price = str(new_price) + ' Cr'

    else:
        new_price = price 

    return new_price 