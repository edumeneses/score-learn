---
layout: default
title: Find by topic
description: "The course as a knowledge base: common questions about score, grouped by topic, each linked to the section of the lesson that answers it."
nav_order: 2
permalink: /topics
---

# Find by topic

*ossia score* {{ site.score_version }}
{: .label .label-green}

The course is written to be read in order, although most visits start with a single question, such as how to receive MIDI from a controller or how to get video onto a projector. This page groups those questions by topic and links each one to the section of the lesson that answers it, so that you can arrive, read the section, and leave.

A lesson opened this way still assumes what the lessons before it taught. When a section uses a term you have not met, the **Before this lesson** box at the top of the page names the lesson that introduces it, and [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html) defines most of the vocabulary in one place.

This page is generated from `_data/topics.yml`, and every link on it is checked against the headings of the lesson it points at.

{% for topic in site.data.topics %}
## {{ topic.title }}
{: #{{ topic.id }} }

{{ topic.intro }}

{% for q in topic.questions -%}
{%- assign u = site.data.units | where_exp: "x", "x.num == q.unit" | first -%}
{%- capture label -%}{%- if u.kind == "milestone" -%}Milestone {{ u.num }}{%- elsif u.kind == "capstone" -%}Capstone{%- else -%}Lesson {{ u.num }}{%- endif -%}{%- endcapture -%}
- [{{ q.q }}]({{ site.baseurl }}/learn/{{ u.slug }}.html{% if q.anchor %}#{{ q.anchor }}{% endif %}) <small>{{ label }}{% for s in q.see %}{% assign su = site.data.units | where_exp: "x", "x.num == s" | first %}, see also [{% if su.kind == "milestone" %}Milestone {{ su.num }}{% elsif su.kind == "capstone" %}the capstone{% else %}Lesson {{ su.num }}{% endif %}]({{ site.baseurl }}/learn/{{ su.slug }}.html){% endfor %}</small>
{% endfor %}
{% endfor %}
