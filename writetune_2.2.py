from music21 import *
import random
import datetime

#Structure - setting up the structure of the piece

newscore = stream.Score()
newscore.definesExplicitSystemBreaks=True
newtune = stream.Part()



newscore.insert(0, metadata.Metadata())
newscore.metadata.title = 'Random Reel' + ' ' + str(datetime.datetime.now())
newscore.metadata.composer = 'Tunebot 3000'
newscore.insert(0,newtune)


m1 = stream.Measure()
m2 = stream.Measure()
m3 = stream.Measure()
m4 = stream.Measure()
m5 = stream.Measure()
m6 = stream.Measure()
m7 = stream.Measure()
m8 = stream.Measure()


newtune.insert(0,m1)
newtune.insert(1,m2)        
newtune.insert(2,m3)
newtune.insert(3,m4)
newtune.insert(4,m5)
newtune.insert(5,m6)
newtune.insert(6,m7)
newtune.insert(7,m8)



ts = meter.TimeSignature('4/4')
m1.insert(0, ts)
ts.beamSequence.partition(2)
ks= key.KeySignature(3)
m1.insert(0, ks)
m8.rightBarline = bar.Barline(style='final', location='right')







#Vocabulary

vocab1 = ["A4", "B4", "C#5", "E5"]
vocab2 = ["A4", "C#5", "E5", "A5"]
vocab3 = ["A5", "E5", "C#5", "A4"]
vocab4 = ["A4", "C#5", "A4", "D5"]
vocab5 = ["C#5", "D5", "C#5", "B4"]
vocab6 = ["E5", "F#5", "A5", "E5"]
vocab7 = ["A4", "F#4", "E4", "F#4"]
vocab8 = ["D5", "A4", "C#5", "A4"]
vocab9 = ["F#5", "E5", "C#5", "B4"]
vocab10 = ["A5", "F#5", "E5", "C#5"]
vocab11 = ["D5", "B4", "A4", "D5"]
vocab12 = ["D5", "E5", "F#5", "A5"]
vocab13 = ["D5", "B4", "A4", "F#4"]
vocab14 = ["A4", "D5", "F#5", "E5"]
vocab15 = ["A4", "D5", "F#5", "A5"]
vocab16 = ["A5", "F#5", "D5", "A5"]
vocab17 = ["A5", "F#5", "E5", "D5"]
vocab18 = ["F#5", "A5", "F#5", "E5"]
vocab19 = ["A4", "B4", "A4", "F#4"]
vocab20 = ["A4", "B4", "C#5", "D5"]
phrases = [vocab1,vocab2,vocab3,vocab4,vocab5,vocab6,vocab7,vocab8,vocab9,vocab10,vocab11,vocab12,vocab13,vocab14,vocab15,vocab16,vocab17,vocab18,vocab19,vocab20]



#Write the melody

count =0
measure=0
while measure<8:
        vocabchoice = random.randint(0,19)
        while count<4:
                newtune[measure].append(note.Note(phrases[vocabchoice][count], type="eighth"))
                (note.Note(phrases[vocabchoice][count], type="eighth"))
                count=count+1
        count=0        
        vocabchoice = random.randint(0,19)
        while count<4:
                
                newtune[measure].append(note.Note(phrases[vocabchoice][count], type="eighth"))
                count=count+1
        
        measure=measure+1
        count=0



#Print it

newscore.show('text')
newscore.show()
'''
Problems
- no coherent idea/development
- no consideration for how sets would fit together (wide, angular jumps, etc)
- no cadences/resolutions

basically, there should be a 4 note melodic idea ending in a half-cadence, then that idea repeated in some way with a final cadence/resolution
'''

        
