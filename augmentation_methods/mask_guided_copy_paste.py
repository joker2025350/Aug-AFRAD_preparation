"""Mask-guided defect Copy-Paste.

Pastes the masked defect region of a donor image onto a background image.

Usage:
    python mask_guided_copy_paste.py --donor d.jpg --mask m.tif \
        --background b.jpg --output out.jpg [--dx 0 --dy 0 --feather-radius 0]
"""

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter


def copy_paste(donor, mask, background, dx=0, dy=0, feather=0.0):
    donor = donor.convert("RGB")
    mask = mask.convert("L").point(lambda v: 255 if v > 127 else 0)
    if mask.size != donor.size:
        raise ValueError("Donor and mask sizes differ")
    if mask.getbbox() is None:
        raise ValueError("Empty mask")
    background = background.convert("RGB").resize(donor.size, Image.Resampling.LANCZOS)

    alpha = mask
    if feather > 0:
        alpha = ImageChops.multiply(mask, mask.filter(ImageFilter.GaussianBlur(feather)))

    donor_layer = Image.new("RGB", donor.size, (0, 0, 0))
    donor_layer.paste(donor, (dx, dy))
    alpha_layer = Image.new("L", donor.size, 0)
    alpha_layer.paste(alpha, (dx, dy))
    if alpha_layer.getbbox() is None:
        raise ValueError("Shifted mask is outside the image")

    output = background.copy()
    output.paste(donor_layer, (0, 0), alpha_layer)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--donor", type=Path, required=True)
    parser.add_argument("--mask", type=Path, required=True)
    parser.add_argument("--background", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dx", type=int, default=0)
    parser.add_argument("--dy", type=int, default=0)
    parser.add_argument("--feather-radius", type=float, default=0.0)
    args = parser.parse_args()

    result = copy_paste(
        Image.open(args.donor),
        Image.open(args.mask),
        Image.open(args.background),
        args.dx,
        args.dy,
        args.feather_radius,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() in {".jpg", ".jpeg"}:
        result.save(args.output, quality=95, subsampling=0)
    else:
        result.save(args.output)


if __name__ == "__main__":
    main()
