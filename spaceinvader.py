import mcpi.minecraft as minecraft, time

mc = minecraft.Minecraft.create()

for block in (0,2,4,6,8,10):
    mc.setBlock(1,10,block,56)
    time.sleep(1)
    mc.postToChat(block)
    time.sleep(1)

for name in ("George","Malachy"):
    mc.postToChat(name)
