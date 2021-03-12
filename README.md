# first-order-image-animation
Repo for First Order Motion Model for Image Animation

This repo generates animated image from the provided image source and driving video. <br>

`data`: the data can be downloaded from this this [link](https://drive.google.com/drive/folders/1kZ1gCnpfU0BnpdU47pLM_TQ6RypDDqgw?usp=sharing) and saved in the root folder. we will need one image source and one video source to generate the animation. each with size of 256 x 256.

### setup
- git clone <git url>
- cd project folder
- pip install -e .
- python main.py

The animated video will be generated in the root folder with the name `generated.mp4`

### References:
- https://github.com/AliaksandrSiarohin/first-order-model
- https://aliaksandrsiarohin.github.io/first-order-model-website/