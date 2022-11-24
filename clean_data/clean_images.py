from PIL import Image
import os
os.chdir(r'D:\AiCore\week4\facebook-marketplaces-recommendation-ranking-system\clean_data\cleaned_images')
import cv2
import numpy as np

def resize_image(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.ANTIALIAS)
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im

def img_channels(im):
    img = cv2.imread(im)
    img_np = np.asarray(img)
    if  img_np.shape[-1] != 3:
        print('failed')




if __name__ == '__main__':
    path = r"C:\Users\a_asf\Desktop\test"
    dirs = os.listdir(path)
    final_size = 512
    for n, item in enumerate(dirs):
        img_path_and_name = 'C:\\Users\\a_asf\\Desktop\\test\\' + item
        im = Image.open('C:\\Users\\a_asf\\Desktop\\test\\' + item)
        img_channels(img_path_and_name)
        #img_channels(im)
        new_im = resize_image(final_size, im)
        new_im.save(f'{n}_resized.jpg')
