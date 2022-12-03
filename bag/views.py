from django.shortcuts import render


def view_bag(request):
    """ A view that shows the shhooing bag contents"""

    return render(request, 'bag/bag.html')
