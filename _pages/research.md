---
layout: page
title: Research
permalink: /research/
---

### Python package/modules/functions

I have started creating an archive of modules and 
functions. The package/repository is located here and will
be kept up to date: [lwsspy](https://github.com/lsawade/lwsspy).
Documentation for the package can be found here: 
[https://lsawade.github.io/lwsspy/](https://lsawade.github.io/lwsspy/)
This is the place I edit and spend the most time on.

### Global CMT Inversion

The Global CMT inversion package that I was constantly working on is
can be found here: [GCMT3D](https://lsawade.github.io/GCMT3D/). However, 
most needed features are now included in 
[lwsspy](https://github.com/lsawade/lwsspy), see above

### How to make a Python package

A side project that I have been constantly expanding is the 
tutorial package [HTMAPP](https://lsawade.github.io/how_to_make_a_python_package/),
which in the beginngin I just wanted to have as a sample package.
It's so much more now. It's an almost complete overview on package 
management/distribution and a lot of small things that are not
covered in your Python tutorial.
It's basically a skeleton with every bone you need, but missing the
it's vital parts (the code that actually does stuff).
I have been working on this with mainly
[Peter Makus](https://petermakus.github.io). But other contributors are 
welcome.

### Matlab functions etc.

Although I have put a substantial amount of time into Matlab coding, I have 
never documented all the code that have written. This has now changed,
and I will put Matlab codes that appear over time into this Github 
repository: [LWSS](https://github.com/lsawade/lwss).


### Receiver Functions

With [Peter Makus](https://petermakus.github.io) and 
[Stéphane Rondenay](http://stephanerondenay.com), I was and am working on 
receiver function imaging from local to global scale. As part of Peter's 
Master's thesis, he translated the GLImER scripts into Python to making it
compatible with obspy, and he/we implemented a new way of CCP stacking that
makes it feasible to stack hundred thousands of traces globally. Furthermore,
we implemented imaging tools to create both publication grade cross sections
with arbitrary waypoints on the globe, as well as explore the CCP volumes in 
3D. 

### Mesh Exploration

For this exploration of the Receiver Functions I created a subtool called
[MeshSlice](https://github.com/lsawade/meshslice). It's documentation can 
be found [here](https://lsawade.github.io/meshslice/). The reason why we 
chose to make this tool a separate package is that it's agnostic to the input
mesh. It's based on [PyVista](https://docs.pyvista.org/index.html) and 
the VTK, and (as of now) slices any mesh using spherical slices around the 
`(0,0,0)`. 