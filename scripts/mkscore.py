#!/usr/bin/env python3
"""Build the lesson score files that the figures are captured from.

Score documents are JSON, so the course authors its example scores here rather
than by hand in the interface. Two reasons, both practical:

  1. a figure is reproducible: re-running this script and re-capturing gives the
     same image, which matters when the pinned score version changes;
  2. no synthetic input is needed, so figures can be captured on a machine whose
     session is locked, or over ssh with a display attached.

The temporal and nodal views are a property of the document (`Nodal` in the
racks), so the two views of one score are two files, not two interactions.

Usage:
    python3 scripts/mkscore.py 00        # writes library/learn/00-what-score-is/
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library" / "learn"

SEC = 705_600_000  # flicks per second, score's internal time unit

# Logical width of the scenario editor in the pinned capture format: a 3840 px
# fullscreen window at QT_SCALE_FACTOR=2, minus the two side panels.
EDITOR_WIDTH_PX = 950

SCENARIO_UUID = "de035912-5b03-49a8-bc4d-b2cba68e21d9"
AUTOMATION_UUID = "d2a67bd8-5d3f-404e-b6e9-e350cf2a833f"
CURVE_SEGMENT_UUID = "1e7cb83f-4e47-4b14-814d-2242a9c75991"
AUDIO_IN_UUID = "a1574bb0-cbd4-4c7d-9417-0c25cfd1187b"
AUDIO_OUT_UUID = "a1d97535-18ac-444a-8417-0cbc1692d897"
GAIN_UUID = "9a13fb32-269a-47bf-99a9-930188c1f19c"
AUTOMATION_OUT_UUID = "047e4cc2-4d99-4e8b-bf98-206018d02274"
AUTOMATION_CTRL_UUID = "af2b4fc3-aecb-4c15-a5aa-1c573a239925"
SOUND_UUID = "63174570-d608-44bf-a9cb-e6f5a11f73cc"
VIDEO_UUID = "32dc5341-7748-4c31-a226-82e6bd685744"
VIDEO_OUT_UUID = "f1c71046-b754-49a5-8e66-d01374773dfc"
WINDOW_PROTOCOL_UUID = "5a181207-7d40-4ad8-814e-879fcdf8cc31"

OSC_PROTOCOL_UUID = "9a42de4b-f6eb-4bca-9564-01b975f601b9"
PLUGIN_MIDI_UUID = "1f923578-08c3-49be-9ba9-69c144ee2e32"
PLUGIN_DEVICES_UUID = "6e610e1f-9de2-4c36-90dd-0ef570002a21"
PLUGIN_DATA_UUID = "05e72689-e02c-4c9d-a0bf-fe84c32d3d96"

DEVICE = "lesson"


def meta(name: str, label: str = "", color: str = "Transparent1") -> dict:
    return {
        "ScriptingName": name,
        "Comment": "",
        "Color": color,
        "Label": label,
        "Touched": True,
    }


def audio_inlet() -> dict:
    return {
        "uuid": AUDIO_IN_UUID,
        "ObjectName": "Inlet",
        "id": 0,
        "Hidden": False,
        "Custom": "Audio in",
        "Exposed": "audio in",
    }


def audio_outlet() -> dict:
    return {
        "uuid": AUDIO_OUT_UUID,
        "ObjectName": "Outlet",
        "id": 0,
        "Hidden": False,
        "Custom": "Audio out",
        "Exposed": "audio out",
        "GainInlet": {
            "uuid": GAIN_UUID,
            "ObjectName": "Inlet",
            "id": 10000,
            "Hidden": False,
            "Custom": "Gain",
            "Exposed": "gain",
            "Value": {},
            "Init": {},
            "Domain": {"Float": {"Min": 0.0, "Max": 1.0}},
        },
        "PanInlet": {
            "uuid": GAIN_UUID,
            "ObjectName": "Inlet",
            "id": 10001,
            "Hidden": False,
            "Custom": "Pan",
            "Exposed": "pan",
            "Value": {},
            "Init": {},
            "Domain": {},
        },
        "Gain": 1.0,
        "Pan": [1.0, 1.0],
        "Propagate": True,
    }


def automation(pid: int, address: str, duration: int, start: float, end: float,
               name: str, power: float = 1.0,
               segments: list[tuple[float, float, float, float, float]] | None = None) -> dict:
    """An automation process writing a float to `address`.

    `segments` overrides the single default segment with a list of
    (x0, y0, x1, y1, power) tuples, for curves that need a breakpoint.
    """
    return {
        "uuid": AUTOMATION_UUID,
        "ObjectName": "Automation",
        "id": pid,
        "Metadata": meta(name),
        "Duration": duration,
        "Height": 300.0,
        "StartOffset": 0,
        "LoopDuration": duration,
        "Pos": [40.0, 40.0],
        "Size": [200.0, 100.0],
        "Loops": False,
        "Outlet": {
            "uuid": AUTOMATION_OUT_UUID,
            "ObjectName": "Outlet",
            "id": 0,
            "Hidden": False,
            "Custom": "Out",
            "Exposed": "out",
            "Address": address,
            "MinInlet": {
                "uuid": AUTOMATION_CTRL_UUID,
                "ObjectName": "Inlet",
                "id": 0,
                "Hidden": False,
                "Custom": "Control",
                "Exposed": "control",
                "Value": {"Float": 0.0},
                "Init": {},
                "Domain": {},
            },
            "MaxInlet": {
                "uuid": AUTOMATION_CTRL_UUID,
                "ObjectName": "Inlet",
                "id": 1,
                "Hidden": False,
                "Custom": "Control",
                "Exposed": "control",
                "Value": {"Float": 1.0},
                "Init": {},
                "Domain": {},
            },
        },
        "Curve": {
            "ObjectName": "CurveModel",
            "id": 1000 + pid,
            "Segments": [
                {
                    "uuid": CURVE_SEGMENT_UUID,
                    "ObjectName": "CurveSegmentModel",
                    "id": index + 1,
                    "Previous": index if index else None,
                    "Following": index + 2 if index + 1 < len(segments or [1]) else None,
                    "Start": [seg[0], seg[1]],
                    "End": [seg[2], seg[3]],
                    "Power": seg[4],
                }
                for index, seg in enumerate(segments or [(0.0, start, 1.0119, end, power)])
            ],
        },
        "Tween": False,
    }


def sound(pid: int, filename: str, duration: int, name: str,
          loops: bool = True) -> dict:
    """A sound file player. `filename` is resolved against the project folder,
    which is what the <PROJECT>: prefix means, so the document travels."""
    return {
        "uuid": SOUND_UUID,
        "ObjectName": "Sound",
        "id": pid,
        "Metadata": meta(name),
        "Duration": duration,
        "Height": 300.0,
        "StartOffset": 0,
        "LoopDuration": duration,
        "Pos": [40.0, 40.0],
        "Size": [200.0, 100.0],
        "Loops": loops,
        "File": f"<PROJECT>:{filename}",
        "Outlet": audio_outlet(),
        "Stretch": 0,
        "Mode": 0,
        "Tempo": 120.0,
    }


def video(pid: int, filename: str, duration: int, name: str,
          loops: bool = True, to_window: bool = True) -> dict:
    """A video file player.

    Its outlet carries a texture. Addressing that outlet to `Window:/` is what
    puts the image on screen: no cable is needed, which is the same mechanism the
    shipped video example uses.
    """
    outlet = {
        "uuid": VIDEO_OUT_UUID,
        "ObjectName": "Outlet",
        "id": 0,
        "Hidden": False,
    }
    if to_window:
        outlet["Address"] = "Window:/"
    return {
        "uuid": VIDEO_UUID,
        "ObjectName": "VideoProcess",
        "id": pid,
        "Metadata": meta(name),
        "Duration": duration,
        "Height": 300.0,
        "StartOffset": 0,
        "LoopDuration": duration,
        "Pos": [40.0, 40.0],
        "Size": [200.0, 100.0],
        "Loops": loops,
        "Inlets": [],
        "Outlets": [outlet],
        "FilePath": f"<PROJECT>:{filename}",
        "Scale": 0,
        "Tempo": 120.0,
        "IgnoreTempo": False,
    }


def window_device() -> dict:
    """The Window device, read from score's own video example."""
    import json as _json
    import pathlib as _pathlib
    cached = _pathlib.Path("/tmp/windev.json")
    if cached.exists():
        return _json.loads(cached.read_text())
    return {
        "Device": {
            "Name": "Window",
            "Protocol": WINDOW_PROTOCOL_UUID,
            "Background": False,
        },
        "Children": [],
    }


def interval(iid: int, name: str, start_state: int, end_state: int,
             start_date: int, duration: int, processes: list[dict],
             *, height: float = 0.4, rigid: bool = True,
             max_duration: int | None = None, nodal: bool = False,
             label: str = "", fit: bool = False, max_inf: bool = False) -> dict:
    """One stretch of time, holding processes in its racks."""
    slots = [
        {"Processes": [p["id"]], "Process": p["id"], "Height": 140.0, "Nodal": nodal}
        for p in processes
    ]
    return {
        "ObjectName": "Scenario::IntervalModel",
        "id": iid,
        "Metadata": meta(name, label),
        "Inlet": audio_inlet(),
        "Outlet": audio_outlet(),
        "Processes": processes,
        "SmallViewRack": slots,
        "FullViewRack": [{"Process": p["id"], "Nodal": nodal} for p in processes],
        "DefaultDuration": duration,
        "MinDuration": duration,
        "MaxDuration": max_duration if max_duration is not None else duration,
        "GuiDuration": int(duration * 1.02),
        "Speed": 1.0,
        "Rigidity": rigid,
        "MinNull": False,
        # A document whose root has a bounded maximum stops when that maximum is
        # reached, however its contents are structured, so an endless inner loop
        # still ends. `max_inf` is what lets a loop actually run forever.
        "MaxInf": max_inf,
        "Signatures": [],
        "StartState": start_state,
        "EndState": end_state,
        "StartDate": start_date,
        "HeightPercentage": height,
        "NodalSlotHeight": 140.0,
        "QuantizationRate": -1.0,
        # Zoom is flicks per pixel. In practice score fits the document to the
        # editor's width on load regardless of this value, so it is written for
        # correctness rather than relied on; what matters for figures is that
        # the editor extends to about x=3225 in the capture format, which is
        # wider than it looks, so crops must not stop short of it.
        "Zoom": (duration / EDITOR_WIDTH_PX) if fit else -1.0,
        "Center": (duration // 2) if fit else 0,
        "ViewMode": 0,
        "SmallViewShown": True,
        "HasSignature": False,
    }


def timesync(tid: int, date: int, events: list[int], *, active: bool = False,
             label: str = "", start: bool = False, auto: bool = False) -> dict:
    """An instant. `active` is what makes it a trigger: it waits.

    `auto` is the interface's **start on play**, and `start` marks the instant as
    a place execution can begin. Out-of-time material needs all three together:
    a trigger, armed when the score starts, at an instant execution may enter,
    on a chain that nothing connects to the score's own beginning.
    """
    return {
        "ObjectName": "Scenario::TimeSyncModel",
        "id": tid,
        "Metadata": meta(f"Sync.{tid}", label, "Gray"),
        "Date": date,
        "Events": events,
        "MusicalSync": -1.0,
        "AutoTrigger": auto,
        "Start": start,
        "Active": active,
        "Expression": " { true == false } ",
    }


def transition(iid: int, start_state: int, end_state: int, date: int,
               *, height: float = 0.4, name: str = "") -> dict:
    """An instantaneous interval, which is what score calls a transition.

    Zero duration is the whole point: taking no time, it can join two states in
    either chronological direction, and a loop is simply one pointing backwards.
    `Graphal` is the flag that marks it as one.

    It carries none of an ordinary interval's machinery, no racks, no ports, no
    processes, because there is no time in which anything could run; writing
    those keys anyway is what made the first attempts here fail to load.
    """
    return {
        "ObjectName": "Scenario::IntervalModel",
        "id": iid,
        "Metadata": meta(name or f"Transition.{iid}"),
        "Graphal": True,
        "DefaultDuration": 0,
        "MinDuration": 0,
        "MaxDuration": 0,
        "GuiDuration": 0,
        "Speed": 1.0,
        "Rigidity": True,
        "MinNull": False,
        "MaxInf": False,
        "StartState": start_state,
        "EndState": end_state,
        "StartDate": date,
        "HeightPercentage": height,
    }


def event(eid: int, tnode: int, states: list[int], date: int,
          condition: str = "") -> dict:
    return {
        "ObjectName": "Scenario::EventModel",
        "id": eid,
        "Metadata": meta(f"Event.{eid}", "", "Emphasis4"),
        "TimeNode": tnode,
        "States": states,
        "Condition": condition,
        "Date": date,
        "Offset": 0,
    }


def message(path: str, value: float) -> dict:
    return {
        "Name": "",
        "Accessors": [],
        "Unit": "none",
        "Previous": [],
        "Following": [],
        "User": None,
        "Priorities": [1, 2, 0],
        "Children": [
            {
                "Name": DEVICE,
                "Accessors": [],
                "Unit": "none",
                "Previous": [],
                "Following": [],
                "User": None,
                "Priorities": [1, 2, 0],
                "Children": [
                    {
                        "Name": path,
                        "Accessors": [],
                        "Unit": "none",
                        "Previous": [],
                        "Following": [],
                        "User": {"Float": value},
                        "Priorities": [1, 2, 0],
                    }
                ],
            }
        ],
    }


def state(sid: int, eid: int, height: float, *, prev: int | None = None,
          nxt: int | None = None, messages: dict | None = None) -> dict:
    return {
        "ObjectName": "Scenario::StateModel",
        "id": sid,
        "Metadata": meta(f"State.{sid}", "", "Base1"),
        "Event": eid,
        "PreviousConstraint": prev,
        "NextConstraint": nxt,
        "HeightPercentage": height,
        "Messages": messages if messages is not None else {
            "Name": "",
            "Accessors": [],
            "Unit": "none",
            "Previous": [],
            "Following": [],
            "User": None,
            "Priorities": [1, 2, 0],
            "Children": [],
        },
        "Controls": [],
        "StateProcesses": [],
    }


def osc_device() -> dict:
    """One OSC device with the three parameters the lesson score writes to."""
    def param(name: str) -> dict:
        return {
            "Address": {
                "ioType": "<->",
                "ClipMode": "Free",
                "RepetitionFilter": False,
                "Value": {"Float": 0.0},
                "Domain": {"Float": {"Min": 0.0, "Max": 1.0}},
                "Name": name,
            }
        }

    return {
        "uuid": PLUGIN_DEVICES_UUID,
        "RootNode": {},
        "Children": [
            {
                "Device": {
                    "Name": DEVICE,
                    "Protocol": OSC_PROTOCOL_UUID,
                    "Config": {
                        "Mode": 1,
                        "Version": 0,
                        "Framing": 1,
                        "Bundle": 0,
                        "Transport": {
                            "UDP": {
                                "Local": {"Bind": "0.0.0.0", "Port": 9997},
                                "Remote": {
                                    "Host": "127.0.0.1",
                                    "Port": 9996,
                                    "Broadcast": False,
                                },
                            }
                        },
                    },
                },
                "Children": [param("level"), param("colour"), param("shutter"), param("haze")],
            }
        ],
    }


def lesson_00() -> dict:
    """The score Lesson 00 reads: nested intervals, an automation, states, a
    trigger, a condition, a branch, and an address written on a state.

    Layout in time:

        0s ........ 6s ................. 13s
        [ Approach ]--(trigger)--[ Bright ]        condition: level > 0.5
                              \\-[ Dark   ]        condition: level <= 0.5

    `Approach` holds a nested scenario, so the hierarchy is visible; the two
    outgoing intervals leave the same instant, which is what makes a linear
    reading of the document impossible.
    """
    # nested scenario inside the first interval: one interval of its own
    inner_auto = automation(20, f"{DEVICE}:/shutter", 3 * SEC, 0.1, 0.9, "Automation (float).20")
    inner = {
        "uuid": SCENARIO_UUID,
        "ObjectName": "Scenario",
        "id": 10,
        "Metadata": meta("Scenario.10"),
        "Duration": 6 * SEC,
        "Height": 420.0,
        "StartOffset": 0,
        "LoopDuration": 6 * SEC,
        "Pos": [40.0, 40.0],
        "Size": [200.0, 100.0],
        "Loops": False,
        "Inlet": audio_inlet(),
        "Outlet": audio_outlet(),
        "StartTimeNodeId": 100,
        "StartEventId": 100,
        "StartStateId": 100,
        "Exclusive": False,
        "TimeNodes": [
            timesync(100, 0, [100], start=True),
            timesync(101, 3 * SEC, [101]),
        ],
        "Events": [event(100, 100, [100], 0), event(101, 101, [101], 3 * SEC)],
        "States": [
            state(100, 100, 0.30, nxt=100),
            state(101, 101, 0.30, prev=100),
        ],
        "Constraints": [
            interval(100, "Shutter", 100, 101, 0, 3 * SEC, [inner_auto], height=0.30)
        ],
        "Comments": [],
    }

    approach = interval(
        1,
        "Approach",
        1,
        2,
        0,
        6 * SEC,
        [automation(2, f"{DEVICE}:/level", 6 * SEC, 0.0, 1.0, "Automation (float).2", 1.6), inner],
        height=0.16,
    )
    bright = interval(
        2,
        "Bright",
        3,
        5,
        6 * SEC,
        7 * SEC,
        [automation(3, f"{DEVICE}:/colour", 7 * SEC, 0.8, 0.2, "Automation (float).3")],
        height=0.10,
    )
    dark = interval(
        3,
        "Dark",
        4,
        6,
        6 * SEC,
        5 * SEC,
        [automation(4, f"{DEVICE}:/colour", 5 * SEC, 0.2, 0.05, "Automation (float).4")],
        height=0.46,
    )

    scenario = {
        "uuid": SCENARIO_UUID,
        "ObjectName": "Scenario",
        "id": 1,
        "Metadata": meta("Scenario.1"),
        "Duration": 14 * SEC,
        "Height": 900.0,
        "StartOffset": 0,
        "LoopDuration": 14 * SEC,
        "Pos": [40.0, 40.0],
        "Size": [200.0, 100.0],
        "Loops": False,
        "Inlet": audio_inlet(),
        "Outlet": audio_outlet(),
        "StartTimeNodeId": 0,
        "StartEventId": 0,
        "StartStateId": 0,
        "Exclusive": False,
        "TimeNodes": [
            timesync(0, 0, [0], start=True),
            # the trigger: three events share this instant, one arriving and two
            # leaving under conditions
            timesync(1, 6 * SEC, [1, 2, 3], active=True, label="waits for /lesson/go"),
            timesync(2, 13 * SEC, [4]),
            timesync(3, 11 * SEC, [5]),
        ],
        "Events": [
            event(0, 0, [1], 0),
            event(1, 1, [2], 6 * SEC),
            event(2, 1, [3], 6 * SEC, condition=f" {{ {DEVICE}:/level > 0.5 }} "),
            event(3, 1, [4], 6 * SEC, condition=f" {{ {DEVICE}:/level <= 0.5 }} "),
            event(4, 2, [5], 13 * SEC),
            event(5, 3, [6], 11 * SEC),
        ],
        "States": [
            state(1, 0, 0.16, nxt=1, messages=message("level", 0.0)),
            state(2, 1, 0.16, prev=1),
            state(3, 2, 0.10, nxt=2, messages=message("colour", 0.8)),
            state(4, 3, 0.46, nxt=3, messages=message("colour", 0.2)),
            state(5, 4, 0.10, prev=2),
            state(6, 5, 0.46, prev=3),
        ],
        "Constraints": [approach, bright, dark],
        "Comments": [],
    }

    root = interval(
        0,
        "lesson-00",
        0,
        1,
        0,
        14 * SEC,
        [scenario],
        height=0.5,
        rigid=False,
        max_duration=15 * SEC,
    )
    # the root interval of a document is bounded by the base scenario's states
    root["StartState"] = 0
    root["EndState"] = 1

    return {
        "Document": {
            "ObjectName": "Scenario::ScenarioDocumentModel",
            "id": 1,
            "BaseScenario": {
                "ObjectName": "Scenario::BaseScenario",
                "id": 0,
                "Constraint": root,
                "StartTimeNode": timesync(0, 0, [0], start=True),
                "EndTimeNode": timesync(1, 14 * SEC, [1]),
                "StartEvent": event(0, 0, [0], 0),
                "EndEvent": event(1, 1, [1], 14 * SEC),
                "StartState": state(0, 0, 0.5, nxt=0),
                "EndState": state(1, 1, 0.5, prev=0),
            },
            "Speed": 1.0,
            "Cables": [],
            "BusIntervals": [],
        },
        "Plugins": [
            {
                "uuid": PLUGIN_MIDI_UUID,
                "Refresh": False,
                "Reconnect": False,
                "MidiRatio": 1.0,
            },
            _devices(extra_devices),
            {"uuid": PLUGIN_DATA_UUID, "Data": ""},
        ],
        "Version": 4,
        "Commit": "",
        "Tag": "3.8.2",
    }


def to_nodal(doc: dict) -> dict:
    """Same document, with the intervals inside the scenario shown as graphs.

    The root interval keeps its temporal rack on purpose. Flipping the root too
    replaces the whole timeline with a single collapsed node, which teaches
    nothing; leaving it temporal shows what the reader needs to see, that the
    contents of a stretch of time are a dataflow graph.
    """
    out = copy.deepcopy(doc)
    root = out["Document"]["BaseScenario"]["Constraint"]

    def flip(node) -> None:
        if isinstance(node, dict):
            if "Nodal" in node:
                node["Nodal"] = True
            for value in node.values():
                flip(value)
        elif isinstance(node, list):
            for value in node:
                flip(value)

    # everything under the root's processes, but not the root's own racks
    for process in root.get("Processes", []):
        flip(process)
    return out


def document(root: dict, extra_devices: list | None = None,
             endless: bool = False) -> dict:
    """Wrap a root interval into a full score document.

    `endless` makes the base scenario's closing instant a **trigger**, with the
    never-true expression every sync already carries. Without it the document
    stops when that instant's date arrives, however its contents are structured,
    so a score whose inner loop should run forever still ends. This is the same
    idiom Lesson 17 describes for bounding a loop, used here to refuse to bound
    one: `MaxInf` on the root is necessary and, on its own, not sufficient.
    """
    return {
        "Document": {
            "ObjectName": "Scenario::ScenarioDocumentModel",
            "id": 1,
            "BaseScenario": {
                "ObjectName": "Scenario::BaseScenario",
                "id": 0,
                "Constraint": root,
                "StartTimeNode": timesync(0, 0, [0], start=True),
                "EndTimeNode": timesync(1, root["DefaultDuration"], [1],
                                        active=endless),
                "StartEvent": event(0, 0, [0], 0),
                "EndEvent": event(1, 1, [1], root["DefaultDuration"]),
                "StartState": state(0, 0, 0.5, nxt=0),
                "EndState": state(1, 1, 0.5, prev=0),
            },
            "Speed": 1.0,
            "Cables": [],
            "BusIntervals": [],
        },
        "Plugins": [
            {
                "uuid": PLUGIN_MIDI_UUID,
                "Refresh": False,
                "Reconnect": False,
                "MidiRatio": 1.0,
            },
            _devices(extra_devices),
            {"uuid": PLUGIN_DATA_UUID, "Data": ""},
        ],
        "Version": 4,
        "Commit": "",
        "Tag": "3.8.2",
    }


def _devices(extra: list | None) -> dict:
    """The device plugin entry: the lesson OSC device plus anything else asked for."""
    entry = osc_device()
    if extra:
        entry["Children"] = entry["Children"] + list(extra)
    return entry


def scenario(pid: int, duration: int, timenodes: list[dict], events: list[dict],
             states: list[dict], intervals: list[dict], *,
             height: float = 900.0) -> dict:
    return {
        "uuid": SCENARIO_UUID,
        "ObjectName": "Scenario",
        "id": pid,
        "Metadata": meta(f"Scenario.{pid}"),
        "Duration": duration,
        "Height": height,
        "StartOffset": 0,
        "LoopDuration": duration,
        "Pos": [40.0, 40.0],
        "Size": [200.0, 100.0],
        "Loops": False,
        "Inlet": audio_inlet(),
        "Outlet": audio_outlet(),
        "StartTimeNodeId": 0,
        "StartEventId": 0,
        "StartStateId": 0,
        "Exclusive": False,
        "TimeNodes": timenodes,
        "Events": events,
        "States": states,
        "Constraints": intervals,
        "Comments": [],
    }


def chain(spans: list[tuple[str, int, int, list[dict], float]],
          messages: dict[int, dict] | None = None) -> tuple[list, list, list, list]:
    """Build a straight chain of intervals, one after another.

    `spans` is a list of (name, start seconds, duration seconds, processes,
    height). Each interval gets its own start state; the last one closes the
    chain. `messages` optionally attaches cue messages to the state at index n.
    """
    messages = messages or {}
    timenodes: list[dict] = []
    events: list[dict] = []
    states: list[dict] = []
    intervals: list[dict] = []

    for index, (name, start, duration, processes, height) in enumerate(spans):
        date = start * SEC
        timenodes.append(timesync(index, date, [index], start=(index == 0)))
        events.append(event(index, index, [index], date))
        states.append(
            state(
                index,
                index,
                height,
                prev=index - 1 if index else None,
                nxt=index,
                messages=messages.get(index),
            )
        )
        intervals.append(
            interval(index, name, index, index + 1, date, duration * SEC,
                     processes, height=height)
        )

    last = len(spans)
    end_date = (spans[-1][1] + spans[-1][2]) * SEC
    timenodes.append(timesync(last, end_date, [last]))
    events.append(event(last, last, [last], end_date))
    states.append(
        state(last, last, spans[-1][4], prev=last - 1,
              messages=messages.get(last))
    )
    return timenodes, events, states, intervals


def lesson_04() -> dict:
    """One interval, one automation. The smallest useful score."""
    auto = automation(2, f"{DEVICE}:/level", 8 * SEC, 0.0, 1.0,
                      "Automation (float).2", 1.4)
    tn, ev, st, iv = chain([("Fade in", 0, 8, [auto], 0.34)])
    root = interval(0, "lesson-04", 0, 1, 0, 8 * SEC,
                    [scenario(1, 8 * SEC, tn, ev, st, iv, height=600.0)],
                    height=0.5, rigid=False)
    return document(root)


def p1_solution() -> dict:
    """The Milestone P1 reference solution: a sixty-second cue.

    Three automations in sequence, a preset state at the top, and a blackout
    state at the end, so the artefact both starts and ends in a known condition.
    """
    rise = automation(2, f"{DEVICE}:/level", 20 * SEC, 0.0, 1.0,
                      "Automation (float).2", 1.8)
    hold = automation(3, f"{DEVICE}:/colour", 20 * SEC, 0.15, 0.9,
                      "Automation (float).3")
    fall = automation(4, f"{DEVICE}:/level", 20 * SEC, 1.0, 0.0,
                     "Automation (float).4", 0.6)
    shutter = automation(5, f"{DEVICE}:/shutter", 20 * SEC, 0.2, 1.0,
                         "Automation (float).5")

    tn, ev, st, iv = chain(
        [
            ("Rise", 0, 20, [rise], 0.22),
            ("Hold", 20, 20, [hold, shutter], 0.22),
            ("Fall", 40, 20, [fall], 0.22),
        ],
        messages={
            0: message("level", 0.0),
            3: message("level", 0.0),
        },
    )
    root = interval(0, "p1-automated-cue", 0, 1, 0, 60 * SEC,
                    [scenario(1, 60 * SEC, tn, ev, st, iv)],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def lesson_09() -> dict:
    """Three cues and nothing else: states carry the messages, the intervals
    between them are empty, which is what a cue list looks like in score."""
    tn, ev, st, iv = chain(
        [
            ("Wait", 0, 6, [], 0.30),
            ("Wait", 6, 6, [], 0.30),
        ],
        messages={
            0: message("level", 0.0),
            1: message("level", 0.7),
            2: message("level", 0.25),
        },
    )
    root = interval(0, "lesson-09", 0, 1, 0, 12 * SEC,
                    [scenario(1, 12 * SEC, tn, ev, st, iv, height=600.0)],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def p2_solution() -> dict:
    """Milestone P2: one shape driving four channel groups at once.

    Uses an OSC device rather than Art-Net so that the document runs for readers
    with no receiver installed; the structure is what the milestone is about.
    """
    autos = [
        automation(2 + n, f"{DEVICE}:/{name}", 20 * SEC, 0.05, 0.95,
                   f"Automation (float).{2 + n}", 1.7)
        for n, name in enumerate(("level", "colour", "shutter", "haze"))
    ]
    tn, ev, st, iv = chain([("Wash", 0, 20, autos, 0.16)],
                           messages={0: message("level", 0.0),
                                     1: message("level", 0.0)})
    root = interval(0, "p2-light-wash", 0, 1, 0, 20 * SEC,
                    [scenario(1, 20 * SEC, tn, ev, st, iv)],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def lesson_10() -> dict:
    """Four curve shapes, same start, same end, same duration."""
    shapes = [
        ("Linear", automation(2, f"{DEVICE}:/level", 3 * SEC, 0.05, 0.95,
                              "Automation (float).2", 1.0)),
        ("Accelerating", automation(3, f"{DEVICE}:/level", 3 * SEC, 0.05, 0.95,
                                    "Automation (float).3", 3.0)),
        ("Decelerating", automation(4, f"{DEVICE}:/level", 3 * SEC, 0.05, 0.95,
                                    "Automation (float).4", 0.33)),
        ("Hold", automation(5, f"{DEVICE}:/level", 3 * SEC, 0.0, 0.0,
                            "Automation (float).5", 1.0,
                            segments=[(0.0, 0.0, 0.35, 0.6, 0.6),
                                      (0.35, 0.6, 0.65, 0.6, 1.0),
                                      (0.65, 0.6, 1.0, 1.0, 2.4)])),
    ]
    # all four at the same height, so they chain in one row and the shapes can be
    # compared directly; staircasing them makes the curves too small to read
    spans = [(name, i * 3, 3, [auto], 0.30)
             for i, (name, auto) in enumerate(shapes)]
    tn, ev, st, iv = chain(spans)
    root = interval(0, "lesson-10", 0, 1, 0, 12 * SEC,
                    [scenario(1, 12 * SEC, tn, ev, st, iv)],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def lesson_15() -> dict:
    """An interval that waits: elastic duration, then a trigger."""
    approach = automation(2, f"{DEVICE}:/level", 5 * SEC, 0.0, 1.0,
                          "Automation (float).2", 1.5)
    after = automation(3, f"{DEVICE}:/colour", 4 * SEC, 0.9, 0.1,
                       "Automation (float).3")

    scen = scenario(
        1, 9 * SEC,
        [timesync(0, 0, [0], start=True),
         timesync(1, 5 * SEC, [1], active=True, label="waits for /lesson/go"),
         timesync(2, 9 * SEC, [2])],
        [event(0, 0, [0], 0), event(1, 1, [1], 5 * SEC), event(2, 2, [2], 9 * SEC)],
        [state(0, 0, 0.22, nxt=0, messages=message("level", 0.0)),
         state(1, 1, 0.22, prev=0, nxt=1),
         state(2, 2, 0.22, prev=1)],
        # the first interval is elastic, which is what score draws dashed
        [interval(0, "Approach", 0, 1, 0, 5 * SEC, [approach], height=0.22,
                  rigid=False, max_duration=8 * SEC),
         interval(1, "After", 1, 2, 5 * SEC, 4 * SEC, [after], height=0.22)],
    )
    root = interval(0, "lesson-15", 0, 1, 0, 9 * SEC, [scen],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def lesson_16() -> dict:
    """One instant, two conditional branches, and a layer that always runs."""
    intro = automation(2, f"{DEVICE}:/level", 4 * SEC, 0.0, 1.0,
                       "Automation (float).2", 1.6)
    high = automation(3, f"{DEVICE}:/colour", 6 * SEC, 0.9, 0.2,
                      "Automation (float).3")
    low = automation(4, f"{DEVICE}:/colour", 6 * SEC, 0.2, 0.05,
                     "Automation (float).4")
    layer = automation(5, f"{DEVICE}:/haze", 6 * SEC, 0.1, 0.5,
                       "Automation (float).5")

    scen = scenario(
        1, 10 * SEC,
        [timesync(0, 0, [0], start=True),
         timesync(1, 4 * SEC, [1, 2, 3, 4]),
         timesync(2, 10 * SEC, [5]),
         timesync(3, 10 * SEC, [6]),
         timesync(4, 10 * SEC, [7])],
        [event(0, 0, [0], 0),
         event(1, 1, [1], 4 * SEC),
         event(2, 1, [2], 4 * SEC, condition=f" {{ {DEVICE}:/level >= 0.5 }} "),
         event(3, 1, [3], 4 * SEC, condition=f" {{ {DEVICE}:/level < 0.5 }} "),
         event(4, 1, [4], 4 * SEC),
         event(5, 2, [5], 10 * SEC),
         event(6, 3, [6], 10 * SEC),
         event(7, 4, [7], 10 * SEC)],
        [state(0, 0, 0.14, nxt=0, messages=message("level", 0.0)),
         state(1, 1, 0.14, prev=0),
         state(2, 2, 0.30, nxt=1, messages=message("colour", 0.9)),
         state(3, 3, 0.52, nxt=2, messages=message("colour", 0.2)),
         state(4, 4, 0.74, nxt=3),
         state(5, 5, 0.30, prev=1),
         state(6, 6, 0.52, prev=2),
         state(7, 7, 0.74, prev=3)],
        [interval(0, "Approach", 0, 1, 0, 4 * SEC, [intro], height=0.14),
         interval(1, "High", 2, 5, 4 * SEC, 6 * SEC, [high], height=0.30),
         interval(2, "Low", 3, 6, 4 * SEC, 6 * SEC, [low], height=0.52),
         interval(3, "Layer (always)", 4, 7, 4 * SEC, 6 * SEC, [layer], height=0.74)],
    )
    root = interval(0, "lesson-16", 0, 1, 0, 10 * SEC, [scen],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def lesson_17() -> dict:
    """A loop made with a transition, and material that lives outside the timeline.

    Two structures side by side, because the lesson's point is that they are the
    same mechanism seen twice:

        0s ---[ Intro ]--- 3s ---[ Phrase ]--- 9s
                            ^                   |
                            \\--- transition ---/     loops the phrase forever

              (nothing connects this to the start)
                           4s ---[ On demand ]--- 8s
                            ^
                            trigger, armed on play

    The loop returns to the *second* instant rather than the first, so the intro
    plays once and the phrase repeats, which is easier to read in a figure than a
    loop over everything.

    The out-of-time chain is out of time for one reason only: no interval joins it
    to the instant the score starts from. Its own instant carries a trigger with
    start on play, which is what makes it fireable while the rest runs.
    """
    intro = automation(10, f"{DEVICE}:/level", 3 * SEC, 0.0, 1.0,
                       "Automation (float).10", 1.5)
    phrase = automation(11, f"{DEVICE}:/colour", 6 * SEC, 0.9, 0.1,
                        "Automation (float).11")
    onwards = automation(12, f"{DEVICE}:/haze", 4 * SEC, 0.1, 0.8,
                         "Automation (float).12")

    scen = scenario(
        1, 14 * SEC,
        [
            timesync(0, 0, [0], start=True),
            timesync(1, 3 * SEC, [1]),
            timesync(2, 9 * SEC, [2]),
            # the out-of-time chain begins here: a trigger, armed on play, at an
            # instant execution is allowed to start from
            timesync(3, 4 * SEC, [3], active=True, auto=True, start=True,
                     label="fires on demand"),
            timesync(4, 8 * SEC, [4]),
        ],
        [
            event(0, 0, [0], 0),
            event(1, 1, [1, 4], 3 * SEC),
            event(2, 2, [2, 3], 9 * SEC),
            event(3, 3, [5], 4 * SEC),
            event(4, 4, [6], 8 * SEC),
        ],
        [
            state(0, 0, 0.20, nxt=0, messages=message("level", 0.0)),
            state(1, 1, 0.20, prev=0, nxt=1),
            state(2, 2, 0.20, prev=1),
            # the two ends of the transition: it leaves the later instant and
            # arrives at the earlier one
            state(3, 2, 0.30, nxt=3),
            state(4, 1, 0.30, prev=3),
            state(5, 3, 0.62, nxt=2),
            state(6, 4, 0.62, prev=2),
        ],
        [
            interval(0, "Intro", 0, 1, 0, 3 * SEC, [intro], height=0.20),
            interval(1, "Phrase", 1, 2, 3 * SEC, 6 * SEC, [phrase], height=0.20),
            interval(2, "On demand", 5, 6, 4 * SEC, 4 * SEC, [onwards],
                     height=0.62),
            transition(3, 3, 4, 9 * SEC, height=0.30, name="Loop"),
        ],
    )
    root = interval(0, "lesson-17", 0, 1, 0, 14 * SEC, [scen],
                    height=0.5, rigid=False, fit=True, max_inf=True)
    return document(root, endless=True)


def p4_solution() -> dict:
    """Milestone P4: an installation that idles, reacts, and returns to idle.

        0s --[ Idle ]-- 4s --(visitor)--+-- level > 0.5 --[ Bright ]-- 10s --+
             ^                          |                                    |
             |                          +-- level <= 0.5 --[ Quiet ]-- 8s ---+
             |                                                               |
             +---------------- return transitions ---------------------------+

    The trigger and the conditions are two mechanisms doing two jobs, which is
    the distinction Lesson 16 insisted on: the visitor's arrival *releases* the
    instant, and the conditions *choose* which branch leaves it.

    Both branches return to the score's first instant, so the idle phrase plays
    again and the piece repeats indefinitely. The two outcomes are deliberately
    different lengths, because a return path that only works when both branches
    are the same duration is not a return path.
    """
    idle = automation(20, f"{DEVICE}:/haze", 4 * SEC, 0.1, 0.25,
                      "Automation (float).20")
    bright = automation(21, f"{DEVICE}:/level", 6 * SEC, 0.2, 1.0,
                        "Automation (float).21", 1.7)
    quiet = automation(22, f"{DEVICE}:/colour", 4 * SEC, 0.6, 0.05,
                       "Automation (float).22", 0.6)

    scen = scenario(
        1, 14 * SEC,
        [
            timesync(0, 0, [0], start=True),
            timesync(1, 4 * SEC, [1, 2, 3], active=True,
                     label="a visitor arrives"),
            timesync(2, 10 * SEC, [4]),
            timesync(3, 8 * SEC, [5]),
        ],
        [
            # the first instant also receives both return transitions
            event(0, 0, [0, 8, 9], 0),
            event(1, 1, [1], 4 * SEC),
            event(2, 1, [2], 4 * SEC,
                  condition=f" {{ {DEVICE}:/level > 0.5 }} "),
            event(3, 1, [3], 4 * SEC,
                  condition=f" {{ {DEVICE}:/level <= 0.5 }} "),
            event(4, 2, [4, 6], 10 * SEC),
            event(5, 3, [5, 7], 8 * SEC),
        ],
        [
            state(0, 0, 0.15, nxt=0, messages=message("haze", 0.1)),
            state(1, 1, 0.15, prev=0),
            state(2, 2, 0.35, nxt=1, messages=message("level", 0.2)),
            state(3, 3, 0.60, nxt=2, messages=message("colour", 0.6)),
            state(4, 4, 0.35, prev=1),
            state(5, 5, 0.60, prev=2),
            # each branch's end departs on a transition back to the beginning
            state(6, 4, 0.45, nxt=3),
            state(7, 5, 0.70, nxt=4),
            state(8, 0, 0.45, prev=3),
            state(9, 0, 0.70, prev=4),
        ],
        [
            interval(0, "Idle", 0, 1, 0, 4 * SEC, [idle], height=0.15),
            interval(1, "Bright", 2, 4, 4 * SEC, 6 * SEC, [bright], height=0.35),
            interval(2, "Quiet", 3, 5, 4 * SEC, 4 * SEC, [quiet], height=0.60),
            transition(3, 6, 8, 10 * SEC, height=0.45, name="Return (bright)"),
            transition(4, 7, 9, 8 * SEC, height=0.70, name="Return (quiet)"),
        ],
    )
    root = interval(0, "p4-interactive-installation", 0, 1, 0, 14 * SEC, [scen],
                    height=0.5, rigid=False, fit=True, max_inf=True)
    return document(root, endless=True)


def lesson_20() -> dict:
    """Two sound files: one played once, one looping to fill its interval.

    The excerpts come from the Citizen DJ packages, which are freely usable and
    installable through the package manager, so the document ships complete.
    """
    once = sound(2, "excerpt-ghosts.wav", 8 * SEC, "Sound.2", loops=False)
    looped = sound(3, "excerpt-rocking-chair.wav", 8 * SEC, "Sound.3", loops=True)
    tn, ev, st, iv = chain([
        ("Plays once", 0, 8, [once], 0.22),
        ("Loops to fill", 8, 8, [looped], 0.22),
    ])
    root = interval(0, "lesson-20", 0, 1, 0, 16 * SEC,
                    [scenario(1, 16 * SEC, tn, ev, st, iv)],
                    height=0.5, rigid=False, fit=True)
    return document(root)


def lesson_25() -> dict:
    """Two video sources, both addressed to the window device.

    The clips are generated with ffmpeg and committed, so no camera and no
    downloaded material are needed; the commands are printed in the lesson.
    """
    bars = video(2, "mock-bars.mp4", 8 * SEC, "Video.2")
    second = video(3, "mock-second.avi", 8 * SEC, "Video.3")
    tn, ev, st, iv = chain([
        ("H.264 source", 0, 8, [bars], 0.22),
        ("MJPEG source", 8, 8, [second], 0.22),
    ])
    root = interval(0, "lesson-25", 0, 1, 0, 16 * SEC,
                    [scenario(1, 16 * SEC, tn, ev, st, iv)],
                    height=0.5, rigid=False, fit=True)
    return document(root, extra_devices=[window_device()])


BUILDERS = {
    "00": ("00-what-score-is", lesson_00),
    "04": ("04-first-process", lesson_04),
    "P1": ("p1-automated-cue", p1_solution),
    "09": ("09-states-snapshots-presets", lesson_09),
    "P2": ("p2-light-wash", p2_solution),
    "10": ("10-automation-curves", lesson_10),
    "15": ("15-triggers", lesson_15),
    "16": ("16-conditions-and-branching", lesson_16),
    "17": ("17-loops-and-out-of-time", lesson_17),
    "P4": ("p4-interactive-installation", p4_solution),
    "20": ("20-sound-files", lesson_20),
    "25": ("25-video-pipeline", lesson_25),
}


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "00"
    if which not in BUILDERS:
        print(f"unknown lesson {which!r}; known: {', '.join(BUILDERS)}")
        return 1
    slug, builder = BUILDERS[which]
    out_dir = LIBRARY / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = builder()
    stem = {"P1": "p1-solution", "P2": "p2-solution",
            "P4": "p4-solution"}.get(which, f"lesson-{which}")
    temporal = out_dir / f"{stem}.score"
    temporal.write_text(json.dumps(doc, indent=1), encoding="utf8")
    print(f"wrote {temporal.relative_to(ROOT)}")
    if which == "00":
        # only Lesson 00 needs the second view; see checks/00-what-score-is.md
        nodal = out_dir / f"{stem}-nodal.score"
        nodal.write_text(json.dumps(to_nodal(doc), indent=1), encoding="utf8")
        print(f"wrote {nodal.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
