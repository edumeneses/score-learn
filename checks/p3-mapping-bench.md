# Re-verification note: p3-mapping-bench

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| p3-01 | The bench: one conditioned input, three branches, observation on each | **done**, docs/learn/assets/p3/p3-01-mapping-bench.png |

## Re-verify when the pinned version changes

- The joystick device, for readers using a gamepad as the input.
- That Alt+Drag still saves a fragment to the user library.
- Signal display behaviour as the observation process.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## The bench, and the shapes it teaches, 2026-08-18

Edu assembled the patch by hand; it is committed as `p3-bench.score` and the figure is
captured from it. The node positions were then shifted in the JSON rather than dragged,
which is the cheaper way to lay a patch out.

**The processes, with their uuids**, so a builder can emit this patch later:

| Process | ObjectName | uuid |
|---|---|---|
| LFO | `LFO` | `1e17e479-3513-44c8-a8a7-017be9f6ac8a` |
| Range Filter | `range_filter` | `db16b5fa-e6b0-4f89-8210-225384dbc677` |
| Smooth | `ValueFilter` | `bf603921-5a48-4aa5-9bc1-48a762be6467` |
| Multi-choice | `multi_choice` | `2c1d4578-7ef7-48b1-bbb8-c2b1c41063c9` |
| Signal display | `SignalDisplay` | `9906e563-ddeb-4ecd-908c-952baee2a0a5` |
| Value display | `Display` | `3f4a41f2-fa39-420f-ab0f-0af6b8409edb` |

Note that **`Smooth` is `ValueFilter` in the file**, and its `Type` inlet chooses between
`OneEuro`, `LowPass`, `Average`, and `Median`. `Multi-choice` takes its signal on inlet
**11000** (`In 0`), not on inlet 0, which is `Input count`.

**Cables are object paths**, and entirely generatable; the earlier note calling them
intractable was wrong. Each end is a list from the document root down to the port:

```json
{"ObjectName": "Process::Cable", "id": 1, "Type": 0,
 "Source": [{"ObjectName": "Scenario::ScenarioDocumentModel", "ObjectId": 1},
            {"ObjectName": "Scenario::BaseScenario", "ObjectId": 0},
            {"ObjectName": "Scenario::IntervalModel", "ObjectId": 0},
            {"ObjectName": "LFO", "ObjectId": 1},
            {"ObjectName": "Outlet", "ObjectId": 0}],
 "Sink":   [ ... same prefix ..., {"ObjectName": "range_filter", "ObjectId": 2},
            {"ObjectName": "Inlet", "ObjectId": 0}]}
```

The prefix is the path to whatever holds the processes. Here they sit directly on the root
interval, so there is no `Scenario` in it; a patch inside a scenario would have one.

`mkscore.py` has **not** been taught these yet: six process shapes with all their inlet
defaults is a large job, and the figure did not need it. The information above is what a
later session needs to do it.

## Known imperfection in the figure

The third branch's observation is blank while the other two are live, and it stays blank
however long the score plays. I did not chase the cause, and the lesson does not assert
one: it points at the blank display as an illustration of why the milestone asks for
observation on every stage. If a later session works out why `Multi-choice` reports nothing
here, correct the lesson and this note together.

## How p3-01 was captured, 2026-08-18

Open `p3-bench.score`, press play, then **pan the graph by dragging empty background**,
which is how a node clipped by the editor's left edge is brought into view. Shifting every
node's `Pos` in the JSON does nothing visible, because score keeps its own view scroll and
the whole graph moves with it; only a relative move or a pan changes what is on screen.
