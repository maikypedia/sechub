from jinja2 import Template
import os
from datetime import datetime


class ResearchArticles(list):
    template_file = f"{os.path.dirname(__file__)}/templates/ResearchArticles.jinja2"

    @property
    def categories(self):
        categories = []

        for article in self:
            for category in article["categories"].keys():
                if not category in categories:
                    categories.append(category)

        return categories

    def category_tags(self, category: str):
        tags = []

        for article in self:
            if article["categories"].get(category):
                for tag in article["categories"][category]:
                    if not tag in tags:
                        tags.append(tag)
        return tags

    def get_article_by_category(self, category: str):
        articles = []

        for article in self:
            if article["categories"].get(category):
                articles.append(article)
        return articles

    def get_article_by_category_tag(self, category: str, tag: str):
        articles = []

        for article in self:
            if article["categories"].get(category):
                if tag in article["categories"][category]:
                    articles.append(article)
        return articles

    def render(self, category: str = None, tag: str = None):

        if category:
            if tag:
                articles = self.get_article_by_category_tag(category, tag)
            else:
                articles = self.get_article_by_category(category)
        else:
            articles = self

        articles.sort(key=lambda date: datetime.strptime(
            date["published_at"], '%Y/%m/%d'), reverse=True)

        with open(self.template_file, "r") as template:
            return Template(template.read()).render(articles=articles)[1:]
