#lookup dict
notes = {"C":1,("C#","Db"):2,"D":3, ("D#","Eb"):4, "E":5, "F":6, ("F#","Gb"):7, "G":8, ("G#","Ab"):9, "A":10, ("A#","Bb"):11, "B":12, "B":0}
#reverse lookup
notesReversed = dict((reversed(item) for item in notes.items()))

#semitone steps 
modes = {"major":(2,2,1,2,2,2,1), "minor":(2,1,1,2,2,2,1)}
modesReversed = dict((reversed(item) for item in modes.items()))


chromatic = 12
offset = [None] * len(modes["major"])
scale = [None] * 7


def getScale(tonic,modeChoice):
	for x in range(0,len(modeChoice)):
		offset[x] = sum(modeChoice[0:x])
		
	for x in range(0,7):
		scale[x] = notesReversed[(notes[tonic] + offset[x])%chromatic]
	print(tonic, modesReversed[modeChoice], " is ", scale)

def printAll():
	for key,value in notes.items():
		getScale(key,modes["major"])
	
printAll()
