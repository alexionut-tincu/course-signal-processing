# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import scipy.io.wavfile
import sounddevice as sd

fs = 44100
t = np.linspace(0, 1.0, fs, endpoint=False)
x = 0.5 * np.sin(2 * np.pi * 440 * t)
scipy.io.wavfile.write('ex03.wav', fs, (x * 32767).astype('int16'))
rate, data = scipy.io.wavfile.read('ex03.wav')
sd.play(data, rate)
sd.wait()
