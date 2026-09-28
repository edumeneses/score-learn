---
layout: default
title: Shortcut cheatsheet
description: "Every keyboard shortcut and mouse gesture of ossia score, grouped by what they act on, on one page."
nav_order: 2
permalink: /shortcuts
---

# Shortcut cheatsheet

*ossia score* {{ site.score_version }}
{: .label .label-green}

Every shortcut and mouse gesture the course knows of, grouped by what it acts on. The menu entries were read from *score* {{ site.score_version }} itself, and the rest link to the lesson that uses them. On macOS, `Ctrl` is the `⌘` key.

<div class="cheatsheet-filter">
  <input type="search" id="cheatsheet-filter" placeholder="Filter, for example: zoom, trigger, Ctrl+Shift" aria-label="Filter shortcuts">
</div>

<div class="cheatsheet" markdown="0">
{%- for group in site.data.shortcuts %}
  <section class="cheatsheet-card">
    <h2>{{ group.title }}</h2>
    {%- if group.intro %}<p class="cheatsheet-intro">{{ group.intro }}</p>{% endif %}
    <div class="cheatsheet-rows">
    {%- for item in group.items %}
      <div class="cheatsheet-row">
        <span class="cheatsheet-keys">
        {%- if item.keys -%}
          {%- assign alts = item.keys | split: " / " -%}
          {%- for alt in alts -%}
            {%- assign keys = alt | split: "+" -%}
            {%- for k in keys -%}
              {%- assign shown = k | replace: "Left", "←" | replace: "Right", "→" | replace: "Up", "↑" | replace: "Down", "↓" -%}
              <kbd>{{ shown }}</kbd>{% unless forloop.last %}<span class="cheatsheet-plus">+</span>{% endunless %}
            {%- endfor -%}
            {%- unless forloop.last %}<span class="cheatsheet-or">or</span>{% endunless -%}
          {%- endfor -%}
        {%- else -%}
          <span class="cheatsheet-mouse">{{ item.mouse }}</span>
        {%- endif -%}
        </span>
        <span class="cheatsheet-action">{{ item.action }}
        {%- if item.see -%}
          {%- assign u = site.data.units | where_exp: "x", "x.num == item.see" | first -%}
          {%- if u %} <a class="cheatsheet-see" href="{{ site.baseurl }}/learn/{{ u.slug }}.html">L{{ u.num }}</a>{% endif -%}
        {%- endif -%}
        {%- if item.src == "docs" %} <span class="cheatsheet-docs" title="From upstream's reference page; not yet checked in this build">†</span>{% endif -%}
        </span>
      </div>
    {%- endfor %}
    </div>
  </section>
{%- endfor %}
</div>

<p class="cheatsheet-note">† From <a href="{{ site.docs_baseurl }}/reference/shortcuts.html">upstream's shortcut reference</a>, not yet checked in {{ site.score_version }}; arrow keys act on whichever part of the window has keyboard focus. The two uses of <code>Ctrl+R</code> depend on what is selected: a device refreshes its namespace, a state refreshes its stored values.</p>

<script>
(function () {
  var input = document.getElementById("cheatsheet-filter");
  if (!input) return;
  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    document.querySelectorAll(".cheatsheet-card").forEach(function (card) {
      var shown = 0;
      var title = card.querySelector("h2").textContent.toLowerCase();
      card.querySelectorAll(".cheatsheet-row").forEach(function (row) {
        var text = (row.textContent.replace(/\s+/g, "") + " " + row.textContent).toLowerCase();
        var hit = !q || text.indexOf(q.replace(/\s+/g, "")) >= 0 || text.indexOf(q) >= 0 || title.indexOf(q) >= 0;
        row.style.display = hit ? "" : "none";
        if (hit) shown++;
      });
      card.style.display = shown ? "" : "none";
    });
  });
})();
</script>
