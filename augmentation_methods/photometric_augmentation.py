"""Deterministic photometric augmentation (training set only).

Usage:
    python photometric_augmentation.py --train-dir <train> --output-dir <out>

<train> contains one sub-folder per class (broken, crack, folds, impurities,
normal, rough). Only the new augmented images are written to <out>/<class>/;
original images are left untouched.

  crack, folds        6 variants per image (all transforms below)
  impurities, rough   1 variant per image, chosen by the image's SHA-256
  broken, normal      not augmented
"""

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageEnhance

SUFFIXES = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

TRANSFORMS = (
    ("brightness_090", "brightness", 0.90),
    ("brightness_110", "brightness", 1.10),
    ("contrast_090", "contrast", 0.90),
    ("contrast_110", "contrast", 1.10),
    ("gamma_090", "gamma", 0.90),
    ("gamma_110", "gamma", 1.10),
)
ALL, ONE = "all", "one"
CLASS_POLICY = {"crack": ALL, "folds": ALL, "impurities": ONE, "rough": ONE}


def transform(image, name, value):
    if name == "brightness":
        return ImageEnhance.Brightness(image).enhance(value)
    if name == "contrast":
        return ImageEnhance.Contrast(image).enhance(value)
    lut = [round((i / 255.0) ** value * 255.0) for i in range(256)]
    return image.point(lut * len(image.getbands()))


def selected(policy, path):
    if policy == ALL:
        return TRANSFORMS
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return (TRANSFORMS[int(digest[:16], 16) % len(TRANSFORMS)],)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--train-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    for cls, policy in CLASS_POLICY.items():
        out = args.output_dir / cls
        out.mkdir(parents=True, exist_ok=True)
        count = 0
        for path in sorted((args.train_dir / cls).iterdir()):
            if path.suffix.lower() not in SUFFIXES:
                continue
            image = Image.open(path).convert("RGB")
            for tid, name, value in selected(policy, path):
                transform(image, name, value).save(out / f"{path.stem}__{tid}.png")
                count += 1
        print(f"{cls}: {count} images")


if __name__ == "__main__":
    main()
