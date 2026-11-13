#!/usr/bin/env python3
"""cutest-picture-01 entry: write one picture to /output/entry.png.

The picture is a tiny fluffy cream kitten and a tiny fluffy cream puppy
snuggled cheek-to-cheek, asleep together in a soft pink knitted basket,
both wearing tiny pink knitted scarves, with floating pink hearts and
cherry blossom petals in warm golden light. It is stored in this
repository as base64 text in picture.jpg.b64 (a single line, so the
repository holds no binary files). The program decodes it and writes
the JPEG bytes to /output/entry.png.

No network, no randomness, no timestamps: two runs write the same bytes.
"""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "picture.jpg.b64")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    with open(DST, "wb") as out:
        out.write(data)
    print("wrote", DST)


if __name__ == "__main__":
    main()
