import os
import cv2
from PIL import Image


def jpg2video(savepath, fps):

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    # 'hi' is your images folder path
    images = os.listdir('hi')
    im = Image.open('mv/' + images[0])
    videowriter = cv2.VideoWriter(savepath, fourcc, fps, im.size)
    
    os.chdir('hi')
    i = 0
    while (i < 1501):
        # Image.open('foo_'+str(i)+'.jpg').convert("RGB").save('foo_'+str(i)+'.jpg')
        image = 'foo_'+str(i)+'.jpg'
        try:
            frame = cv2.imread(image)
            videowriter.write(frame)
        except Exception as exc:
            print(image, exc)
        i += 10
    
    videowriter.release()
    print(savepath, 'Synthetic success!')


if __name__ == '__main__':
    # your video save path
    savepath = 'hi.avi'
    jpg2video(savepath, 10)

