#fibbonaci
#last number + current number = new number
import time
sequence = [1,1]
last = 1
current = 1
freq = input ("how many times do you want the sequence to repeat? ")
freq = int(freq)
for i in range (freq):
    number = 0
    number = last + current + number
    last = current
    current = number
    sequence.append(number)
    print (sequence)
sequence = str(sequence)
f = open ("Sequence.txt","w+")
f.write(sequence)
f.close()

