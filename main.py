#The video will be of three sizes 5min 8min and 10min
#according to the size of the video we will fetch the images
#images will change every 15 secs
#the images will be saved in the folder named "images"
#the music will be saved in the folder named "music"
import random

vid_lenth = [5,8,10]
def Get_length(lst):
    #type(lst) = list
    return random.choice(lst)

