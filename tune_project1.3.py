from music21 import *
import random
import datetime
import copy

#add E cadence stuff
#
#Structure - setting up the structure of the piece

newscore=stream.Score()
newtune = stream.Part()

newscore.insert(0, metadata.Metadata())
newscore.metadata.title = 'Random Reel' + ' ' + str(datetime.datetime.now())
newscore.metadata.composer = 'Tunebot 3000'
newscore.insert(newtune)

m1 = stream.Measure()
m2 = stream.Measure()
m3 = stream.Measure()
m4 = stream.Measure()
m5 = stream.Measure()
m6 = stream.Measure()
m7 = stream.Measure()
m8 = stream.Measure()
m9 = stream.Measure()
m10 = stream.Measure()
m11 = stream.Measure()
m12 = stream.Measure()
m13 = stream.Measure()
m14 = stream.Measure()
m15 = stream.Measure()
m16 = stream.Measure()

newtune.append(m1)
newtune.append(m2)        
newtune.append(m3)
newtune.append(m4)
newtune.append(m5)
newtune.append(m6)
newtune.append(m7)
newtune.append(m8)
newtune.append(m9)
newtune.append(m10)        
newtune.append(m11)
newtune.append(m12)
newtune.append(m13)
newtune.append(m14)
newtune.append(m15)
newtune.append(m16)

ts = meter.TimeSignature('4/4')
newtune.insert(0, ts)
ts.beamSequence.partition(2)
ks= key.KeySignature(3)
m1.insert(0, ks)
newtune.makeMeasures()
m1.insert(bar.Repeat(direction='start'))
m8.insert(bar.Repeat(direction='end'))
m9.insert(bar.Repeat(direction='start'))
m16.insert(bar.Repeat(direction='end'))


sl = layout.SystemLayout(isNew=True)
m5.insert(sl)
m9.insert(sl)
m13.insert(sl)


#Vocabulary
#A Stuff

vocab1 = ["A4", "B4", "C#5", "E5"]
vocab2 = ["A4", "B4", "A4", "F#4"]
vocab3 = ["A4", "B4", "C#5", "D5"]

vocab4 = ["A4", "C#5", "E5", "A5"]
vocab5 = ["A4", "C#5", "E5", "C#5"]
vocab6 = ["A4", "C#5", "B4", "C#5"]
vocab7 = ["A4", "C#5", "A4", "D5"]

vocab8 = ["A4", "F#4", "E4", "F#4"]
vocab9 = ["A4", "F#4", "A4", "E4"]
vocab10 = ["A4", "F#4", "A4", "B4"]

vocab11 = ["C#5", "D5", "E5", "A5"]
vocab12 = ["C#5", "E5", "F#5", "A5"]
vocab13 = ["C#5", "E5", "C#5", "A4"]
vocab14 = ["C#5", "D5", "C#5", "B4"]
vocab15 = ["C#5", "E5", "C#5", "A4"]
vocab16 = ["C#5", "B4", "A4", "B4"]
vocab17 = ["C#5", "B4", "C#5", "D5"]
vocab18 = ["C#5", "B4", "C#5", "E5"]

vocab19 = ["E5", "F#5", "A5", "E5"]
vocab20 = ["E5", "F#5", "E5", "C#5"]
vocab21 = ["E5", "D5", "C#5", "B4"]
vocab22 = ["E5", "C#5", "B4", "A4"]
vocab23 = ["E5", "C#5", "E5", "F#5"]
         
vocab24 = ["A5", "E5", "C#5", "A4"]
vocab25 = ["A5", "E5", "C#5", "B4"]
vocab26 = ["A5", "F#5", "E5", "C#5"]


#D Stuff

vocab27 = ["D5", "E5", "F#5", "A5"]
vocab28 = ["D5", "E5", "F#5", "E5"]
vocab29 = ["D5", "F#5", "E5", "D5"]
vocab30 = ["D5", "F#5", "A5", "F#5"]
vocab31 = ["D5", "C#5", "B4", "A4"]
vocab32 = ["D5", "B4", "A4", "D5"]
vocab33 = ["D5", "B4", "A4", "F#4"]
vocab34 = ["D5", "A4", "D5", "F#5"]
vocab35 = ["D5", "A4", "F#5", "D5"]

vocab36 = ["F#5", "E5", "C#5", "B4"]
vocab37 = ["F#5", "E5", "C#5", "E5"]
vocab38 = ["F#5", "E5", "D5", "C#5"]
vocab39 = ["F#5", "A5", "E5", "F#5"]
vocab40 = ["F#5", "A5", "F#5", "E5"]

vocab41 = ["A4", "D5", "F#5", "E5"]
vocab42 = ["A4", "D5", "F#5", "D5"]
vocab43 = ["A4", "D5", "F#5", "A5"]
vocab44 = ["A4", "D5", "F#5", "A4"]

vocab45 = ["A5", "F#5", "D5", "A4"]
vocab46 = ["A5", "F#5", "D5", "F#5"]
vocab47 = ["A5", "F#5", "D5", "F#5"]
vocab48 = ["A5", "F#5", "E5", "D5"]

phrases = [vocab1,vocab2,vocab3,vocab4,vocab5,vocab6,vocab7,vocab8,vocab9,vocab10,vocab11,vocab12,vocab13,vocab14,vocab15,vocab16,vocab17,vocab18,vocab19,vocab20,vocab21,vocab22,vocab23,vocab24,vocab25,vocab26]
phrases2 = [vocab27,vocab28,vocab29,vocab30,vocab31,vocab32,vocab33,vocab34,vocab35,vocab36,vocab37,vocab38,vocab39,vocab40,vocab41,vocab42,vocab43,vocab44,vocab45,vocab46,vocab47,vocab48]

#Write the melody


count =0
measure=0
#randomly chosen measures
#new D material
while measure<16:
        if measure==1 or measure==5 or measure==9 or measure==13:
                vocabchoice = random.randint(0,21)
                while count<4:
                        newtune[measure].append(note.Note(phrases2[vocabchoice][count], type="eighth"))
                        count=count+1
                count=0
                vocabchoice = random.randint(0,21)
                while count<4:
                        newtune[measure].append(note.Note(phrases2[vocabchoice][count], type="eighth"))
                        count=count+1
                count=0
                measure=measure+1
#rephrases bar 1                
        elif measure==4:
                count=2
                while count<10:
                        rephrase=copy.deepcopy(m1)
                        newtune[measure].append(rephrase[count])
                        count=count+1
                count=0
                measure=measure+1

        elif measure==7 or measure==15:
                vocabchoice = random.randint(0,25)
                while count<4:
                        newtune[measure].append(note.Note(phrases[vocabchoice][count], type="eighth"))
                        count=count+1
                newtune[measure].append(note.Note("A", type="half"))
                #vocabchoice = random.randint(0,25)                
                #while count<4:
                        #newtune[measure].append(note.Note(phrases[vocabchoice][count], type="eighth"))
                        #count=count+1
                #newtune[measure].append(note.Note("A", type="half")) 
               	measure=measure+1
               	count=0
#rephrases bar 8               
        elif measure==12:
                count=2
                while count<10:
                        rephrase=copy.deepcopy(m9)
                        newtune[measure].append(rephrase[count])
                        count=count+1
               	measure=measure+1
                count=0
                               
        else:
                vocabchoice = random.randint(0,25)
                while count<4:    
                        newtune[measure].append(note.Note(phrases[vocabchoice][count], type="eighth"))
                        count=count+1       
                count=0
                vocabchoice = random.randint(0,25)                
                while count<4:    
                        newtune[measure].append(note.Note(phrases[vocabchoice][count], type="eighth"))
                        count=count+1       
                count=0
                measure=measure+1




#Print it!
newtune.show('text')
newtune.show()
'''
Problems
- no coherent idea/development
- no consideration for how sets would fit together (wide, angular jumps, etc)
- ends with a final, held tonic

basically, there should be a 4 note melodic idea ending in a half-cadence, then that idea repeated in some way with a final cadence/resolution
'''

        
