# Final Project
# Loops                        2+= 15  1=8  0=0                             4 while                 15 (15)
# Conditionals                 2+= 15  1=8  0=0                             4 ifs 2 else            15 (30)
# Functions                    2+= 20  1=10 0=0                             start, main             20 (50)
# Class                      used= 30 made=5 ignored=0                                               0 (50)
# Lists,dictionaries,tuples    2+= 15  1=8  0=0                             2 dictionaries          15 (65)
# Quality                    high= 20 average=10 poor=0                     ??                      10 (75)

# Using the programming skills you have learned over the course of the class,
# write code that will interact with Minecraft and build a village. In addition to the requirements
# in the rubric for the final you must meet the following criteria.

# At least 4 different types of building; each one a different size;                        x
#    at least one non-square.                                                               x
# At least 3 copies of each building.                                                       x
# Each building must be made of different material, i.e. one of cobblestone,                x
#    one of stone brick and one of brick.
# Each building must have a roof made of material other than that of the base               x
#    building. The stone brick building for example should have a roof of oak wood.
# Buildings must be hollow. (As in filled with air, not solid all the way through.)         x
# There should be a path between the buildings made of gravel or cobblestone                x (sandstone)
# (if you did not use cobblestone for a building).
# Buildings may not be placed in a straight line.
# The entire village must be placed using only Python code.
# You do not need villager npcs.
# Reward: If you manage to do this, and it works: 100 extra points on the final.


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# setting block types to their name in 2 dictionaries
# block for building blocks
block = {'air': 0, 'granite': (1, 1), 'grass': 2, 'lava': 10, 'glass': 20, 'path': 24, 'mossy_brick': 98,
         'cracked': (98, 2), 'trapdoor': 96, 'nether_brick': 112, 'oak_slab': 125, 'path_stair': 128, 'ice': 174}
# roof for roof blocks
roof = {'snow': 35, 'brick_stair': 108, 'red_sand': (179, 1), 'quarts_stair': 156}
# setting items as variables
bed = 26
obsidian = 49
torch = 50
door = 64
ladder = 65

# ALL mc.setBlock are x coordinate, y coordinate, z coordinate, item, item option
# ALL mc.setBlocks are starting (x, y, z), ending (x, y, z) item, item option


def start():
    # set player starting position
    # mc.player.setTilePos(0, 95, 0)

    # set land base
    mc.setBlocks(-100, 50, 100, 100, 70, -100, block['grass'])
    mc.setBlocks(-99, 71, 99, 99, 100, -99, block['air'])
    # build city walls
    mc.setBlocks(-100, 70, 100, 100, 76, 100, block['mossy_brick'])
    mc.setBlocks(-100, 70, -100, -100, 76, 100, block['mossy_brick'])
    mc.setBlocks(100, 70, -100, -100, 76, -100, block['mossy_brick'])
    mc.setBlocks(100, 70, 100, 100, 76, -100, block['mossy_brick'])

    # castle hill
    mc.setBlocks(-30, 71, 30, 30, 71, -30, block['grass'])
    mc.setBlocks(-28, 72, 28, 28, 72, -28, block['grass'])
    mc.setBlocks(-25, 73, 25, 25, 73, -25, block['grass'])
    mc.setBlocks(-20, 73, 20, 20, 73, -20, block['lava'])
    mc.setBlocks(-18, 73, 18, 18, 73, -18, block['grass'])
    mc.setBlocks(-1, 74.5, 18, 1, 74.5, 21, block['trapdoor'])
    mc.setBlocks(-2, 74, 21, -2, 75, 21, block['nether_brick'])
    mc.setBlocks(-2, 74, 18, -2, 75, 18, block['nether_brick'])
    mc.setBlocks(2, 74, 21, 2, 75, 21, block['nether_brick'])
    mc.setBlocks(2, 74, 18, 2, 75, 18, block['nether_brick'])
    mc.setBlock(-2, 76, 21, torch)
    mc.setBlock(-2, 76, 18, torch)
    mc.setBlock(2, 76, 21, torch)
    mc.setBlock(2, 76, 18, torch)


# main function definition
def main():
    # call start function to build our land base
    start()

# CASTLE
    # keep
    mc.setBlocks(-13, 74, 13, 13, 80, -13, block['nether_brick'])
    mc.setBlocks(0, 74, 13, 0, 75, 13, block['air'])
    mc.setBlocks(-1, 74, 13, -1, 75, 13, 95, 3)
    mc.setBlocks(1, 74, 13, 1, 75, 13, 95, 3)
    mc.setBlock(0, 74, 14, door, 1)
    mc.setBlock(0, 75, 14, door, 8)
    mc.setBlock(-2, 76, 14, torch, 3)
    mc.setBlock(2, 76, 14, torch, 3)

    # towers ~ sw
    mc.setBlocks(-15, 74, 15, -12, 85, 12, block['nether_brick'])
    mc.setBlocks(-14, 74, 14, -13, 85, 13, block['air'])
    mc.setBlocks(-13, 74, 13, -12, 76, 12, block['air'])
    mc.setBlocks(-14, 73, 14, -13, 73, 13, block['oak_slab'])
    mc.setBlocks(-13, 73, 13, -12, 73, 12, block['oak_slab'])
    mc.setBlocks(-14, 84, 14, -14, 84, 13, block['oak_slab'])
    mc.setBlock(-13, 84, 13, block['oak_slab'])
    mc.setBlocks(-13, 74, 14, -13, 84, 14, ladder, 4)
    mc.setBlock(-14, 78, 14, torch, 1)
    mc.setBlock(-15, 86, 12, torch)
    mc.setBlock(-12, 86, 12, torch)
    mc.setBlock(-15, 86, 15, torch)
    mc.setBlock(-12, 86, 15, torch)
    #  ~ se
    mc.setBlocks(15, 74, 15, 12, 85, 12, block['nether_brick'])
    mc.setBlocks(14, 74, 14, 13, 85, 13, block['air'])
    mc.setBlocks(13, 74, 13, 12, 76, 12, block['air'])
    mc.setBlocks(14, 73, 14, 13, 73, 13, block['oak_slab'])
    mc.setBlocks(13, 73, 13, 12, 73, 12, block['oak_slab'])
    mc.setBlocks(14, 84, 14, 14, 84, 13, block['oak_slab'])
    mc.setBlock(13, 84, 13, block['oak_slab'])
    mc.setBlocks(13, 74, 14, 13, 84, 14, ladder, 5)
    mc.setBlock(14, 78, 14, torch, 2)
    mc.setBlock(15, 86, 12, torch)
    mc.setBlock(12, 86, 12, torch)
    mc.setBlock(15, 86, 15, torch)
    mc.setBlock(12, 86, 15, torch)
    #  ~ nw
    mc.setBlocks(-15, 74, -15, -12, 85, -12, block['nether_brick'])
    mc.setBlocks(-14, 74, -14, -13, 85, -13, block['air'])
    mc.setBlocks(-13, 74, -13, -12, 76, -12, block['air'])
    mc.setBlocks(-14, 73, -14, -13, 73, -13, block['oak_slab'])
    mc.setBlocks(-13, 73, -13, -12, 73, -12, block['oak_slab'])
    mc.setBlocks(-14, 84, -14, -14, 84, -13, block['oak_slab'])
    mc.setBlock(-13, 84, -13, block['oak_slab'])
    mc.setBlocks(-13, 74, -14, -13, 84, -14, ladder, 4)
    mc.setBlock(-14, 78, -14, torch, 1)
    mc.setBlock(-15, 86, -12, torch)
    mc.setBlock(-12, 86, -12, torch)
    mc.setBlock(-15, 86, -15, torch)
    mc.setBlock(-12, 86, -15, torch)
    #  ~ ne
    mc.setBlocks(15, 74, -15, 12, 85, -12, block['nether_brick'])
    mc.setBlocks(14, 74, -14, 13, 85, -13, block['air'])
    mc.setBlocks(13, 74, -13, 12, 76, -12, block['air'])
    mc.setBlocks(14, 73, -14, 13, 73, -13, block['oak_slab'])
    mc.setBlocks(13, 73, -13, 12, 73, -12, block['oak_slab'])
    mc.setBlocks(14, 84, -14, 14, 84, -13, block['oak_slab'])
    mc.setBlock(13, 84, -13, block['oak_slab'])
    mc.setBlocks(13, 74, -14, 13, 84, -14, ladder, 5)
    mc.setBlock(14, 78, -14, torch, 2)
    mc.setBlock(15, 86, -12, torch)
    mc.setBlock(12, 86, -12, torch)
    mc.setBlock(15, 86, -15, torch)
    mc.setBlock(12, 86, -15, torch)

    # keep inside
    mc.setBlocks(-12, 74, 12, 12, 79, -12, block['air'])
    mc.setBlocks(-12, 73, 12, 12, 73, -12, block['oak_slab'])
    mc.setBlocks(-2, 74, -3, 2, 74, -7, 126)
    mc.setBlocks(-1, 74, -5, 1, 74, -7, block['oak_slab'])
    mc.setBlock(0, 75, -6, 203, 3)
    mc.setBlocks(-1, 75, -6, -1, 75, -7, 204)
    mc.setBlocks(1, 75, -6, 1, 75, -7, 204)
    mc.setBlocks(1, 75, -7, -1, 75, -7, 204)
    mc.setBlocks(1, 76, -7, -1, 76, -7, 205)
    mc.setBlock(0, 78, -7, 138)
    mc.setBlocks(-1, 74, 12, 1, 74, -2, 171, 3)
    mc.setBlocks(-2, 74, 12, -2, 74, -2, 171, 10)
    mc.setBlocks(2, 74, 12, 2, 74, -2, 171, 10)

    mc.setBlocks(-8, 74, 8, -8, 79, 8, block['oak_slab'])
    mc.setBlocks(-9, 76, 8, -9, 79, 8, torch, 2)
    mc.setBlocks(-8, 76, 7, -8, 79, 7, torch, 4)
    mc.setBlocks(-8, 76, 9, -8, 79, 9, torch, 3)
    mc.setBlocks(-7, 76, 8, -7, 79, 8, torch, 1)

    mc.setBlocks(8, 74, -8, 8, 79, -8, block['oak_slab'])
    mc.setBlocks(9, 76, -8, 9, 79, -8, torch, 1)
    mc.setBlocks(8, 76, -7, 8, 79, -7, torch, 3)
    mc.setBlocks(8, 76, -9, 8, 79, -9, torch, 4)
    mc.setBlocks(7, 76, -8, 7, 79, -8, torch, 2)

    mc.setBlocks(8, 74, 8, 8, 79, 8, block['oak_slab'])
    mc.setBlocks(9, 76, 8, 9, 79, 8, torch, 1)
    mc.setBlocks(8, 76, 7, 8, 79, 7, torch, 4)
    mc.setBlocks(8, 76, 9, 8, 79, 9, torch, 3)
    mc.setBlocks(7, 76, 8, 7, 79, 8, torch, 2)

    mc.setBlocks(-8, 74, -8, -8, 79, -8, block['oak_slab'])
    mc.setBlocks(-9, 76, -8, -9, 79, -8, torch, 2)
    mc.setBlocks(-8, 76, -7, -8, 79, -7, torch, 3)
    mc.setBlocks(-8, 76, -9, -8, 79, -9, torch, 4)
    mc.setBlocks(-7, 76, -8, -7, 79, -8, torch, 1)

# main path
    mc.setBlocks(-1, 73, 13, 1, 73, 18, block['path'])
    mc.setBlocks(-1, 73, 21, 1, 73, 25, block['path'])
    mc.setBlocks(-1, 73, 26, 1, 73, 26, block['path_stair'], 3)
    mc.setBlocks(-2, 73, 26, -2, 74, 26, block['nether_brick'])
    mc.setBlock(-2, 75, 26, torch)
    mc.setBlocks(2, 73, 26, 2, 74, 26, block['nether_brick'])
    mc.setBlock(2, 75, 26, torch)
    mc.setBlocks(-1, 72, 27, 1, 72, 28, block['path'])
    mc.setBlocks(-1, 72, 29, 1, 72, 29, block['path_stair'], 3)
    mc.setBlocks(-1, 71, 30, 1, 71, 30, block['path_stair'], 3)
    mc.setBlocks(-1, 70, 31, 1, 70, 33, block['path'])
    mc.setBlocks(-2, 71, 31, -2, 72, 31, block['nether_brick'])
    mc.setBlock(-2, 73, 31, torch)
    mc.setBlocks(2, 71, 31, 2, 72, 31, block['nether_brick'])
    mc.setBlock(2, 73, 31, torch)
    mc.setBlocks(-33, 70, 33, 36, 70, 36, block['path'])
    mc.setBlocks(33, 70, 36, 36, 70, -36, block['path'])
    mc.setBlocks(-34, 70, -36, -36, 70, 36, block['path'])
    mc.setBlocks(33, 70, -36, -36, 70, -33, block['path'])
    # side paths
    mc.setBlocks(57, 70, 16, 33, 70, 16, block['path'])
    mc.setBlocks(67, 70, 62, 67, 70, 36, block['path'])
    mc.setBlocks(67, 70, 36, 33, 70, 36, block['path'])
    mc.setBlocks(47, 70, 48, 47, 70, 36, block['path'])
    mc.setBlocks(27, 70, 66, 27, 70, 36, block['path'])
    mc.setBlocks(14, 70, 48, 14, 70, 36, block['path'])
    mc.setBlocks(-1, 70, 79, -93, 70, 79, block['path'])
    mc.setBlocks(-38, 70, 89, -38, 70, 79, block['path'])
    mc.setBlocks(-10, 70, 79, -10, 70, 36, block['path'])
    mc.setBlocks(-3, 70, 56, -3, 70, 36, block['path'])
    mc.setBlocks(-21, 70, 51, -21, 70, 36, block['path'])
    mc.setBlocks(-49, 70, 18, -49, 70, 21, block['path'])
    mc.setBlocks(-49, 70, 18, -36, 70, 18, block['path'])
    mc.setBlocks(-36, 70, 36, -53, 70, 36, block['path'])
    mc.setBlocks(-53, 70, 36, -53, 70, 49, block['path'])

# 6-walled house 1
    x1 = -1
    x2 = 4
    x3 = -1
    x4 = -4
    x5 = -1
    y = 74
    z = 53
    z2 = 62
    mc.setBlocks(-4, 70, 57, 3, 74, 61, block['oak_slab'])
    mc.setBlocks(0, 70, 54, 3, 74, 57, block['oak_slab'])
    mc.setBlocks(-3, 71, 58, 2, 76, 60, block['air'])
    mc.setBlocks(1, 71, 55, 2, 76, 57, block['air'])
    mc.setBlock(-3, 71, 57, door, 1)
    mc.setBlock(-3, 72, 57, door, 8)
    mc.setBlock(-4, 72, 59, block['glass'])
    mc.setBlock(0, 72, 61, block['glass'])
    mc.setBlock(3, 72, 59, block['glass'])
    mc.setBlock(-1, 72, 57, block['glass'])
    mc.setBlock(1, 71, 55, bed, 10)
    mc.setBlock(1, 71, 56, bed, 2)
    mc.setBlock(0, 73, 60, torch, 4)
    # 6-wall roof
    while y < 77:
        mc.setBlocks(x1, y, z, x2, y, z, roof['brick_stair'], 2)
        mc.setBlocks(x3, y, z+3, x4, y, z+3, roof['brick_stair'], 2)
        mc.setBlocks(x5, y, z+1, x5, y, z+2, roof['brick_stair'], 0)
        mc.setBlocks(x5-4, y, z+3, x5-4, y, z2, roof['brick_stair'], 0)
        mc.setBlocks(x4, y, z2, x2, y, z2, roof['brick_stair'], 3)
        mc.setBlocks(x2, y, z+1, x2, y, z2, roof['brick_stair'], 1)
        x1 += 1
        x2 -= 1
        x3 += 1
        x4 += 1
        x5 += 1
        y += 1
        z += 1
        z2 -= 1
        if y == 77:
            mc.setBlocks(-2, y, 59, 1, y, 59, 44, 4)

# 6-walled house 2
    x1 = -1+30
    x2 = 4+30
    x3 = -1+30
    x4 = -4+30
    x5 = -1+30
    y = 74
    z = 53+10
    z2 = 62+10
    mc.setBlocks(-4+30, 70, 57+10, 3+30, 74, 61+10, block['oak_slab'])
    mc.setBlocks(0+30, 70, 54+10, 3+30, 74, 57+10, block['oak_slab'])
    mc.setBlocks(-3+30, 71, 58+10, 2+30, 76, 60+10, block['air'])
    mc.setBlocks(1+30, 71, 55+10, 2+30, 76, 57+10, block['air'])
    mc.setBlock(-3+30, 71, 57+10, door, 1)
    mc.setBlock(-3+30, 72, 57+10, door, 8)
    mc.setBlock(-4+30, 72, 59+10, block['glass'])
    mc.setBlock(0+30, 72, 61+10, block['glass'])
    mc.setBlock(3+30, 72, 59+10, block['glass'])
    mc.setBlock(-1+30, 72, 57+10, block['glass'])
    mc.setBlock(1+30, 71, 55+10, bed, 10)
    mc.setBlock(1+30, 71, 56+10, bed, 2)
    mc.setBlock(0+30, 73, 60+10, torch, 4)
    # 6-wall roof
    while y < 77:
        mc.setBlocks(x1, y, z, x2, y, z, roof['brick_stair'], 2)
        mc.setBlocks(x3, y, z+3, x4, y, z+3, roof['brick_stair'], 2)
        mc.setBlocks(x5, y, z+1, x5, y, z+2, roof['brick_stair'], 0)
        mc.setBlocks(x5-4, y, z+3, x5-4, y, z2, roof['brick_stair'], 0)
        mc.setBlocks(x4, y, z2, x2, y, z2, roof['brick_stair'], 3)
        mc.setBlocks(x2, y, z+1, x2, y, z2, roof['brick_stair'], 1)
        x1 += 1
        x2 -= 1
        x3 += 1
        x4 += 1
        x5 += 1
        y += 1
        z += 1
        z2 -= 1
        if y == 77:
            mc.setBlocks(-2+30, y, 59+10, 1+30, y, 59+10, 44, 4)

# 6-walled house 3
    x1 = -1+60
    x2 = 4+60
    x3 = -1+60
    x4 = -4+60
    x5 = -1+60
    y = 74
    z = 53-40
    z2 = 62-40
    mc.setBlocks(-4+60, 70, 57-40, 3+60, 74, 61-40, block['oak_slab'])
    mc.setBlocks(0+60, 70, 54-40, 3+60, 74, 57-40, block['oak_slab'])
    mc.setBlocks(-3+60, 71, 58-40, 2+60, 76, 60-40, block['air'])
    mc.setBlocks(1+60, 71, 55-40, 2+60, 76, 57-40, block['air'])
    mc.setBlock(-3+60, 71, 57-40, door, 1)
    mc.setBlock(-3+60, 72, 57-40, door, 8)
    mc.setBlock(-4+60, 72, 59-40, block['glass'])
    mc.setBlock(0+60, 72, 61-40, block['glass'])
    mc.setBlock(3+60, 72, 59-40, block['glass'])
    mc.setBlock(-1+60, 72, 57-40, block['glass'])
    mc.setBlock(1+60, 71, 55-40, bed, 10)
    mc.setBlock(1+60, 71, 56-40, bed, 2)
    mc.setBlock(0+60, 73, 60-40, torch, 4)
    # 6-wall roof
    while y < 77:
        mc.setBlocks(x1, y, z, x2, y, z, roof['brick_stair'], 2)
        mc.setBlocks(x3, y, z+3, x4, y, z+3, roof['brick_stair'], 2)
        mc.setBlocks(x5, y, z+1, x5, y, z+2, roof['brick_stair'], 0)
        mc.setBlocks(x5-4, y, z+3, x5-4, y, z2, roof['brick_stair'], 0)
        mc.setBlocks(x4, y, z2, x2, y, z2, roof['brick_stair'], 3)
        mc.setBlocks(x2, y, z+1, x2, y, z2, roof['brick_stair'], 1)
        x1 += 1
        x2 -= 1
        x3 += 1
        x4 += 1
        x5 += 1
        y += 1
        z += 1
        z2 -= 1
        if y == 77:
            mc.setBlocks(-2+60, y, 59-40, 1+60, y, 59-40, 44, 4)

# Triangle house 1
    x = -17
    x2 = -21
    x4 = -24
    y = 71
    z = 52
    z2 = 58
    while y <= 75 and y > 70:
        mc.setBlocks(x, y, z, x, y, z2, block['cracked'])
        mc.setBlocks(x-1, y, z, x4, y, z, block['cracked'])
        mc.setBlocks(x-1, y, z2, x4, y, z2, block['cracked'])
        x -= 1
        x4 += 1
        if x >= x2:
            y += 1
        else:
            y -= 1
    # triangle roof
    x = -17
    x2 = -21
    y = 71
    z = 52
    z2 = 58
    while y <= 76 and y > 70:
        mc.setBlocks(x+1, y, z-1, x+1, y, z2+1, roof['red_sand'])
        x -= 1
        if x >= x2-1:
            y += 1
        else:
            y -= 1
    # triangle inside
    mc.setBlock(-21, 71, 52, door, 1)
    mc.setBlock(-21, 72, 52, door, 8)
    mc.setBlock(-21, 74, 53, torch, 3)
    mc.setBlock(-21, 74, 57, torch, 4)
    mc.setBlock(-24, 73, 55, block['glass'])
    mc.setBlock(-25, 72, 55, block['glass'])
    mc.setBlock(-18, 73, 55, block['glass'])
    mc.setBlock(-17, 72, 55, block['glass'])
    mc.setBlock(-18, 72, 55, block['air'])
    mc.setBlock(-19, 73, 55, block['air'])
    mc.setBlock(-24, 72, 55, block['air'])
    mc.setBlock(-23, 73, 55, block['air'])
    mc.setBlock(-19, 71, 53, bed, 10)
    mc.setBlock(-19, 71, 54, bed, 2)

    # Triangle house 2
    x = -17-28
    x2 = -21-28
    x4 = -24-28
    y = 71
    z = 52-30
    z2 = 58-30
    while y <= 75 and y > 70:
        mc.setBlocks(x, y, z, x, y, z2, block['cracked'])
        mc.setBlocks(x-1, y, z, x4, y, z, block['cracked'])
        mc.setBlocks(x-1, y, z2, x4, y, z2, block['cracked'])
        x -= 1
        x4 += 1
        if x >= x2:
            y += 1
        else:
            y -= 1
    # triangle roof
    x = -17-28
    x2 = -21-28
    y = 71
    z = 52-30
    z2 = 58-30
    while y <= 76 and y > 70:
        mc.setBlocks(x+1, y, z-1, x+1, y, z2+1, roof['red_sand'])
        x -= 1
        if x >= x2-1:
            y += 1
        else:
            y -= 1
    # triangle inside
    mc.setBlock(-21-28, 71, 52-30, door, 1)
    mc.setBlock(-21-28, 72, 52-30, door, 8)
    mc.setBlock(-21-28, 74, 53-30, torch, 3)
    mc.setBlock(-21-28, 74, 57-30, torch, 4)
    mc.setBlock(-24-28, 73, 55-30, block['glass'])
    mc.setBlock(-25-28, 72, 55-30, block['glass'])
    mc.setBlock(-18-28, 73, 55-30, block['glass'])
    mc.setBlock(-17-28, 72, 55-30, block['glass'])
    mc.setBlock(-18-28, 72, 55-30, block['air'])
    mc.setBlock(-19-28, 73, 55-30, block['air'])
    mc.setBlock(-24-28, 72, 55-30, block['air'])
    mc.setBlock(-23-28, 73, 55-30, block['air'])
    mc.setBlock(-19-28, 71, 53-30, bed, 10)
    mc.setBlock(-19-28, 71, 54-30, bed, 2)

# Triangle house 3
    x = -17+68
    x2 = -21+68
    x4 = -24+68
    y = 71
    z = 52-3
    z2 = 58-3
    while y <= 75 and y > 70:
        mc.setBlocks(x, y, z, x, y, z2, block['cracked'])
        mc.setBlocks(x-1, y, z, x4, y, z, block['cracked'])
        mc.setBlocks(x-1, y, z2, x4, y, z2, block['cracked'])
        x -= 1
        x4 += 1
        if x >= x2:
            y += 1
        else:
            y -= 1
    # triangle roof
    x = -17+68
    x2 = -21+68
    y = 71
    z = 52-3
    z2 = 58-3
    while y <= 76 and y > 70:
        mc.setBlocks(x+1, y, z-1, x+1, y, z2+1, roof['red_sand'])
        x -= 1
        if x >= x2-1:
            y += 1
        else:
            y -= 1
    # triangle inside
    mc.setBlock(-21+68, 71, 52-3, door, 1)
    mc.setBlock(-21+68, 72, 52-3, door, 8)
    mc.setBlock(-21+68, 74, 53-3, torch, 3)
    mc.setBlock(-21+68, 74, 57-3, torch, 4)
    mc.setBlock(-24+68, 73, 55-3, block['glass'])
    mc.setBlock(-25+68, 72, 55-3, block['glass'])
    mc.setBlock(-18+68, 73, 55-3, block['glass'])
    mc.setBlock(-17+68, 72, 55-3, block['glass'])
    mc.setBlock(-18+68, 72, 55-3, block['air'])
    mc.setBlock(-19+68, 73, 55-3, block['air'])
    mc.setBlock(-24+68, 72, 55-3, block['air'])
    mc.setBlock(-23+68, 73, 55-3, block['air'])
    mc.setBlock(-19+68, 71, 53-3, bed, 10)
    mc.setBlock(-19+68, 71, 54-3, bed, 2)

# Round house 1
    mc.setBlocks(-50, 70, 52, -57, 73, 55, block['ice'])
    mc.setBlocks(-51, 70, 51, -56, 73, 56, block['ice'])
    mc.setBlocks(-52, 70, 50, -55, 73, 57, block['ice'])
    mc.setBlock(-53, 71, 50, door, 1)
    mc.setBlock(-53, 72, 50, door, 8)
    mc.setBlocks(-52, 71, 51, -55, 74, 56, block['air'])
    mc.setBlocks(-51, 71, 52, -56, 74, 55, block['air'])
    mc.setBlock(-54, 72, 50, block['glass'])
    mc.setBlock(-57, 72, 54, block['glass'])
    mc.setBlock(-53, 72, 57, block['glass'])
    mc.setBlock(-50, 72, 53, block['glass'])
    mc.setBlock(-56, 73, 52, torch, 3)
    mc.setBlock(-51, 73, 55, torch, 4)
    mc.setBlocks(-52, 71, 51, -55, 71, 56, 171, 7)
    mc.setBlocks(-51, 71, 52, -56, 71, 55, 171, 7)
    mc.setBlock(-51, 71, 52, bed, 10)
    mc.setBlock(-51, 71, 53, bed, 2)
    # round roof
    mc.setBlocks(-49, 74, 51, -58, 74, 56, roof['snow'])
    mc.setBlocks(-51, 74, 49, -56, 74, 58, roof['snow'])
    mc.setBlocks(-50, 74, 50, -57, 74, 57, roof['snow'])
    mc.setBlocks(-52, 75, 52, -55, 75, 55, roof['snow'])
    mc.setBlocks(-53, 76, 53, -54, 76, 54, roof['snow'])

    # Round house 2
    mc.setBlocks(-50+120, 70, 52+13, -57+120, 73, 55+13, block['ice'])
    mc.setBlocks(-51+120, 70, 51+13, -56+120, 73, 56+13, block['ice'])
    mc.setBlocks(-52+120, 70, 50+13, -55+120, 73, 57+13, block['ice'])
    mc.setBlock(-53+120, 71, 50+13, door, 1)
    mc.setBlock(-53+120, 72, 50+13, door, 8)
    mc.setBlocks(-52+120, 71, 51+13, -55+120, 74, 56+13, block['air'])
    mc.setBlocks(-51+120, 71, 52+13, -56+120, 74, 55+13, block['air'])
    mc.setBlock(-54+120, 72, 50+13, block['glass'])
    mc.setBlock(-57+120, 72, 54+13, block['glass'])
    mc.setBlock(-53+120, 72, 57+13, block['glass'])
    mc.setBlock(-50+120, 72, 53+13, block['glass'])
    mc.setBlock(-56+120, 73, 52+13, torch, 3)
    mc.setBlock(-51+120, 73, 55+13, torch, 4)
    mc.setBlocks(-52+120, 71, 51+13, -55+120, 71, 56+13, 171, 7)
    mc.setBlocks(-51+120, 71, 52+13, -56+120, 71, 55+13, 171, 7)
    mc.setBlock(-51+120, 71, 52+13, bed, 10)
    mc.setBlock(-51+120, 71, 53+13, bed, 2)
    # round roof
    mc.setBlocks(-49+120, 74, 51+13, -58+120, 74, 56+13, roof['snow'])
    mc.setBlocks(-51+120, 74, 49+13, -56+120, 74, 58+13, roof['snow'])
    mc.setBlocks(-50+120, 74, 50+13, -57+120, 74, 57+13, roof['snow'])
    mc.setBlocks(-52+120, 75, 52+13, -55+120, 75, 55+13, roof['snow'])
    mc.setBlocks(-53+120, 76, 53+13, -54+120, 76, 54+13, roof['snow'])

    # Round house 3
    mc.setBlocks(-50-40, 70, 52+30, -57-40, 73, 55+30, block['ice'])
    mc.setBlocks(-51-40, 70, 51+30, -56-40, 73, 56+30, block['ice'])
    mc.setBlocks(-52-40, 70, 50+30, -55-40, 73, 57+30, block['ice'])
    mc.setBlock(-53-40, 71, 50+30, door, 1)
    mc.setBlock(-53-40, 72, 50+30, door, 8)
    mc.setBlocks(-52-40, 71, 51+30, -55-40, 74, 56+30, block['air'])
    mc.setBlocks(-51-40, 71, 52+30, -56-40, 74, 55+30, block['air'])
    mc.setBlock(-54-40, 72, 50+30, block['glass'])
    mc.setBlock(-57-40, 72, 54+30, block['glass'])
    mc.setBlock(-53-40, 72, 57+30, block['glass'])
    mc.setBlock(-50-40, 72, 53+30, block['glass'])
    mc.setBlock(-56-40, 73, 52+30, torch, 3)
    mc.setBlock(-51-40, 73, 55+30, torch, 4)
    mc.setBlocks(-52-40, 71, 51+30, -55-40, 71, 56+30, 171, 7)
    mc.setBlocks(-51-40, 71, 52+30, -56-40, 71, 55+30, 171, 7)
    mc.setBlock(-51-40, 71, 52+30, bed, 10)
    mc.setBlock(-51-40, 71, 53+30, bed, 2)
    # round roof
    mc.setBlocks(-49-40, 74, 51+30, -58-40, 74, 56+30, roof['snow'])
    mc.setBlocks(-51-40, 74, 49+30, -56-40, 74, 58+30, roof['snow'])
    mc.setBlocks(-50-40, 74, 50+30, -57-40, 74, 57+30, roof['snow'])
    mc.setBlocks(-52-40, 75, 52+30, -55-40, 75, 55+30, roof['snow'])
    mc.setBlocks(-53-40, 76, 53+30, -54-40, 76, 54+30, roof['snow'])

# Square house
    mc.setBlocks(16, 70, 49, 12, 74, 53, block['granite'])
    mc.setBlocks(15, 71, 50, 13, 75, 52, block['air'])
    mc.setBlocks(15, 70, 50, 13, 70, 52, 1, 4)
    mc.setBlock(14, 71, 49, door, 1)
    mc.setBlock(14, 72, 49, door, 8)
    mc.setBlock(13, 71, 52, torch)
    # square roof
    x = 17
    x2 = 11
    y = 74
    z = 48
    z2 = 54
    while y < 77:
        mc.setBlocks(x, y, z, x2, y, z, roof['quarts_stair'], 2)
        mc.setBlocks(x2, y, z+1, x2, y, z2-1, roof['quarts_stair'], 0)
        mc.setBlocks(x2, y, z2, x, y, z2, roof['quarts_stair'], 3)
        mc.setBlocks(x, y, z+1, x, y, z2-1, roof['quarts_stair'], 1)
        x -= 1
        x2 += 1
        y += 1
        z += 1
        z2 -= 1
        if y == 77:
            mc.setBlock(x, y, z, block['glass'])
    mc.setBlock(14, 72, 53, block['glass'])
    mc.setBlock(16, 72, 51, block['glass'])
    mc.setBlock(12, 72, 51, block['glass'])

    # Square house 2
    mc.setBlocks(16-15, 70, 49+31, 12-15, 74, 53+31, block['granite'])
    mc.setBlocks(15-15, 71, 50+31, 13-15, 75, 52+31, block['air'])
    mc.setBlocks(15-15, 70, 50+31, 13-15, 70, 52+31, 1, 4)
    mc.setBlock(14-15, 71, 49+31, door, 1)
    mc.setBlock(14-15, 72, 49+31, door, 8)
    mc.setBlock(13-15, 71, 52+31, torch)
    # square roof
    x = 17-15
    x2 = 11-15
    y = 74
    z = 48+31
    z2 = 54+31
    while y < 77:
        mc.setBlocks(x, y, z, x2, y, z, roof['quarts_stair'], 2)
        mc.setBlocks(x2, y, z+1, x2, y, z2-1, roof['quarts_stair'], 0)
        mc.setBlocks(x2, y, z2, x, y, z2, roof['quarts_stair'], 3)
        mc.setBlocks(x, y, z+1, x, y, z2-1, roof['quarts_stair'], 1)
        x -= 1
        x2 += 1
        y += 1
        z += 1
        z2 -= 1
        if y == 77:
            mc.setBlock(x, y, z, block['glass'])
    mc.setBlock(14-15, 72, 53+31, block['glass'])
    mc.setBlock(16-15, 72, 51+31, block['glass'])
    mc.setBlock(12-15, 72, 51+31, block['glass'])

    # Square house 3
    mc.setBlocks(16-52, 70, 49+41, 12-52, 74, 53+41, block['granite'])
    mc.setBlocks(15-52, 71, 50+41, 13-52, 75, 52+41, block['air'])
    mc.setBlocks(15-52, 70, 50+41, 13-52, 70, 52+41, 1, 4)
    mc.setBlock(14-52, 71, 49+41, door, 1)
    mc.setBlock(14-52, 72, 49+41, door, 8)
    mc.setBlock(13-52, 71, 52+41, torch)
    # square roof
    x = 17-52
    x2 = 11-52
    y = 74
    z = 48+41
    z2 = 54+41
    while y < 77:
        mc.setBlocks(x, y, z, x2, y, z, roof['quarts_stair'], 2)
        mc.setBlocks(x2, y, z+1, x2, y, z2-1, roof['quarts_stair'], 0)
        mc.setBlocks(x2, y, z2, x, y, z2, roof['quarts_stair'], 3)
        mc.setBlocks(x, y, z+1, x, y, z2-1, roof['quarts_stair'], 1)
        x -= 1
        x2 += 1
        y += 1
        z += 1
        z2 -= 1
        if y == 77:
            mc.setBlock(x, y, z, block['glass'])
    mc.setBlock(14-52, 72, 53+41, block['glass'])
    mc.setBlock(16-52, 72, 51+41, block['glass'])
    mc.setBlock(12-52, 72, 51+41, block['glass'])

    # goloms
    mc.setBlock(14, 71, 32, 42)
    mc.setBlock(14, 72, 32, 42)
    mc.setBlock(15, 72, 32, 42)
    mc.setBlock(13, 72, 32, 42)
    mc.setBlock(14, 73, 32, 86)


main()
