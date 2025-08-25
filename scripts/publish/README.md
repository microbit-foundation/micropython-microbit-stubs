This directory contains scripts and templates for packaging stubs as wheels and publishing these.

Preparation:

* Optional: remove old wheels from dist (required if you want to regenerate wheels for the same version)
* Create a virtual environment
* install `build` and `twine`

Building the wheels:

```
python build-wheels.py
```

Publishing the wheels:

```
python publish-wheels.py
```
