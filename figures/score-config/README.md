# Pinned settings for figure captures

`score.conf` is the settings file every figure is captured with. `capture.py launch`
copies it into a fresh private `XDG_CONFIG_HOME` at each launch, so nothing a session
changes survives into the next, and Edu's own `~/.config/ossia` is never read or written.

Three incidents are why it exists:

- **2026-09-17**: `Settings > User interface > Show musical metrics` had been left on
  after figure 24-01, which blanks the time ruler and swaps the transport's speed field
  for a tempo. A pinned file cannot drift that way.
- **2026-09-25**: `~/.config/ossia/failsafe.bit`, dated 2026-07-09, meant every capture
  since July started in failsafe mode. The private directory has no such file.
- **2026-09-25**: the transport clock stayed at zero after Play. The user settings select
  the native PipeWire driver with `Auto-connect ports` off, so score's PipeWire node is
  never linked to a sink, PipeWire keeps it suspended, and the log reports
  `Audio engine seems stuck?`. This file selects `Dummy (No audio)` instead, which ticks
  on its own. The course needs no sound from a figure.

It was derived from Edu's `score.conf` of 2026-09-25, with the Dummy driver selected
through the interface on the capture server (only the `Driver` key changed) and recent
files, plugin caches, and window geometry removed. The binary `@Variant(...)` values are
score's own serialisation of factory keys; change them through the interface on a
throwaway instance and copy the result, rather than by hand.

`Library/RootPath` and the plug-in search paths name `/home/edu`; on another machine,
edit them or pass `--user-config` to `capture.py launch`.
