import pygame

n = input()
k = input()
if n.isdigit() and k.isdigit():
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
    n = int(n)
    k = int(k)
    size = n
    n += k * n

    pygame.init()
    sc = pygame.display.set_mode((1200, 900))
    z = 0
    while k > z:
        pygame.draw.circle(sc, colors[z % 3], (n, n), n - z * size)
        z = z + 1

        pygame.display.update()

    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
else:
    print('Неправильный формат ввода')
