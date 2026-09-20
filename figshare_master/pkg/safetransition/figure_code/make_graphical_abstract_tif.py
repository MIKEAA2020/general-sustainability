#!/usr/bin/env python3
"""Export the EMS graphical abstract (1328 x 531 px) as LZW-compressed TIFF.

Mirrors the master deposit's graphical-abstract pipeline; PNG is regenerated
by make_safetransition_figs.py, this script only converts the format.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(HERE, "..", "figs_p3", "graphical_abstract.png")
dst = os.path.join(HERE, "..", "figs_p3", "graphical_abstract.tif")
im = Image.open(src)
im.save(dst, compression="tiff_lzw")
print(f"wrote {dst} ({os.path.getsize(dst)} B, {im.size[0]}x{im.size[1]} px)")
