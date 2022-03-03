# Table of contents

* [README](<../README.md>)

## CTF

* [Challenges](<CTF/Challenges/README.md>)
{% for category in challenges.categories %}
  * [{{category}}](<CTF/Challenges/{{category}}/README.md>)
  {% for tag in challenges.category_tags(category) %}
    * [{{tag}}](<CTF/Challenges/{{category}}/{{tag}}.md>)
  {% endfor %}
{% endfor %}
* [Resources](<CTF/Resources/README.md>)
  {% for category in resources.categories %}
  * [{{category}}](<CTF/Resources/{{category}}.md>)
  {% endfor %}

## Research

{% for category in articles.categories %}
* [{{category}}](<Research/{{category}}.md>)
{% endfor %}