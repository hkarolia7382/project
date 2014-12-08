import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

wool=35
air=0

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def H(x,y,z):
	mc.setBlocks(x+4,y+2,z,x+4,y+8,z,wool,5)
	mc.setBlocks(x+4,y+5,z,x+8,y+5,z,wool,5)
	mc.setBlocks(x+8,y+2,z,x+8,y+8,z,wool,5)

def Y(x,y,z):
	mc.setBlocks(x+12,y+2,z,x+12,y+8,z,wool,6)
	mc.setBlocks(x+13,y+5,z,wool,6)
	mc.setBlocks(x+14,y+4,z,wool,6)
	mc.setBlocks(x+15,y+3,z,wool,6)
	mc.setBlocks(x+16,y+2,z,wool,6)
	mc.setBlocks(x+14,y+6,z,wool,6
	mc.setBlocks(x+15,y+7,z,wool,6)
	mc.setBlocks(x+16,y+8,z,wool,6)

H(x,y,z)
Y(x,y,z)
