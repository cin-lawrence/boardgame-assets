import numpy as np
from pathlib import Path
from PIL import Image


path_images = Path(__file__).absolute().parent / 'images_png'
path_output = Path(__file__).absolute().parent / 'images'

path_output.mkdir(parents=True, exist_ok=True)

meta = {
    'artifacts': (10, 4),
    'artifacts_lux': (10, 2),
    'cardbacks': (3, 1),
    'firstplayer': (2, 1),
    'mages': (10, 1),
    'mages_lux': (4, 1),
    'magicitems': (9, 1),
    'magicitems_lux': (2, 1),
    'monuments': (10, 1),
    'monuments_lux': (4, 1),
    'powerplaces': (10, 1),
    'powerplaces_lux': (4, 1),
    'scrolls': (9, 1),
    'tokens': (5, 1),
}

for filename, dimension in meta.items():
    ndinput = np.asarray(Image.open(path_images / f'{filename}.png'))
    h, w, c = ndinput.shape
    num_w, num_h = dimension
    print(
        f'Cutting file {filename} into {num_w} x {num_h}, '
        f'expecting size to be {w // num_w} x {h // num_h}'
    )

    ndtiles = ndinput.reshape(
        num_h, h // num_h, num_w, w // num_w, c).swapaxes(1, 2)
    for rowidx, rows in enumerate(ndtiles):
        for colidx, imgarray in enumerate(rows):
            Image.fromarray(imgarray).save(
                path_output / f'{filename}_{rowidx}_{colidx}.png')
