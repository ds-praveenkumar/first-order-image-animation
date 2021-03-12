# main.py
import imageio
from demo import load_checkpoints
from demo import make_animation
from skimage import img_as_ubyte
from skimage.transform import resize
import warnings
warnings.filterwarnings("ignore")

def video_generator():

    generator, kp_detector = load_checkpoints(  config_path='config/vox-256.yaml', 
                                                checkpoint_path='vox-cpk.pth.tar'
                                            )

    print(" generator and detector loaded ...  ")
    source_image = 'me.jpg'
    driving_video = '04.mp4'
    source_image = imageio.imread(source_image)
    reader = imageio.get_reader(driving_video)
    
    #Resize image and video to 256x256
    source_image = resize(source_image, (256, 256))[..., :3]
    fps = reader.get_meta_data()['fps']
    driving_video = []
    try:
        for im in reader:
            driving_video.append(im)
    except RuntimeError:
        pass
    reader.close()
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]
    predictions = make_animation(   source_image, driving_video, generator, kp_detector, 
                                    relative=True, adapt_movement_scale=True)
    #save resulting video
    imageio.mimsave('generated.mp4', [img_as_ubyte(frame) for frame in predictions], fps=fps)
    print( 'video saved ...')

if __name__ == "__main__":
    video_generator()
