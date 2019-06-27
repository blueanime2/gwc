from PIL import Image

def load_img(image):
    pic = Image.open(image)
    return pic
def show_img(object):
    object.show()

def save_img(img_object, save_name):
    img_object.save(save_name)

img_object = load_img("rickandmorty.jpg")

show_img(img_object)
save_img(img_object,"rickandmorty2.jpg")


# should return a new Image object with filter applied
# create a new empty list
def obamacon(img_object):
    original_pixl = img_object.getdata()
    intensity =[]
    for i in original_pixl:
    
#  # use for loop to literate through every single pixl
#     # at every pixl sum up every RGB value
#         # use condiionals(IF ELSE statements) and boolean checks to determin which color to change