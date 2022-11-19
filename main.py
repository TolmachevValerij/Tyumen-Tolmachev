import pygame as pg
a = input()
n = input()

RES = WEDTH, HEIGHT = int(a), int(a)

sc = pg.display.set_mode(RES)


B = (0, 0, 0)
H = (255, 255, 255)


size = int(n)

board = pg.Surface(RES)

for x in range(int(n)):
    for y in range(int(n)):
        if (x + y) % 2 == 0:
            pg.draw.rect(board, B, [size * x, size * y, size, size])
        else:
            pg.draw.rect(board, H, [size * x, size * y, size, size])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    sc.blit(board, (0, 0))

    pg.display.flip()

