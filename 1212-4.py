#1212-4
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(1,21):
    mc.setBlock(x,y-1,z+i,57)