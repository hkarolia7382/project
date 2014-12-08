import mcpi.minecraft as minecraft,time,random #Importing the moduels for use
mc = minecraft.Minecraft.create() #Creating a link to the minecraft instance

mc.setBlocks(-30,-5,-30,30,30,30,0) #Sets all blocks within set radius to air

for blocks in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14): #14 blocks are set to fifferent colours of wool
	mc.postToChat(blocks)
	mc.setBlock(0,blocks,0,35,blocks)
	time.sleep(2)
