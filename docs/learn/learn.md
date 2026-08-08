---
layout: default
title: Lessons
nav_order: 1
has_children: true
permalink: /learn
---

# The course

*ossia score* {{ site.score_version }}
{: .label .label-green}

Forty-seven units in twelve modules, followed by a capstone. Lessons carry a permanent number: new material takes a new number or a Part II, so that a link, a bookmark, or a video description never points at the wrong lesson.

Work through the modules in order. A *Make it work* milestone at the end of a cluster uses only what the preceding lessons introduced, so if a milestone is unclear, the gap is in a lesson you can name.

Units without a link are planned but not yet written. This table is generated from `_data/units.yml`, which is the single source of truth for the numbering and for the published addresses.

{% assign phase_titles = "Phase 1: authoring interactive scores|Phase 2: media|Phase 3: scripting, deployment, and contribution" | split: "|" %}
{% assign phase_notes = "A reader who finishes Phase 1 can build and install an interactive work. This is the minimum coherent course.|Audio, MIDI and musical time, video and graphics. Nothing here requires hardware beyond the computer.|Putting your own code inside a score, deploying it, and contributing upstream.|" | split: "|" %}
{% for phase in (1..3) %}
## {{ phase_titles[forloop.index0] }}

{{ phase_notes[forloop.index0] }}

| # | Unit | Read | Practice |
|---|---|---|---|
{%- for module in site.data.modules -%}
{%- if module.phase == phase %}
| **{{ module.id }}** | **{{ module.title }}** | | |
{%- for unit in site.data.units -%}
{%- if unit.module == module.id %}
| {{ unit.num }} | {% if unit.written %}[{{ unit.title }}]({{ site.baseurl }}/learn/{{ unit.slug }}.html){% else %}{{ unit.title }}{% endif %} | {{ unit.read }} min | {% if unit.practice > 0 %}{{ unit.practice }} min{% else %}none{% endif %} |
{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- endfor %}
{% endfor %}

## Reading budgets

The read column is the page's own budget, capped at fifteen minutes by design. The practice column is separate and deliberate: a twelve minute read can carry half an hour at the keyboard, and a lesson that hides that under a single number misleads whoever is planning a workshop around it.

Totals: {% assign total_read = 0 %}{% assign total_practice = 0 %}{% for unit in site.data.units %}{% assign total_read = total_read | plus: unit.read %}{% assign total_practice = total_practice | plus: unit.practice %}{% endfor %}{{ total_read }} minutes of reading and {{ total_practice }} minutes of practice across {{ site.data.units | size }} units.
