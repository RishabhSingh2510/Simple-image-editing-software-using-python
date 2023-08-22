from PIL import Image , ImageFilter
from PIL.ImageFilter import (
    BLUR,CONTOUR,DETAIL,EDGE_ENHANCE,EDGE_ENHANCE_MORE,EMBOSS,FIND_EDGES,SMOOTH,SMOOTH_MORE,SHARPEN
)
print('IMAGE EDITOR')
print('what you want to do')
i = int(input('1 = blurring\n2 = changing format\n3 = adding filters\n4 = mirror effect\n5 = rotation\n')) #enter the path of the image you want to edit
im = Image.open('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.png')
def B():
    b = int(input('enter the blur value (any positive integer value)'))
    gimage = im.filter(ImageFilter.GaussianBlur(b))
    gimage.show()
    gimage.save('C:\\Users\\ASUS\\Desktop\\college\\python\\blurgoku.png')

def C_F():
    def JPEG() :
        print('converting to jpeg' )
        im.save('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.jpeg')

    def TIFF() :    
        print('converting to tiff')
        im.save('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.tiff')

    def PNG() : 
        print('converting to png')
        im.save('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.png')

    def GIF() :
        print('converting to gif')
        im.save('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.gif')

    def BITMAP() :
        print('converting to bitmap')
        im.save('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.bmp')

    def EPS() :
        print('converting to eps')
        im.save('C:\\Users\\ASUS\\Desktop\\college\\python\\goku.eps')

    a = int(input('1 = to jpeg\n2 = to tiff\n3 = to png\n4 = to gif\n5 = to bitmap\n6 = to eps\n'))

    if a == 1:
        JPEG()
    elif a == 2:
        TIFF()
    elif a == 3:
        PNG()
    elif a == 4:
        GIF()
    elif a == 5:
        BITMAP()
    elif a == 6:
        EPS()
    else :
        print('not possible')

def A_F():
    f = int(input('0 = blur\n1 = contour\n2 = detail\n3 = edge enhance\n4 = edge enhance more\n5 = emboss\n6 = find edges\n7 = smooth\n8 = smooth more\n9 = sharpen\n'))

    def blur():
        im1 = im.filter(BLUR)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def contour():
        im1 = im.filter(CONTOUR)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def detail():
        im1 = im.filter(DETAIL)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def edge_enhance():
        im1 = im.filter(EDGE_ENHANCE)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def edge_enhance_more():
        im1 = im.filter(EDGE_ENHANCE_MORE)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def emboss():
        im1 = im.filter(EMBOSS)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def find_edges():
        im1 = im.filter(FIND_EDGES)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def smooth():
        im1 = im.filter(SMOOTH)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def smooth_more():
        im1 = im.filter(SMOOTH_MORE)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    def sharpen():
        im1 = im.filter(SHARPEN)
        im1.show()
        print('image is saved')
        im1.save('C:\\Users\\ASUS\\Desktop\\college\\python\\filtergoku.png')

    if f == 0:
        blur()

    elif f == 1:
        contour()

    elif f == 2:
        detail()

    elif f == 3:
        edge_enhance()

    elif f == 4:
        edge_enhance_more()

    elif f == 5:
        emboss()

    elif f == 6:
        find_edges()

    elif f == 7:
        smooth()

    elif f == 8:
        smooth_more()

    elif f == 9:
        sharpen()

    else :
        print('not possible')


def M_E():
    m = int(input('1 = mirror at bottom\n2 = mirror at right\n'))

    def vertical():
        out = im.transpose(method=Image.FLIP_TOP_BOTTOM)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\vertical.png')

    def horizontal():
        out = im.transpose(method=Image.FLIP_LEFT_RIGHT)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\horizontal.png')

    if m == 1:
        vertical()
    elif m == 2:
        horizontal()

    else :
        print('not possible')


def R_O():
    r = int(input('1= 45\n2= 90\n3= 135\n4= 180\n5= 225\n6= 270\n7= 315\n8= 360\n'))

    def a():
        angle = 45
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def b():
        angle = 90
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def c():
        angle = 135
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def d():
        angle = 180
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def e():
        angle = 225
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def f():
        angle = 270
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def g():
        angle = 315
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')
    def h():
        angle = 360
        out = im.rotate(angle)
        out.save('C:\\Users\\ASUS\\Desktop\\college\\python\\rotategoku.png')

    if r == 1:
        a()
    elif r == 2:
        b()
    elif r == 3:
        c()
    elif r == 4:
        d()
    elif r == 5:
        e()
    elif r == 6:
        f()
    elif r == 7:
        g()
    elif r == 8:
        h()
    else :
        print('not possible')    


if i == 1:
    B()
elif i == 2:
    C_F()
elif i == 3:
    A_F()
elif i == 4:
    M_E()
elif i == 5:
    R_O()
else :
    print('not supported')