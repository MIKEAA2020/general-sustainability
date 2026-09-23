#!/usr/bin/env python3
"""Convert graphical_abstract.png (300 dpi canvas) to the submission TIFF
(Lossless LZW, 300 dpi tag), per Elsevier graphical-abstract specs.
Run in the same directory as make_graphical_abstract.py."""
from PIL import Image
im = Image.open("graphical_abstract.png")
im.save("graphical_abstract.tif", compression="tiff_lzw", dpi=(300, 300))
print("wrote graphical_abstract.tif (LZW, 300 dpi)")
