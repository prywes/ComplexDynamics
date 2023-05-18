from numpy import complex, array
from PIL import Image, ImageDraw


def mandelbrot(iterations):
    im = Image.new('RGB', (1000, 1000), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for i in range(1000):
        for j in range(1000):

            c1 = (i - 700.0) / 340.0
            c2 = (j - 500.0) / 340.0
            c = complex(c1, c2)
            z = complex(0, 0)
            for k in range(iterations):
                z = z * z + c
                if abs(z) > 2.0:
                    if 0 <= k < 2:
                        draw.point((i, j), fill=(255, 255, 0))
                        break
                    elif 2 <= k < 4:
                        draw.point((i, j), fill=(220, 220, 0))
                        break
                    elif 4 <= k < 6:
                        draw.point((i, j), fill=(180, 180, 0))
                        break
                    elif 6 <= k < 8:
                        draw.point((i, j), fill=(150, 150, 0))
                        break
                    else:
                        draw.point((i, j), fill=(150, 150, 0))
                        break

    return im


def quadraticfilledjuliaset(c1, c2):
    c = complex(c1, c2)
    im = Image.new('RGB', (1000, 1000), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    for i in range(1000):
        for j in range(1000):
            z1 = (i - 500.0) / 340.0
            z2 = -(j - 500.0) / 340.0
            z = complex(z1, z2)
            for k in range(26):
                z = z * z + c
                if abs(z) > 10.0:
                    draw.point((i, j), fill=(256 - (k * 10), 256 - (k * 10), 256 - (k * 10)))
                    break
    return im

#mandelbrot(100).show()

quadraticfilledjuliaset( -1.9,0).show()

