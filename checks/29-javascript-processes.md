# Re-verification note: 29-javascript-processes

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 29-01 | The script editor and the console panel | **done**, docs/learn/assets/29/29-01-script-editor-and-console.png |

See `checks/FIGURES-PENDING.md` for the consolidated list.

## Re-verify when the pinned version changes

- The Score API calls named: find, createProcess, automate, setCurvePoints, setSteps, createIntervalAfter, startMacro/endMacro, inlets/inlet, valueType, min/max, enumValues, setValue, outlet, setAddress, endState.
- That .js files in the user library run in the global context when double-clicked.
- The module form that registers actions in the Scripts menu, including the actions array and ActionContext.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Grounded by the figure, 2026-08-11

- **`Ctrl+Shift+C` opens the console**, as the lesson says. The panel list under
  `View > Windows` confirms the whole set and their shortcuts: `Device Explorer`
  `Ctrl+Shift+D`, `Processes` `Ctrl+Shift+P`, `User Library` `Ctrl+Shift+B`, `Project
  folder` `Ctrl+Shift+L`, `History` `Ctrl+Shift+H`, `Audio` `Ctrl+Shift+M`, `Message log`
  `Ctrl+Shift+G`, `Sync` `Ctrl+G`, `Console` `Ctrl+Shift+C`. There is **no Inspector entry**:
  the inspector is the lower half of the right dock and appears when something is selected.
- **The console is a JavaScript ES7 environment**, which is what it prints on opening,
  along with a link to `https://ossia.io/score-docs/panels/console.html`. `2+2` returns `4`.
- **The script editor is a separate top-level window**, 1600x1600 as it opens, with
  `Execution` and `GUI` tabs, a log pane, and `Clear log`, `Close`, and `Compile` buttons.
  It is opened from a button on the process header and from the same button in the
  inspector.
- **Declared ports become real ports.** The shipped `average` example declares
  `ValueInlet { id: in1 }`, `ValueOutlet { id: out1 }`, and
  `IntSlider { id: range; min: 1; max: 100000; objectName: "milliseconds" }`, and the
  inspector then lists an input, a `milliseconds` control, and an output. The node in the
  score shows `Value In`, `milliseconds`, and `Value Out`.
- **`property var avg: []` is how state is kept between ticks**, and
  `tick: function(token, state)` is the tick signature. Both are as the lesson describes.

## How 29-01 was captured, 2026-08-11

On `lesson-04.score`, whose single interval gives the process somewhere to live.

1. Select the interval, filter the process library to `javascript`, and double-click
   `Script > Javascript > average`.
2. Click the editor button on the node header. The editor opens as its own window.
3. `Ctrl+Shift+C` for the console, then click its input line and evaluate `2+2`.
4. Move the editor window up so it stops covering the console. `capture.py` has no command
   for this; the four lines that do it are in the commit message, using
   `capture.window_list` plus `win.configure`.
5. Select the process in the right dock's object tree, so the inspector shows its ports
   rather than the interval's properties. The node itself is behind the editor window.

**The process library's filter lags badly.** Typing `javascript` looked like it had dropped
every character after the first; in fact the keystrokes were queued behind the tree rebuild
and arrived seconds later, so a retry produced `javascriptavascript`. Wait several seconds
after typing before deciding a search failed.
