---
layout: default
title: Find by topic
description: "The course as a knowledge base: common questions about score, grouped by topic, each linked to the section of the lesson that answers it."
nav_order: 1
permalink: /topics
---

# Find by topic

*ossia score* {{ site.score_version }}
{: .label .label-green}

The course is written to be read in order, although most visits start with a single question, such as how to receive MIDI from a controller or how to get video onto a projector. This page groups those questions by topic and links each one to the section of the lesson that answers it, so that you can arrive, read the section, and leave.

A lesson opened this way still assumes what the lessons before it taught. When a section uses a term you have not met, the **Before this lesson** box at the top of the page names the lesson that introduces it, and [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html) defines most of the vocabulary in one place.

Every keyboard shortcut is also on one page, the [Shortcut cheatsheet]({{ site.baseurl }}/shortcuts). This page is generated from `_data/topics.yml`, and every link on it is checked against the headings of the lesson it points at.

The field below searches these questions only, as you type, whereas the search at the top of the page covers the whole course; `Enter` opens the first question that matches.

<div class="topics-filter">
  <input type="search" id="topics-filter" placeholder="Search the questions, for example: MIDI, loop, projector" aria-label="Search the questions on this page" aria-describedby="topics-filter-status" autocomplete="off">
  <p class="topics-filter-status" id="topics-filter-status" aria-live="polite"></p>
</div>

{% for topic in site.data.topics %}
<div class="topic-group" markdown="1">

## {{ topic.title }}
{: #{{ topic.id }} }

{{ topic.intro }}

{% for q in topic.questions -%}
{%- assign u = site.data.units | where_exp: "x", "x.num == q.unit" | first -%}
{%- capture label -%}{%- if u.kind == "milestone" -%}Milestone {{ u.num }}{%- elsif u.kind == "capstone" -%}Final project{%- else -%}Lesson {{ u.num }}{%- endif -%}{%- endcapture -%}
- [{{ q.q }}]({{ site.baseurl }}/learn/{{ u.slug }}.html{% if q.anchor %}#{{ q.anchor }}{% endif %}) <small>{{ label }}{% for s in q.see %}{% assign su = site.data.units | where_exp: "x", "x.num == s" | first %}, see also [{% if su.kind == "milestone" %}Milestone {{ su.num }}{% elsif su.kind == "capstone" %}the capstone{% else %}Lesson {{ su.num }}{% endif %}]({{ site.baseurl }}/learn/{{ su.slug }}.html){% endfor %}</small>
{% endfor %}

</div>
{% endfor %}

<script>
(function () {
  var input = document.getElementById("topics-filter");
  var status = document.getElementById("topics-filter-status");
  if (!input || !status) return;

  // Lowercase, drop accents, and keep letters, digits, and "+" (for Ctrl+Z and the like).
  function norm(s) {
    return s.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
      .toLowerCase().replace(/[^a-z0-9+]+/g, " ").trim();
  }

  // "loops" should find "loop", and "entries" should find "entry".
  function forms(word) {
    var out = [word];
    if (word.length > 4 && /ies$/.test(word)) out.push(word.slice(0, -3) + "y");
    if (word.length > 3 && /s$/.test(word)) out.push(word.slice(0, -1));
    return out;
  }

  var groups = Array.prototype.slice.call(document.querySelectorAll(".topic-group"));
  var items = [];
  groups.forEach(function (group) {
    var title = norm(group.querySelector("h2").textContent);
    group.querySelectorAll("li").forEach(function (li) {
      items.push({ li: li, group: group, own: " " + norm(li.textContent) + " ", title: " " + title + " " });
    });
  });

  function apply() {
    var query = norm(input.value);
    var words = query ? query.split(" ") : [];
    var shown = 0;
    var first = null;
    function matches(text) {
      return words.every(function (w) {
        return forms(w).some(function (f) { return text.indexOf(f) >= 0; });
      });
    }
    // A question matches on its own words and lesson; the topic's title only counts
    // when no question does, so that "loop" lists loops and not every trigger question.
    var own = items.some(function (item) { return matches(item.own); });
    groups.forEach(function (group) { group.dataset.hits = "0"; });
    items.forEach(function (item) {
      var hit = matches(own ? item.own : item.own + item.title);
      item.li.style.display = hit ? "" : "none";
      if (hit) {
        shown++;
        item.group.dataset.hits = String(Number(item.group.dataset.hits) + 1);
        if (!first) first = item.li.querySelector("a");
      }
    });
    groups.forEach(function (group) {
      group.style.display = words.length && group.dataset.hits === "0" ? "none" : "";
    });
    if (!words.length) status.textContent = "";
    else if (shown) status.textContent = shown + (shown === 1 ? " question" : " questions") + " of " + items.length + " match.";
    else status.textContent = "No question on this page matches; the search at the top of the page covers the whole course.";
    input.firstMatch = first;

    var url = new URL(window.location.href);
    if (input.value.trim()) url.searchParams.set("q", input.value.trim());
    else url.searchParams.delete("q");
    window.history.replaceState(null, "", url);
  }

  input.addEventListener("input", apply);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && input.firstMatch) {
      e.preventDefault();
      window.location.href = input.firstMatch.href;
    } else if (e.key === "Escape" && input.value) {
      input.value = "";
      apply();
    }
  });

  var initial = new URL(window.location.href).searchParams.get("q");
  if (initial) {
    input.value = initial;
    apply();
  }
})();
</script>
