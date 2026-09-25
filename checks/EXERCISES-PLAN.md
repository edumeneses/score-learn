# Exercise redesign, proposed 2026-09-25

Edu's brief: the exercises are too academic. Lesson 03's asks for keyboard-only navigation,
which does not work (arrow keys act on whichever part of the window has focus, and that
part cannot be reached by Tab or arrows), and is not what that lesson is for. Exercises
should be lighter and reach a practical result tied to the lesson: making a sound,
connecting a webcam, and so on.

## Decisions (Edu, 2026-09-25)

- **A**, with a change: no starter document ships. The reader builds the sketch step by
  step in Lesson 01's exercise, from a free sound installed through the package manager
  and a shader from the process library.
- **Hardware optional**, but the webcam and the microphone come first where an exercise
  interacts with devices, since readers are assumed to be on laptops, always with a
  fallback for no camera and no microphone. CLAUDE.md's non-negotiable 5 now says so.
- **Solutions** ship only where the result is hard to picture.
- **Practice minutes** are shortened where possible.

## Status

- **Module A written, 2026-09-25**: 00, 01, 02, 03, 04, 05, and P1. Each step was
  performed in 3.8.2 on the capture server, except installing a package, which Lesson 01's
  own section already described, and deleting an interval; what was confirmed, and what
  failed and was therefore left out, is in CLAUDE.md under "Exercises are light and
  practical". Two corrections came from that testing: a gain automation made with
  `Create automation` starts flat at zero, so the sound is silent until its end is
  raised, and a segment bends with `Shift+Drag` after selecting it. Practice minutes: 02 and 03 to 10, 04 to 15, 05 to 10; 01 stays 15 and
  P1 45. Lesson 38's dependency on the old question list was removed at the same time.
- The final module A exercises differ from the table below where testing said so: 02
  recolours the shader instead of setting a state, because moving an interval by dragging
  did not work; 05 re-points the sound by dragging the copy from the project folder panel,
  because typing into the `Path` field did not.
- **Next**: module B (06 to 09, P2), where the webcam and microphone first make sense.

## The original proposal

## What changes, in five rules

1. **Every exercise ends in something you hear or see.** A sound fades in, the window turns
   red, the synth plays four notes. The success line becomes "You are done when you hear
   ..." instead of "You can state ...".
2. **One idea from the lesson, used once, inside the practice budget** in `units.yml`
   (15 to 30 minutes for most lessons). No written maps, essays, question lists, decision
   tables, eight-hour runs, or strangers running the piece. Those move to "Going further"
   where they are still worth something.
3. **Every exercise starts from a shipped document**, so that setup does not eat the time
   and each lesson still works on its own for a reader who arrives from the Find by topic
   page. The cross-lesson threads (the Lesson 00 paragraph carried to 02, 15, and 38; the
   Lesson 06 device map carried to 07) go. Milestones stay cumulative, as designed.
4. **Hardware stays optional, with a fallback in the same sentence.** A webcam, a
   microphone, a phone, or a MIDI controller makes the exercise more fun; the shipped
   clip, sound file, second instance, or virtual port does the same job without it. This
   keeps CLAUDE.md's non-negotiable 5 (see question 2).
5. **Every exercise is performed once in the pinned build before it is published**, on the
   capture server, scripted with `drive.py` where possible. Lesson 03's exercise would not
   have survived that step. Where the result is a document, a solution ships beside the
   lesson's own document.

## The one structural decision: what makes the early lessons audible

Lessons 00 to 18 drive an OSC device, `lesson:`, that nothing listens to, so playing their
documents shows a moving playhead and nothing else. That is the root of the academic
feel: there is no result to aim at. Three ways out:

- **A. A shipped starter, `sketch.score` (recommended).** One looping sound excerpt through a
  `Gain`, and a window showing a flat colour from a shader, both with ports ready to
  automate. Lesson 01 ships it; exercises 01 to 18 use it as "the thing that makes it
  real". Lesson documents and figures stay as they are, and devices are still taught in
  06 to 09 where they belong.
- **B. Rebuild lessons 00 to 05 around media** instead of the OSC device. The most direct,
  but it rewrites six lessons, their figures, and the vocabulary examples, and brings
  media in before its module explains it.
- **C. A monitor for the `lesson:` device**: a second document that receives its OSC and
  shows the values as colour and sound. Nothing in the lessons changes, but every early
  exercise then needs two score windows running, which is the opposite of lighter.

## Lesson by lesson (under A)

Time is the practice budget from `units.yml`. "Needs" is beyond score and the shipped files.

| Unit | Now | Proposed exercise | You are done when | Needs |
|---|---|---|---|---|
| 00 | Write and annotate a paragraph about your work | **Pick your first goal**: choose one thing you want score to do (play a sound, show a camera, move a light, react to a sensor), and the page tells you which lesson gets you there | you know which lesson is your first stop | nothing |
| 01 | Answer three questions about an example; press F1 twice | **Make score make a sound**: open `sketch.score` and press play; if silent, the three-step audio check from 19 | you hear the loop and see the coloured window | speakers |
| 02 | Rewrite the 00 paragraph with the eight words | **Find it and change it**: in the sketch, shorten the interval that holds the sound, and make the state that sets the colour set red | the loop stops sooner and the window starts red | nothing |
| 03 | Keyboard-only navigation (does not work) | **Drive the transport**: play from the middle with Play from here, stop, return to the start, play at half speed, zoom to fit | you started mid-piece and heard it at half speed | speakers |
| 04 | Two automations, stretch vs keep shape | **Fade in**: automate the sketch's gain so the loop fades in over five seconds; lengthen the interval once with Ctrl+drag and once without | you hear the fade stretch in one case and not the other | speakers |
| 05 | Package, move, fragment to library | **Take it with you**: save the sketch as a project folder, move or rename the folder, reopen | it still plays, sound and all, from the new place | nothing |
| P1 | Extend the cue (musical or operable) | Same brief on the sketch's sound and colour, with one extension: **a real ending**, everything to silence and black in the last five seconds | playback ends silent and dark every time | speakers |
| 06 | Write your project's device map | **Turn your speakers down from the score**: add the Audio device and automate its output level | the whole mix dips when the automation does | speakers |
| 07 | One OSC device, break it three ways | **Talk to another app**: send the sketch's volume over OSC to an OSC monitor app on a phone, or to the shipped six-line Python receiver; then send a slider back | you see numbers arrive, and the slider moves the sound | optional phone |
| 08 | Four parameters of different types | **A fade that never goes silent**: set the automation's own range so the loop dips to 20 percent and back; then push a value past a parameter's range under Clip and under Free | the dip stops at 20 percent, and you hear the two modes differ | speakers |
| 09 | Four live-captured cues | **Three looks, one click each**: capture "quiet blue", "loud red", and "off" as states and jump between them; fix one with Ctrl+R | each click recalls its look exactly | speakers |
| P2 | Rebuild against a real receiver, extend | Same brief; one extension: **a blackout at the end** | the software receiver shows the wash and ends dark | software Art-Net receiver |
| 10 | Five versions of one fade, described | **Three fades, keep one**: linear, slow start, slow end on the same sound; keep the one that feels like a light coming up | you chose by listening | speakers |
| 11 | One LFO, three shaped destinations | **Tremolo and pulse**: one LFO on the gain and the colour, speeding up over twenty seconds | the sound wobbles and the window pulses, faster and faster | speakers |
| 12 | Record one gesture three ways | **Record a gesture**: record a value you move by hand (a phone slider, a MIDI knob, or the shipped emulated sensor) and play it back on the volume | the playback repeats your gesture | optional controller |
| 13 | Tune a pipeline, write the reasoning | **Calm a nervous input**: smooth the shipped jittery sensor until the volume follows it without crackle | the sound follows smoothly | speakers |
| 14 | A twelve-row decision table | **Find it in a minute**: three tasks (a click on every beat, words in the window, the loudness of a sound) solved from the library by search | all three work | speakers |
| P3 | Extend the bench | Same brief; one extension, **a safe value when the input stops** | unplug or stop the sensor and the sound settles | emulated sensor |
| 15 | Forty-second passage, two triggers | **Press to continue**: the sketch waits for your click before the loud section, and goes on by itself after ten seconds | it waits for you, and never forever | speakers |
| 16 | Three alternatives, six tests | **Heads or tails**: a random value chooses one of two sounds each time the instant is reached | you hear different sounds on different runs, never both | speakers |
| 17 | Three kinds of repetition | **A loop that ends itself, and a sound on demand**: a phrase that repeats four times, plus a one-shot you fire whenever you like | the loop ends alone, and your shot plays over it | speakers |
| 18 | Make a score operable, hand it over | **Safe to stop**: a stop cue that silences and blacks out, and a start marker on the second section | pressing stop at any moment leaves silence | speakers |
| P4 | Extend; eight-hour test | Same brief; one extension, **a rare third outcome**; the eight-hour run moves to Going further | ten runs in a row all return to idle | emulated sensor |
| 19 | Four files, predict the routing | **Left, right, and a room**: one sound to the left speaker only, one to the right, and a reverb on the master | you hear them placed where you routed them | speakers |
| 20 | Two-minute, four-file document | **A thirty-second collage** from two shipped excerpts: one loops, one plays once with a fade-out | it sounds finished at thirty seconds | speakers |
| 21 | Three-effect chain, reorder, live input | **Make it sound like a cave**: add a reverb and automate its mix; with a microphone, run your voice through the same chain | the room grows over twenty seconds | optional mic |
| 22 | Three speaker-layout variations | **A sound that circles your head**: the four-speaker scene folded to headphones, then twice the speed | you hear it go round | headphones |
| P5 | Extend the set | Same brief, one extension; success is two performances ended by one key | the set ends on one key | keyboard |
| 23 | Four MIDI paths | **Play the synth**: Synthimi playing a four-note piano roll, then from your MIDI keyboard or a virtual one | you hear your notes | optional MIDI keyboard |
| 24 | Three metres and a tempo curve | **Enter on the beat**: a metronome at 90 BPM and a loop whose trigger, quantised to the bar, lands on the downbeat however late you click | the loop always starts on one | speakers |
| 25 | Two clips through a mixer, measure fps | **See yourself**: your webcam, or the shipped clip, into a window, crossfaded with the second clip | your face (or the clip) fades into the other | optional webcam |
| 26 | New shader input, mixing, LED view | **Your own control on a shader**: add one slider to a library shader and automate it; with a webcam, run your image through it | the picture changes as the automation moves | optional webcam |
| 27 | Three geometries, attribute out | **Spin a cube**: a textured primitive and a camera orbit automated over thirty seconds | the cube turns in the window | nothing |
| 28 | Two measures, three files | **Make the picture dance**: the loop's loudness drives brightness, its hits drive a flash | the image moves with the music | speakers |
| P6 | Extend (spatial or operable) | Same brief, one extension; success is ten minutes in fisheye without a full-field flash | it runs ten minutes clean | nothing |
| 29 | Threshold counter, console line, randomiser | **A random-note machine**: a JavaScript process sends a random pitch to the synth on every beat; one console line plays it | it plays different notes each run | speakers |
| 30 | Same relation three ways | **A sound in one line**: a bytebeat formula you change while it plays | you hear your formula | speakers |
| 31 | Faust processor, replicate, compare | **Your own tremolo in five lines of Faust**, its rate on the timeline | the loop wobbles at the rate you drew | speakers |
| 32 | Refactor a patch's sequencing | **Pd makes the sound, score keeps time**: the shipped patch, its gain automated from the timeline | Pd's sound follows score's curve | Pure Data |
| 33 | Six-control surface, stranger runs it | **Control the piece from your phone**: start, stop, and one slider in a browser on another device | the phone starts the sound | optional phone |
| 34 | Five documents, two tests | **The one-page card** for one of your milestones, and nothing else | a friend could start it from the card | nothing |
| 35 | Deploy to a Pi, three tests | **Run it with no interface**: `ossia-score --no-gui --autoplay` on your own machine, stopped with Ctrl+C; a Pi is Going further | the piece plays with no window open | nothing |
| 36 | Two machines, latency, failure | **One cue, two instances**: instance A fires a cue that makes instance B play a sound, on one machine | B plays when A says so | nothing |
| 37 | Record and stream, measure fps | **Record thirty seconds of your piece** to a video file and watch it back | it plays back in sync | OBS Studio |
| 38 | File a report, answer a question | **Answer one real question** you had during the course from the manual, and note where the answer was | you found it | nothing |
| 39 | Build and modify the template | Keep as is; it already ends in something that works | your object appears in the library | compiler toolchain |

## Questions for Edu

1. **A, B, or C** for the early lessons? A is the recommendation.
2. **Hardware**: keep webcam, microphone, phone, and MIDI controller strictly optional with a
   fallback in the same sentence, as above? That keeps non-negotiable 5; making any of them
   a requirement would change it.
3. **Solutions**: ship a solution document per exercise, or only where the result is hard
   to picture?
4. **Budgets**: the new exercises fit the current practice minutes; keep them, or shorten
   some (00 to 05 could drop to ten minutes)?

## What implementation involves

- `sketch.score` built by `mkscore.py` (a Sound process through Gain, a Window device fed
  by a colour shader), verified on the capture server; a jittery emulated sensor and a
  six-line OSC receiver for 07, 12, and 13.
- 46 exercise sections rewritten in Edu's voice, each checked with `check_voice.py` and
  kept inside the 1,400 to 1,900 word budget, which moves when an exercise shrinks.
- Each exercise performed in 3.8.2 before commit, with its result captured, and failures
  recorded in `checks/`.
- `topics.yml` gains a "Make something happen" group pointing at the exercises; lessons
  00, 02, 15, 16, and 38 lose their references to the old threads.
- Suggested order: module A first (00 to 05 and P1, with `sketch.score`), reviewed by Edu,
  then the rest module by module.
