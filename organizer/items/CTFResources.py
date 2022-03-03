from jinja2 import Template
import os


class CTFResources(list):
    template_file = f"{os.path.dirname(__file__)}/templates/CTFResources.jinja2"

    @property
    def categories(self):
        categories = []

        for resource in self:
            for category in resource["categories"]:
                if not category in categories:
                    categories.append(category)

        return categories

    def get_resource_by_category(self, category: str):
        resources = []

        for resource in self:
            if category in resource["categories"]:
                resources.append(resource)
        return resources

    def render(self, category: str = None, tag: str = None):

        if category:
            resources = self.get_resource_by_category(category)
        else:
            resources = self

        with open(self.template_file, "r") as template:
            return Template(template.read()).render(resources=resources)[1:]
