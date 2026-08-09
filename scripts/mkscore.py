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

SCENARIO_UUID = "de035912-5b03-49a8-bc4d-b2cba68e21d9"
AUTOMATION_UUID = "d2a67bd8-5d3f-404e-b6e9-e350cf2a833f"
CURVE_SEGMENT_UUID = "1e7cb83f-4e47-4b14-814d-2242a9c75991"
AUDIO_IN_UUID = "a1574bb0-cbd4-4c7d-9417-0c25cfd1187b"
AUDIO_OUT_UUID = "a1d97535-18ac-444a-8417-0cbc1692d897"
GAIN_UUID = "9a13fb32-269a-47bf-99a9-930188c1f19c"
AUTOMATION_OUT_UUID = "047e4cc2-4d99-4e8b-bf98-206018d02274"
AUTOMATION_CTRL_UUID = "af2b4fc3-aecb-4c15-a5aa-1c573a239925"

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
               name: str, power: float = 1.0) -> dict:
    """An automation process writing a float to `address`."""
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
                    "id": 1,
                    "Previous": None,
                    "Following": None,
                    "Start": [0.0, start],
                    "End": [1.0, end],
                    "Power": power,
                }
            ],
        },
        "Tween": False,
    }


def interval(iid: int, name: str, start_state: int, end_state: int,
             start_date: int, duration: int, processes: list[dict],
             *, height: float = 0.4, rigid: bool = True,
             max_duration: int | None = None, nodal: bool = False,
             label: str = "") -> dict:
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
        "MaxInf": False,
        "Signatures": [],
        "StartState": start_state,
        "EndState": end_state,
        "StartDate": start_date,
        "HeightPercentage": height,
        "NodalSlotHeight": 140.0,
        "QuantizationRate": -1.0,
        "Zoom": -1.0,
        "Center": 0,
        "ViewMode": 0,
        "SmallViewShown": True,
        "HasSignature": False,
    }


def timesync(tid: int, date: int, events: list[int], *, active: bool = False,
             label: str = "", start: bool = False) -> dict:
    """An instant. `active` is what makes it a trigger: it waits."""
    return {
        "ObjectName": "Scenario::TimeSyncModel",
        "id": tid,
        "Metadata": meta(f"Sync.{tid}", label, "Gray"),
        "Date": date,
        "Events": events,
        "MusicalSync": -1.0,
        "AutoTrigger": False,
        "Start": start,
        "Active": active,
        "Expression": " { true == false } ",
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
                "Children": [param("level"), param("colour"), param("shutter")],
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
            osc_device(),
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


BUILDERS = {"00": ("00-what-score-is", lesson_00)}


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "00"
    if which not in BUILDERS:
        print(f"unknown lesson {which!r}; known: {', '.join(BUILDERS)}")
        return 1
    slug, builder = BUILDERS[which]
    out_dir = LIBRARY / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = builder()
    temporal = out_dir / f"lesson-{which}.score"
    nodal = out_dir / f"lesson-{which}-nodal.score"
    temporal.write_text(json.dumps(doc, indent=1), encoding="utf8")
    nodal.write_text(json.dumps(to_nodal(doc), indent=1), encoding="utf8")
    print(f"wrote {temporal.relative_to(ROOT)}")
    print(f"wrote {nodal.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
