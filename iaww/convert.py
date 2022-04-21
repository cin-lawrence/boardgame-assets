import os
from PIL import Image
from pathlib import Path


output_dir = Path(__file__).absolute().parent / 'cubes'
output_jpg = Path(__file__).absolute().parent / 'cubes_png'
output_jpg.mkdir(parents=True, exist_ok=True)


for filename in os.listdir(output_dir):
    im = Image.open(output_dir / filename)
    # .convert('RGB')
    im.save(output_jpg / f'{Path(filename).stem}.png', 'png')
