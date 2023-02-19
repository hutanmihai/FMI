from pwn import *
context.log_level = 'error'
context.timeout = 20
inputArray = [
	  ["A78801C00A7890EC04", 
	   "80290AC03805C04806807C01C02", 
	   "A7990AC00A788FFC00A78A79A79A79C03C03C02", 
	   "A61900C00A649FFC00A61A64A64C02C04"]
	, ["1 2 add 3 mul", 
	   "8 7 sub 5 mul 3 div 8 add 2 5 add mul", 
	   "5 8 10 12 add mul mul 5 4 sub sub 55 mul", 
	   "255 255 mul 90 231 mul add 255 sub"]
	, ["x 1 let x 2 add y 10 let y x sub mul", "x 155 let y 255 let x x y mul mul 3 div 17 div", "234 x 15 let x add 23 mul a 100 let a b 15 let b div div"]
	, ["x 2 2 -1 2 -3 4 let x -10 add", "x 2 2 -1 2 -3 4 let -10 add", 
	   "a 4 5 -10 5 8 -10 -9 -100 255 17 -34 -11 21 20 98 17 3 -16 21 -35 131 2 let a 155 sub", 
	   "a 4 5 -10 5 8 -10 -9 -100 255 17 -34 -11 21 20 98 17 3 -16 21 -35 131 2 let 155 sub", 
	   "a 4 5 -10 5 8 -10 -9 -100 55 17 -34 -11 21 20 98 17 3 -16 21 -35 31 2 let a -2 mul", 
	   "a 4 5 -10 5 8 -10 -9 -100 55 17 -34 -11 21 20 98 17 3 -16 21 -35 31 2 let -2 mul",
	   "a 1 3 -15 -37 255 let a -15 div", 
	   "a 1 3 -15 -37 255 let -15 div",
	   "s 4 6 15 -10 27 -3 255 15 9 81 17 -26 28 -34 8 -10 24 25 -1 -2 -65 -31 85 97 -137 62 let s rot90d",
	   "s 4 6 15 -10 27 -3 255 15 9 81 17 -26 28 -34 8 -10 24 25 -1 -2 -65 -31 85 97 -137 62 let rot90d"]]
outputArray = [
	  ["x 1 let x -14 div", 
	   "2 -10 mul 5 div 6 7 add sub", 
	   "y -10 let x 255 let x y y y mul mul sub", 
	   "a -0 let d -255 let a d d sub div"]
	, ["9", "63", "48345", "85560"]
	, ["27", "120125", "954"]
	, ["2 2 -11 -8 -13 -6", "2 2 -11 -8 -13 -6", 
	   "4 5 -165 -150 -147 -165 -164 -255 100 -138 -189 -166 -134 -135 -57 -138 -152 -171 -134 -190 -24 -153", 
	   "4 5 -165 -150 -147 -165 -164 -255 100 -138 -189 -166 -134 -135 -57 -138 -152 -171 -134 -190 -24 -153", 
	   "4 5 20 -10 -16 20 18 200 -110 -34 68 22 -42 -40 -196 -34 -6 32 -42 70 -62 -4", 
	   "4 5 20 -10 -16 20 18 200 -110 -34 68 22 -42 -40 -196 -34 -6 32 -42 70 -62 -4",
	   "1 3 1 2 -17", 
	   "1 3 1 2 -17",
	   "6 4 -65 8 9 15 -31 -10 81 -10 85 24 17 27 97 25 -26 -3 -137 -1 28 255 62 -2 -34 15",
	   "6 4 -65 8 9 15 -31 -10 81 -10 85 24 17 27 97 25 -26 -3 -137 -1 28 255 62 -2 -34 15"]]
points = [
	  [10, 10, 10, 10]
	, [5, 5, 5, 5]
	, [5, 5, 5]
	, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
]

executables = ["./cerinta1", "./cerinta2", "./cerinta3", "./cerinta4"]

estimatedGrade = 0

for taskIndex in range(len(executables)):
	findProcess = process(["find", executables[taskIndex]])
	findResult = findProcess.recv()
	findProcess.kill()
	
	if findResult.replace("\n", "").strip() != executables[taskIndex]:
		print "Executable %s not found!" % executables[taskIndex]
		continue 
		
	print "Task: %s" % executables[taskIndex]
		
	taskInputArray = inputArray[taskIndex]
	taskOutputArray = outputArray[taskIndex]
	taskPoints = points[taskIndex]
	
	for i in range(0, len(taskInputArray)):
		try:
			sh = process(executables[taskIndex])
			sh.sendline(taskInputArray[i])
			line = sh.recvline().replace("\n", "").strip()
			sh.kill()
			
			if line == taskOutputArray[i]:
				estimatedGrade += taskPoints[i]
				
				if taskIndex < 3:
					print "\tTest %d: OK (%dp)" % (i, taskPoints[i]) 
				
				if taskIndex == 3 and i % 2 == 0:
					print "\tTest %d: OK (%dp)" % (i, taskPoints[i]) 
					taskPoints[i + 1] = 0 # already scored
					
				if taskIndex == 3 and i % 2 == 1:
					if taskPoints[i] == 0:
						print "\tTest %d: already scored" % i
					else:
						print "\tTest %d: OK (%dp)" % (i, taskPoints[i])
			else:
				print "\tTest %d failed (0p)" % i 
				print "\t   Input: %s" % taskInputArray[i]
				print "\t   Your output: %s" % line 
				print "\t   Expected output: %s" % taskOutputArray[i]
			
			if taskIndex == 3 and i % 2 == 1:
				print "\t------------------"
		except:
			print "\tTest %d: exception! (0p)" % i
	print "\n"

print "Estimated grade %dp / 100" % (estimatedGrade + 10)
