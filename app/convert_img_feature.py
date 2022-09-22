from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np

if __name__ == '__main__':
    fe = FeatureExtractor()
    print("image path : ", Path("./static/images").glob("*.jpg"))
    for img_path in sorted(Path("./static/images").glob("*.jpg")):
        #print(img_path)  # e.g., ./static/img/xxx.jpg
        print("images : ", img_path)
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./static/features") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)