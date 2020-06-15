
from os import system
from time import sleep
system('clear')

print('		   ________              __         ___      __ ')
print('		  / ____/ /_  ___  _____/ /__      / (_)____/ /_')
print('		 / /   / __ \/ _ \/ ___/ //_/_____/ / / ___/ __/')
print('		/ /___/ / / /  __/ /__/ ,< /_____/ / (__  ) /_  ')
print('		\____/_/ /_/\___/\___/_/|_|     /_/_/____/\__/  ')
print()
print('‹'+'—'*30+'(Hacking kro pyaar ni)'+'—'*30+'›')
print('‹'+'—'*60+'›')
print(' Author —————› KING')
print(' Credit —————› Sharma G')
print('‹'+'—'*60+'›')
print(' Instagram —————› hacking_with_king')
print(' Github    —————› KING3140')
print('‹'+'—'*60+'›')
file_1=input('[#] Enter file 1 path ≥ ')
file_2=input('[#] Enter file 2 path ≥ ')
bak_up=file_2
try:
	file_1=open(file_1,'r')
	file_2=open(file_2,'a')
except:
	print('file not found')
	quit()


for word in file_1:
	file_2.write(word)
file_1.close()
file_2.close()


final=input('[#] Enter the output file name with extension —————› ')
lines_seen = set() # holds lines already seen
with open(final, "w") as output_file:
	for each_line in open(bak_up,'r'):
		if each_line not in lines_seen: # check if line is not duplicate
			output_file.write(each_line)
			lines_seen.add(each_line)
