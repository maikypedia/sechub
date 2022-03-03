from glob import glob
import json
from core.file import File
import core.constants
from items.CTFChallenges import CTFChallenges
from items.CTFResources import CTFResources
from items.ResearchArticles import ResearchArticles

challenges = CTFChallenges()
resources = CTFResources()
articles = ResearchArticles()

for entry in glob("data/ctf/challenges/[!EDIT_ME]*.json"):
    with open(entry, "r") as data:
        data = json.load(data)
        challenges.append(data)

for entry in glob("data/ctf/resources/[!EDIT_ME]*.json"):
    with open(entry, "r") as data:
        data = json.load(data)
        resources.append(data)

for entry in glob("data/research/articles/[!EDIT_ME]*.json"):
    with open(entry, "r") as data:
        data = json.load(data)
        articles.append(data)

# Regenerate files regarding constants
core.constants.gen(challenges=challenges,
                   resources=resources, articles=articles)

for category in challenges.categories:
    File(f"CTF/Challenges/{category}/General", challenges.render(category))

    for tag in challenges.category_tags(category):
        File(f"CTF/Challenges/{category}/{tag}",
             challenges.render(category, tag)
             )

# Resources
File("CTF/Resources/General", resources.render())

for category in resources.categories:
    File(f"CTF/Resources/{category}", resources.render(category))


for category in articles.categories:
    File(f"Research/{category}", articles.render(category))
