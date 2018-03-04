import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import gc


spf = wave.open('30.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

stereo = signal
slen = len(stereo)
monoSampled = []
#sampleAmount=1
if isinstance(signal[0], list):
    for x in range(0, slen):#, sampleAmount
        sample = 0
        #for i in range(0,sampleAmount):
            #if x+i == slen:
            #    break
        sample += (stereo[x][0]+stereo[x][1])/2#x+i
        #sample = sample / sampleAmount
        monoSampled.extend([sample])
    signal = monoSampled
Time=np.linspace(0, len(signal)/fs, num=len(signal))

gc.collect()
print(len(signal))
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()
