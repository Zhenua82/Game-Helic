from map import Map
import time
import os
#🟩🌲🎁🏆🚁🏭🌊🔥☁️⚡🧺🧡⬛🏥

MAP_W, MAP_H = 26, 12
TICK_SLEEP = 0.05
TREE_UPDATE = 40
FIRES_UPDATE = 100

field = Map(MAP_W, MAP_H)
field.generate_forest(30, 100)
field.generate_rivers(7)
field.generate_rivers(20)


tick = 1
while True:
    os.system('cls')
    print('TICK', tick)
    field.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRES_UPDATE == 0:
        field.update_fires()


#print()