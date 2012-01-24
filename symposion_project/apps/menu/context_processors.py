from menu.models import MenuItem


def menuitems(request):
    return {
        "menuitems": MenuItem.objects.filter(published=True),
    }
