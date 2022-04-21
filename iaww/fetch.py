import requests
from pathlib import Path


with open('images.txt', 'r') as fp:
    content = fp.read()
    image_urls = content.splitlines()


output_dir = Path(__file__).absolute().parent / 'images'
output_dir.mkdir(parents=True, exist_ok=True)


for image_url in image_urls:
    print(f'Getting the image from {image_url}')
    image_data = requests.get(image_url).content
    filename = Path(image_url).name
    with open(output_dir / filename, 'wb') as fp:
        fp.write(image_data)
