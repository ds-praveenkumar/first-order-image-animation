# load_source_data.py


from argparse import ArgumentParser
import imageio
from skimage.transform import resize

def read_source_image(path):
    """
        Reads images from the path provided
    """
    source_image = imageio.imread(path)
    source_image = resize( source_image, (256, 256))[..., :3]



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument( "--")

    parser.add_argument( "--imgpath",default='first-order-image-animation/me.jpg', help="path to image file")

    opt = parser.parse_args()
    print(opt.imgpath)
    # parser.add_argument("--config", required=True, help="path to config")
    # parser.add_argument("--checkpoint", default='vox-cpk.pth.tar', help="path to checkpoint to restore")