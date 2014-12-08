import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()

# Moves Player Close To Built Object
mc.player.setPos(10,10,0)

black=7
red=14
orange=1
green=5

# Setup Empty Lights
mc.setBlock(0,0,0,35,black)
mc.setBlock(0,1,0,35,black)
mc.setBlock(0,2,0,35,black)
mc.setBlock(0,3,0,35,black)
mc.setBlock(0,4,0,35,black)
mc.setBlock(0,5,0,35,black)
mc.setBlock(0,6,0,35,black)

