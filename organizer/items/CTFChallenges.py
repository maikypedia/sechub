from jinja2 import Template
import os
from datetime import datetime


class CTFChallenges(list):
    template_file = f"{os.path.dirname(__file__)}/templates/CTFChallenges.jinja2"

    @property
    def categories(self):
        categories = []

        for challenge in self:
            for category in challenge["categories"].keys():
                if not category in categories:
                    categories.append(category)

        return categories

    def category_tags(self, category: str):
        tags = []

        for challenge in self:
            if challenge["categories"].get(category):
                for tag in challenge["categories"][category]:
                    if not tag in tags:
                        tags.append(tag)
        return tags

    def get_challenge_by_category(self, category: str):
        challenges = []

        for challenge in self:
            if challenge["categories"].get(category):
                challenges.append(challenge)
        return challenges

    def get_challenge_by_category_tag(self, category: str, tag: str):
        challenges = []

        for challenge in self:
            if challenge["categories"].get(category):
                if tag in challenge["categories"][category]:
                    challenges.append(challenge)
        return challenges

    def render(self, category: str = None, tag: str = None):

        if category:
            if tag:
                challenges = self.get_challenge_by_category_tag(category, tag)
            else:
                challenges = self.get_challenge_by_category(category)
        else:
            challenges = self

        challenges.sort(key=lambda date: datetime.strptime(
            date["published_at"], '%Y/%m/%d'), reverse=True)
        with open(self.template_file, "r") as template:
            return Template(template.read()).render(challenges=challenges)[1:]
