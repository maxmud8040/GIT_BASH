from .models import *


def lasted_news(request):
    lasted_news = News.published.all().order_by("-publish_time")[:3]
    categories = Category.objects.all()
    contact_data = ContactData.objects.all()

    context = {
        'lasted_news':lasted_news,
        'categories': categories,
        'contact_data': contact_data,
    }
    return context