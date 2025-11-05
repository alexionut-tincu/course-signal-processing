# https://cs.unibuc.ro/~crusu/ps/Procesarea%20Semnalelor%20(PS)%20-%20Laborator%2002.pdf

import numpy as np
import scipy.io.wavfile
import sounddevice as sd

fs = 44100
t1 = np.linspace(0, 1.0, fs, endpoint=False)
s1 = 0.5 * np.sin(2 * np.pi * 400 * t1)
s2 = 0.5 * np.sin(2 * np.pi * 1200 * t1)
combined = np.concatenate([s1, s2])
scipy.io.wavfile.write('ex05.wav', fs, (combined * 32767).astype('int16'))
sd.play(combined, fs)
sd.wait()
