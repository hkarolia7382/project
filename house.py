import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

time.sleep(2)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

oakstiars = 28
bricks = 45
air = 0

def buildhouse(x,y,z):
	mc.setBlocks(x-2,y-1,z,x-14,y+7,z-8,bricks)
	mc.setBlocks(x-3,y,z-1,x-11,y+4,z-7,air)
	mc.setBlocks(x-4,y,z-1,x-4,y+1,z-1,air)
	mc.etBlocks(x-3,y,z-1,x-11,y,z-7,oakstairs)

for space in (x,x+15,x+30,x+45,x+60):
	buildhouse(space,y,z)
