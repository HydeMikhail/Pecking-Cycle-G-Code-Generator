'''
This script generates a pecking drill cycle
based on the inputs given by the user. The
generated g code will be stored in the

Q:\\MILLING PROGRAMS

directory.
'''

surfaceDepth = round(float(input('Distance From Tool Tip to Top Surface (in) ::: ')), 3)
print('\n')
holeDepth = round(float(input('Relative Depth of Hole (in) ::: ')), 3)
print('\n')
retractLevel = round(float(input('Depth Below Top Surface for Tool Retraction (in) ::: ')), 3)
print('\n')
stepDown = round(float(input('Step Down (in) ::: ')), 3)
print('\n')
feedRate = round(float(input('Feed Rate (ipm) ::: ')), 3)
print('\n')
fileName = input('Enter File Name ::: ')


f = open(fileName+'.txt', 'w+')
f.write('N10 M03\n')
f.write('N20 G04 K2\n')
f.write('N30 G90 G00 Z0\n')

currentDepth = 0
currentStep = 40

f.write('N'+str(currentStep)+' G00 Z-'+str(round(surfaceDepth-.005, 3))+'\n')
currentStep += 10
currentDepth = surfaceDepth

while currentDepth < surfaceDepth + holeDepth:

    if currentDepth + stepDown > surfaceDepth + holeDepth:
        f.write('N'+str(currentStep)+' G01 Z-'+str(round(surfaceDepth + holeDepth, 3))
                +' F'+str(feedRate)+'\n')
        currentStep += 10
        break

    f.write('N'+str(currentStep)+' G01 Z-'+str(round(currentDepth+stepDown+.005, 3))
            +' F'+str(feedRate)+'\n')
    currentStep += 10
    currentDepth += stepDown
    temp = currentDepth
    f.write('N'+str(currentStep)+' G00 Z-'+str(round(surfaceDepth+retractLevel, 3))+'\n')
    currentStep += 10
    currentDepth = surfaceDepth + retractLevel
    f.write('N'+str(currentStep)+' G00 Z-'+str(round(float(temp)-.005, 3))+'\n')
    currentStep += 10
    currentDepth = temp - .005

f.write('N'+str(currentStep)+' G00 Z0\n')
currentStep += 10
f.write('N'+str(currentStep)+' M05\n')
currentStep += 10
f.write('N'+str(currentStep)+' M02\n')

f.close()
