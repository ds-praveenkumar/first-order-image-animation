# main.py

from demo import load_checkpoints


def get_generator_detector():
    generator, kp_detector = load_checkpoints(  config_path='config/vox-256.yaml', 
                                                checkpoint_path='vox-cpk.pth.tar'
                                            )

    print(" generator and detector loaded ...  ")
    return generator, kp_detector


if __name__ == "__main__":
    generator, kp_detector = get_generator_detector()
