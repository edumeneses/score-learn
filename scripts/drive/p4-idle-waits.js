// P4: the visitor trigger after Idle waits between 4 s and 60 s.
// With no input, at 7 s Idle should be over and both branches unstarted;
// past 60 s the maximum should have released the trigger by itself.
//   python3 scripts/drive.py library/learn/p4-interactive-installation/p4-solution.score \
//       scripts/drive/p4-idle-waits.js --timeout 120
var steps = [
  call(function () { Score.play(); }),
  sleep(7000),
  shot(runDir + "/p4-7s.png"),
  sleep(56000),
  call(function () { Score.pause(); }),
  shot(runDir + "/p4-63s.png"),
];
