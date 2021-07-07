from django.core.management.base import BaseCommand, CommandError
from blog.models import Article

import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Fills database with articles from "rss feed" type link'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str,
                    help='Rss feed url')

    def handle(self, *args, **options):
        url = options['url']

        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'xml')

        items = soup.find_all('item')

        filter_func = lambda x : not Article.objects.filter(name=x.find('title').text).exists()
        unadded = filter(filter_func, items)

        for item in unadded:
            body = BeautifulSoup(item.find('description').text, 'lxml').body
            content = ''.join([str(x) for x in body.contents])
            
            article = Article(
                name=item.find('title').text,
                summary="None yet",
                content=content,
                post_date=item.find('pubDate').text
            )
            article.save()
