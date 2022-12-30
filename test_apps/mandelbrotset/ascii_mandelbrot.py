
X_MIN = -2
X_MAX = 1
Y_MIN = -1
Y_MAX = 1
RESL = 100
MAX_ITER = 200


def is_stable(complex_num, iterations=MAX_ITER):
    z = 0+0j
    for i in range(iterations):
        z = z*z + complex_num
        if abs(z) > 2:
            return False

    return True


mandelbrot_str = ''
re_x = []
im_y = []

for n in range(X_MIN * RESL, X_MAX * RESL + 1):
    re_x.append(n / RESL)

for n in range(Y_MIN * RESL, Y_MAX * RESL + 1):
    im_y.append(n / RESL)

for y in im_y:
    for x in re_x:
        c = complex(x, y)
        if is_stable(c):
            mandelbrot_str += '#'
        else:
            mandelbrot_str += ' '
    mandelbrot_str += '\n'

with open('pic.txt', 'w') as f:
    f.write(mandelbrot_str)
