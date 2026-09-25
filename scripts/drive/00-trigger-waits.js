// Lesson 00: the trigger after Approach waits for /lesson/go.
// Plays past Approach's end (6 s) with no input and captures at 8.5 s,
// where Approach should be finished and neither Bright nor Dark started.
//   python3 scripts/drive.py library/learn/00-what-score-is/lesson-00.score \
//       scripts/drive/00-trigger-waits.js
var steps = [
  log("find Approach: " + find("Approach")),
  call(function () { Score.play(); }),
  sleep(8500),
  call(function () { Score.pause(); }),
  shot(runDir + "/trigger-waits-8.5s.png"),
];
