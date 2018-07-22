import level

debug1 = level.Level()
debug1.id = 1
debug1.set_background("img/bg.png")
debug1.next_level = 2
debug1.add_wall(250, 200, 50, 200)
debug1.add_wall(350, 200, 50, 200)
debug1.add_wall(175, 150, 300, 10)

debug2 = level.Level()
debug2.id = 2
debug2.set_background("img/bg2.png")
debug2.next_level = 3
