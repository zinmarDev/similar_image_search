#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
import numpy as np

def feature_data_load():
    features = []
    img_paths = []
    for feature_path in Path("./app/static/features").glob("*.npy"):
        features.append(np.load(feature_path))
        img_paths.append(Path("static/images") / (feature_path.stem + ".jpg"))
    features = np.array(features)
    return features , img_paths

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'similar_image_search.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
