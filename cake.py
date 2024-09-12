import math
def getCylinderVol(radius, height) :
    volume = math.pi * (radius**2) * height
    return volume

x = getCylinderVol(10, 12)
y = getCylinderVol (2, 6)

print(round(x, 4))
print(round(y,4))

def getNumberOfSlices (radius, height, volOfSlice) :
    volume = getCylinderVol (radius, height)
    slices = volume / volOfSlice
    return int(slices)

slice1 = getNumberOfSlices (10, 10, 100)
print(slice1)