from jinja2 import Template
import os
import pathlib

constants = {
    "BOOK_PATH": "gitbook/"
}


def gen(challenges, resources, articles):
    current_path = os.path.dirname(__file__)
    main_path = os.getcwd()

    rewrites = [
        {
            "template": f"{current_path}/templates/book.json",
            "target": f"{main_path}/book.json",
            "constants": {
                "BOOK_PATH": constants["BOOK_PATH"]
            }
        },
        {
            "template": f"{current_path}/templates/SUMMARY.md",
            "target": f"{main_path}/{constants['BOOK_PATH']}SUMMARY.md",
            "constants": {
                "challenges": challenges,
                "resources": resources,
                "articles": articles
            }
        },
        {
            "template": f"{current_path}/templates/EDIT_ME-challenge.json",
            "target": f"{main_path}/data/ctf/challenges/EDIT_ME.json",
            "constants": {}
        },
        {
            "template": f"{current_path}/templates/EDIT_ME-resource.json",
            "target": f"{main_path}/data/ctf/resources/EDIT_ME.json",
            "constants": {}
        },
        {
            "template": f"{current_path}/templates/EDIT_ME-article.json",
            "target": f"{main_path}/data/research/articles/EDIT_ME.json",
            "constants": {}
        }
    ]

    for rewrite in rewrites:
        with open(rewrite["template"], "r") as template:
            pathlib.Path(os.path.dirname(rewrite["target"])).mkdir(
                parents=True, exist_ok=True
            )

            with open(rewrite["target"], "w+") as target:
                rendered = Template(template.read()).render(
                    rewrite["constants"]
                )
                target.write(rendered)
