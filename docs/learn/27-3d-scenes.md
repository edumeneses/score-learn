---
layout: default
title: "Lesson 27: 3D scenes"
description: "Geometry, models, and compute shaders: build a scene from primitives and a loaded model, and drive it from the timeline."
parent: Lessons
nav_order: 32
unit: "27"
permalink: /learn/27-3d-scenes.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "30 min"
score_file: none
---

# Lesson 27: 3D scenes

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 26]({{ site.baseurl }}/learn/26-shaders-and-mixing.html).
>
> **You will need** a window device, and optionally a glTF model file.
>
> **You will build** a scene with a primitive, a loaded model, and a generated geometry, all animated from the timeline.

## Why this matters

Three-dimensional work in *score* is the same render graph as Lesson 25 with geometry added, and it fits the course's logic exactly: geometry is data, materials are shaders, and every parameter is a port. The reason to spend a lesson on it is that the vocabulary is new, and the failure modes are specific: a scene that renders black is usually missing one of four things, and knowing which four saves an hour.

It is also where generated geometry becomes interesting. Because arrays of numbers can be turned into meshes, a scene can be computed rather than modelled, and the array tools you met in Lesson 14 apply directly.

## Concepts

**Four things a scene needs.** A scene renders only when it has geometry to draw, a material to draw it with, a camera to draw it from, and an output to draw into. A black window is almost always one of those four missing, and checking them in that order is the fastest diagnosis available.

**Primitives and loaded models.** Mesh processes provide primitives, cubes, planes, spheres, which are enough for a great deal of work. For modelled content, a model loader reads glTF, the standard interchange format that most modelling tools export.

**Geometry as data.** Arrays can be converted to meshes and to textures, and attributes can be extracted from geometry back into arrays. This is the door between the array tools of Module E and the render graph: generate positions with an expression, convert them to geometry, and you have a computed scene.

**Compute shaders.** For work that belongs on the GPU but is not a picture, a compute shader runs a program over data rather than over pixels. Particle systems and large simulations are the usual reason to reach for one.

**Textures come from anywhere.** A material's texture can be a video file, a camera, a shader from Lesson 26, or a script's output. Because these are all textures in the same graph, feeding a live camera onto a rotating model is a cable, not a feature.

**Coordinates and the fisheye case.** A camera has a position and an orientation, both of which are ports and therefore automatable. For dome work, the projection matters more than the geometry: a fisheye output is what a dome expects, and [Milestone P6]({{ site.baseurl }}/learn/p6-fulldome-scene.html) covers it.

## Walkthrough: three kinds of geometry

{: .note }
> A figure for this lesson is pending: it needs a live GPU session and a model file, so it cannot be produced by the scripted pipeline. See `checks/27-3d-scenes.md`.

1. **Declare a window device** if you have not, and switch to the nodal view.
2. **Add a primitive mesh** and a model display process, cable the mesh into the display and the display into the window. Something should appear. If not, walk the four requirements above.
3. **Move the camera.** Find the camera's position ports and automate one, so the scene rotates over twenty seconds. This is the same automation mechanism as everywhere else.
4. **Give it a texture.** Cable a shader from Lesson 26 into the material's texture input. A generated image is now wrapped on a primitive.
5. **Swap the texture for a camera** device and confirm it updates live.
6. **Load a model.** Add a model loader, point it at a glTF file, and cable it in alongside the primitive. Note the scale: models exported from different tools arrive at wildly different sizes, and this is normal.
7. **Generate geometry.** Use an array generator to produce a set of positions, convert the array to geometry, and render it. You now have a scene whose content is computed rather than authored.
8. **Animate the generation.** Automate a parameter of the array generator so the computed geometry changes shape over time.
9. **Extract an attribute.** Take positions back out of a geometry into an array, and drive something else with them, a sound parameter for instance. The graph runs in both directions.
10. **Try a compute shader** if your scene wants many elements, and compare the frame rate with the array-based approach at the same element count.
11. **Measure.** Note the frame rate with all three kinds of geometry present. This number decides how ambitious the milestone can be.

## Reading a black window

The four-part check, expanded, because this is the most common experience in the lesson and the least documented.

**Is there geometry?** A mesh process with no parameters set may produce nothing. Try a primitive first, always: it removes the question.

**Is there a material?** Geometry with no material has nothing to be drawn with. Some processes provide a default; not all do.

**Is there a camera, pointing at the geometry?** A camera inside the object, or facing away, renders exactly what a camera facing a wall renders. Move it far back and rotate before assuming the geometry is missing.

**Is the output cabled?** Per Lesson 25, nothing appears until something reaches the window device.

Then two more, in order of how often they catch people:

**Scale.** A loaded model may be a thousand times too large or small. If the camera is inside a vast object, you get a solid colour, which reads as a broken render rather than a scale problem.

**Depth and ordering.** Two surfaces at the same depth, or a scene lit from behind, produce images that look like errors and are geometry.

## Modelled or computed?

Two ways to get geometry, with different consequences for the rest of the project.

**Modelled**, in a dedicated tool and imported as glTF. Right when the shape is the point: an object, a building, a character. The cost is that the shape is now outside your document, so changing it means changing tools, and the file has to travel with the project like any other media, per Lesson 05.

**Computed**, from arrays generated inside the score. Right when the shape is a consequence of something else: a field of points whose positions come from a sensor, a form that changes over the piece, a structure with a parameter you want to automate. The shape is then part of the document, versioned with it, and drivable from the timeline.

The second is more distinctive to this software and the more common answer for the work this course describes. A useful hybrid is to import one modelled object and generate everything around it, which keeps the recognisable form and the parametric freedom at once.

One more practical note on units. Nothing in the graph enforces a world scale, so a project mixing modelled and computed geometry has to pick one and convert at the boundary. Deciding that a unit is a metre, writing it down, and scaling imported models to match on arrival is far less work than discovering halfway through a piece that half your scene is a thousand times too large.

## Common mistakes

- **Assuming a black window means a broken graph.** Walk the four requirements.
- **Not trying a primitive first.** It isolates every question about a loaded model.
- **Ignoring model scale.** Exporters disagree, and the symptom is not obviously a scale symptom.
- **Building a scene in the temporal view.** Use the nodal view, as with all graph work.
- **Cabling a texture into a geometry input** or the reverse. Read the port names.
- **Reaching for a compute shader before measuring.** Array-based generation is often enough and much easier to debug.
- **Planning dome content on a flat monitor** without understanding the projection, which the next milestone addresses directly.

## Exercise

Build a scene containing a primitive with a generated texture, a loaded glTF model, and a computed geometry from an array, with the camera animated over thirty seconds so all three are seen. Then extract one attribute from the computed geometry and use it to drive a parameter outside the render graph, in audio or in lighting.

**Success criterion:** all three kinds of geometry render together, the camera movement is written as an automation rather than performed, and one value crosses out of the graph into another medium. If the window was black at any point, note which of the four requirements was missing.

## Going further

- [The 3D examples]({{ site.docs_baseurl }}/examples/3d/3d.html), which are the best available documentation for this material and are worth opening one by one.
- [Meshes]({{ site.docs_baseurl }}/processes/meshes.html), [model display]({{ site.docs_baseurl }}/processes/model-display.html), and [object loader]({{ site.docs_baseurl }}/processes/object-loader.html).
- [Array to mesh]({{ site.docs_baseurl }}/processes/array-to-mesh.html) and [extract attribute]({{ site.docs_baseurl }}/processes/extract-attribute.html) for the data-geometry boundary.
- [Compute shader]({{ site.docs_baseurl }}/processes/compute-shader.html).
