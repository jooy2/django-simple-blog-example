from blog.models import Config
import datetime


def blog_meta(request):
    blog_name = Config.objects.filter(key='blog_name')
    blog_description = Config.objects.filter(key='blog_description')
    current_year = datetime.datetime.now().year

    if not blog_name.exists():
        blog_name[0].value = 'My Blog'

    if not blog_description.exists():
        blog_description[0].value = 'My sample blog'

    return {
        'blog_name': blog_name[0].value,
        'blog_description': blog_description[0].value,
        'current_year': current_year,
    }
