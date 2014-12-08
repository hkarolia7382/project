import time,mcpi.minecraft as minecraft   #Importing Modules
mc = minecraft.Minecraft.create() #Creating Connection To Minecraft Instance

x = random.randint(-127.7,127.7)
y = random.randint(-127.7,127.7)
z = random.randint(-127.7,127.7)

while True:
	time.sleep(2)
	mc.postToChat("3")
	time.sleep(1)
	mc.postToChat("2")
	time.sleep(1)
	mc.postToChat("1")
	time.sleep(1)
	mc.postToChat("CYA!")
	time.sleep(2)
	mc.postToChat("Teleportation Complete")
	time.sleep(3)

	mc.player.setPos(0,10,60)

