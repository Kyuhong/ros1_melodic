import os
import cv2
import yaml
from skimage.io import imread
import matplotlib.pyplot as plt

yaml_path = "~/map.yaml"
yaml_path = os.path.expanduser(yaml_path)

with open(yaml_path) as f:
    map_info = yaml.load(f)

image_path = map_info['image']
resolution = map_info['resolution']
origin = map_info['origin']

map_image = imread(image_path)
img = cv2.cvtColor(map_image, cv2.COLOR_GRAY2BGR)
h, w = img.shape[:2]

x_min = origin[0]
x_max = origin[0]+resolution*w
y_min = origin[1]
y_max = origin[1]+resolution*h

plt.imshow(img, extent=[x_min, x_max, y_min, y_max])
plt.show()
