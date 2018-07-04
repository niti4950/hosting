from .models import*

#make a variable available in all templates
def cart_items(request):
    items = Cart.objects.all()
    """
    q=[]
    for i in items:
        q.append(i.quantity)
        print(q)
    """

    return {'total_items':len(items)}