==================
Blender Cheatsheet
==================

Legend
======

* C = Ctrl
* S = Shift
* T = Tab (when a macro)
* M = alt (a la emacs)

Shortcuts
=========

* 0: resolve to the default
* C-M-0: line up camera to your current view
* S-a: Add menu
* S-f: enter 'fly mode', where the view pans according to your mouse direction
* M-h: unhide hidden objects
* n: toggle properties panel
* C-n: start from the default model
* C-t: track one object with another
* u: unwrap a model according to it's seam lines
* C-z: undo
* S-C-z: redo
* T: toggle 'edit' mode
* F12: render the model

In Edit Mode
============

* C-T-1: Vertex Select
* C-T-2: Edge Select
* C-T-3: Face Select
* b: select all elements within a block (rectangular area)
* e: extrude (a selection of faces)
* C-e: bring up edges menu
* M-e: advanced extrude
* f: fill (a selection of vertexes)
* C-j: join separate mesh objects
* M-m: merge vertices menu (a selection of vertices)
* C-r: create an edgeloop (another loop around an existing loop)
* p: split mesh
* x: brings up delete menu

In fly mode
===========

* w: accelerates inward
* s: accelerates outward
* RMB: reset
* LMB: half the view

In Sculpt Mode
==============

* f: change brush size
* S-f: change the strength of the brush (denser = stronger)



When Object is Selected
=======================

* g: Move object to point
* M-g: reset object coordinate to global center
* h: Hide selected object
* m: Move an object to another layer
* r: rotates the object around vector of the object pointing toward your view (normal rotation)
* r-r: rotates the object parallel to the vector of the object pointing toward your view (trackball rotation)
* M-r: reset rotation to stand upright
* s: Scale an object
* M-s: Scale to original size
* x: Delete Object
* S-d: create a duplicate object

When Dragging/Scaling an object
=======================

* x: manipulate across X axis (global coordinates)
* x-x: manipulate across X axis (local coordinates)
* y: manipulate across Y axis
* y-y: manipulate across Y axis (local coordinates)
* z: manipulate across Z axis
* z-z: manipulate across Z axis (local coordinates)

Terminology
===========

* global coordinates: coordinates relative to the global world
* local coordinates: coordinates relative to the local object 

E.G. the global coordinates of an object's Z axis is different from an
object's Z axis once it is rotated, since the Z axis of the local
object has been rotated.

Edge Flow
---------

Edge flow means the edges of a mesh should be positioned along the
folds so that bending doesn't crease the faces.

Topology
--------

Describes the effectiveness of the edgeflow of the lines of a mesh
