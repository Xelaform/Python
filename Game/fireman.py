from superwires import games
# import random


def lf():
    fireman_image = games.load_image("fireman_left.bmp", transparent=True)
    pic = games.Sprite(image=fireman_image, x=540, y=440)
    return pic


def rf():
    fireman_image = games.load_image("fireman_right.bmp", transparent=True)
    pic = games.Sprite(image=fireman_image, x=740, y=440)
    return pic


def score():
    score = games.Message(value="00", size=100, color=(0, 0, 0), x=750, y=220, lifetime=0)
    games.screen.add(score)


def kbrd():
    if games.keyboard.is_pressed(games.K_LEFT):
        return print('left')
    elif games.keyboard.is_pressed(games.K_RIGHT):
        return print('right')


# def main():
#    score = 0
#    kbrd()
#    fireman = rot
#    games.screen.add(fireman)



games.init(screen_width=1280, screen_height=720, fps=50)
wall_image = games.load_image("wall.bmp", transparent=False)
games.screen.background = wall_image
kbrd()
games.screen.mainloop()
