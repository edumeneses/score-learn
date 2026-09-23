---
layout: default
title: "Lesson 27: 3D scenes: meshes, textures, and cameras"
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

# Lesson 27: 3D scenes: meshes, textures, and cameras

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 26]({{ site.baseurl }}/learn/26-shaders-and-mixing.html), because the textures this lesson wraps onto geometry come from the shaders it introduced.
>
> **You will need** a window device, and optionally a glTF model file, since the model-loading step is the only one that depends on an external file.
>
> **You will build** a scene with a primitive, a loaded model, and a generated geometry, all animated from the timeline through the same automation you have used throughout the course.

## Why this matters

Work in three dimensions in *score* uses the same render graph as Lesson 25 with geometry added, and it fits the course's logic closely, because geometry is data, materials are shaders, and every parameter is a port. The reason to spend a lesson on it is that the vocabulary is new and the failure modes are specific: a scene that renders black is usually missing one of four requirements, and knowing which four saves an hour of guessing.

Furthermore, this is where generated geometry becomes interesting, because arrays of numbers can be turned into meshes, so that a scene can be computed instead of modelled and the array tools you met in Lesson 14 apply directly to the render graph.

## Concepts

### The four requirements of a scene

A scene needs four things before it renders, and a black window is almost always one of them missing. A scene renders only when it has geometry to draw, a material to draw it with, a camera to draw it from, and an output to draw into, so checking those four in that order is the fastest diagnosis available when the window stays black.

### Primitives and loaded models

Primitives cover a great deal of work, and loaded models cover the rest. Mesh processes provide primitives such as cubes, planes, and spheres, which are enough for many pieces, whereas modelled content arrives through a model loader that reads glTF, the standard interchange format that most modelling tools export.

### Geometry as data

Geometry is data, and the conversion runs in both directions. Arrays can be converted to meshes and to textures, and attributes can be extracted from geometry back into arrays, which makes this the door between the array tools of Module E and the render graph: generate positions with an expression, convert them to geometry, and you have a computed scene.

### Compute shaders

Compute shaders run a program over data on the GPU (graphics processing unit). For work that belongs on the GPU but is not a picture, a compute shader operates over data instead of over pixels. Moreover, particle systems and large simulations are the usual reason to reach for one.

### Texture sources

Textures can come from any source in the graph. A material's texture can be a video file, a camera, a shader from Lesson 26, or a script's output, and because these are all textures in the same graph, the same cable serves each of them. In other words, feeding a live camera onto a rotating model is a single connection and not a special feature.

### The camera and its projection

The camera is a set of ports, and dome work changes the projection. A camera has a position and an orientation, both of which are ports and therefore automatable. However, for dome work the projection matters more than the geometry, because a fisheye output is what a dome expects, and [Milestone P6]({{ site.baseurl }}/learn/p6-fulldome-scene.html) covers it.

## Walkthrough: three kinds of geometry

{: .note }
> A figure for this lesson is pending, because it needs a live GPU session and a model file, which the scripted pipeline cannot produce; see `checks/27-3d-scenes.md`.

1. **Declare a window device** if you have not already, and switch to the nodal view, where the cables between geometry, material, and output are visible.
2. **Add a primitive mesh** and a model display process, cable the mesh into the display and the display into the window, and confirm that something appears; if the window stays black, walk the four requirements from Concepts in order.
3. **Move the camera** by finding its position ports and automating one, so that the scene rotates over twenty seconds through the same automation mechanism you have used everywhere else.
4. **Give it a texture** by cabling a shader from Lesson 26 into the material's texture input, which wraps a generated image onto a primitive.
5. **Swap the texture for a camera device** and confirm that the surface updates live, since a camera is a texture like any other in this graph.
6. **Load a model** by adding a model loader, pointing it at a glTF file, and cabling it in alongside the primitive; note the scale, because models exported from different tools arrive at wildly different sizes, and this is normal.
7. **Generate geometry** by using an array generator to produce a set of positions, converting the array to geometry, and rendering it, so that you have a scene whose content is computed instead of authored.
8. **Animate the generation** by automating a parameter of the array generator, so that the computed geometry changes shape over time.
9. **Extract an attribute** by taking positions back out of a geometry into an array and driving something else with them, a sound parameter for instance, which shows that the graph runs in both directions.
10. **Try a compute shader** if your scene needs many elements, and compare the frame rate with the array-based approach at the same element count.
11. **Measure the frame rate** with all three kinds of geometry present, because this number decides how ambitious the milestone can be.

## Reading a black window

The four-part check from Concepts deserves expansion, because a black window is the most common experience in this lesson and the least documented one; the questions below are in the order in which to ask them.

**The first question is whether the scene contains geometry that can be drawn.** A mesh process with no parameters set may produce no output, so try a primitive first in every case, because a primitive that renders removes this question. Conversely, a primitive that does not render points further down the chain.

**The second question is whether the geometry has a material.** Geometry without a material cannot be drawn, and although some processes provide a default, not all of them do.

**The third question is whether a camera exists and points at the geometry.** A camera inside the object, or facing away from it, renders what a camera facing a wall renders, so move it far back and rotate it before assuming that the geometry is missing.

**The fourth question is whether the output is cabled.** Per Lesson 25, no image appears until something reaches the window device, however complete the rest of the scene is.

Once the four requirements are met, two further causes catch people, and scale is the more frequent of them.

**Scale is the first, because a loaded model may be a thousand times too large or too small.** If the camera is inside a vast object, you get a solid colour, which reads as a broken render although it is a scale problem.

**Depth and ordering are the second.** Two surfaces at the same depth, or a scene lit from behind, produce images that look like errors although they are correct renderings of the geometry as placed.

## Modelled or computed?

Geometry can be modelled or computed, and the choice has different consequences for the rest of the project.

**Modelled geometry is made in a dedicated tool and imported as glTF**, which is the right choice when the shape itself is the point, as with an object, a building, or a character. The cost is that the shape now lives outside your document, so changing it means changing tools. Additionally, the file has to travel with the project like any other media, per Lesson 05.

**Computed geometry comes from arrays generated inside the score**, which is the right choice when the shape is a consequence of something else: a field of points whose positions come from a sensor, a form that changes over the piece, or a structure with a parameter you want to automate. The shape is then part of the document, versioned with it, and drivable from the timeline.

The second approach is more distinctive to this software and the more common answer for the work this course describes. However, a useful hybrid is to import one modelled object and generate the surroundings around it, which keeps the recognisable form and the parametric freedom at once.

A practical note on units follows from mixing the two, because no element of the graph enforces a world scale, so a project combining modelled and computed geometry has to pick one and convert at the boundary. Deciding that a unit is a metre, writing that decision down, and scaling imported models to match on arrival is far less work than discovering halfway through a piece that half your scene is a thousand times too large.

## Common mistakes

- **Assuming that a black window means a broken graph**, when walking the four requirements usually finds a missing one.
- **Skipping the primitive test**, although a primitive isolates every question about a loaded model.
- **Ignoring model scale**, since exporters disagree and the symptom does not present itself as a scale symptom.
- **Building a scene in the temporal view**, whereas the nodal view is where graph work belongs, as with the rest of the course.
- **Cabling a texture into a geometry input** or the reverse, which reading the port names prevents.
- **Reaching for a compute shader before measuring**, although array-based generation is often enough and much easier to debug.
- **Planning dome content on a flat monitor** without understanding the projection, which the next milestone addresses directly.

## Exercise

Build a scene containing a primitive with a generated texture, a loaded glTF model, and a computed geometry from an array, with the camera animated over thirty seconds so that all three are seen. Then extract one attribute from the computed geometry and use it to drive a parameter outside the render graph, in audio or in lighting, so that a value leaves the graph as well as entering it.

**Success criterion:** all three kinds of geometry render together, the camera movement is written as an automation and not performed by hand, and one value crosses out of the graph into another medium. If the window was black at any point, note which of the four requirements was missing.

## Going further

- [The 3D examples]({{ site.docs_baseurl }}/examples/3d/3d.html), which are the best available documentation for this material and are worth opening one by one.
- [Meshes]({{ site.docs_baseurl }}/processes/meshes.html), [model display]({{ site.docs_baseurl }}/processes/model-display.html), and [object loader]({{ site.docs_baseurl }}/processes/object-loader.html).
- [Array to mesh]({{ site.docs_baseurl }}/processes/array-to-mesh.html) and [extract attribute]({{ site.docs_baseurl }}/processes/extract-attribute.html) for the data-geometry boundary.
- [Compute shader]({{ site.docs_baseurl }}/processes/compute-shader.html).
