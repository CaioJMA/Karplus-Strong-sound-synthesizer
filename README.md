# 🎸 Karplus-Strong Sound Synthesizer

<p align="justify">
Audio synthesis has played a fundamental role in the development of electronic musical instruments and in various signal processing applications. One of the classic synthesis methods is the Karplus-Strong algorithm, introduced in the 1980s, which is notably effective for generating sounds similar to string instruments such as guitars, basses, and harps. This algorithm combines concepts from digital signal processing with feedback and filtering techniques to produce sounds that are both pleasant and realistic.
</p>
<p align="justify">
This project implements and analyzes the Karplus-Strong Algorithm, covering everything from mathematical formulation to the generation of specific musical notes.
</p>

# Difference Equations

<p align="justify">
The difference equation for the Karplus-Strong algorithm is derived considering that the system consists of a short-duration waveform generator and a feedback loop with $$"L"$$ delay units and a gain factor $$α$$.
</p>
<p align="justify">
The Karplus-Strong algorithm can be described in terms of a difference equation that takes into account a delay filter (with a delay of $$"L"$$ samples) and multiplication by a gain $$α$$. The output $$y[n]$$ at a given instant $$"n"$$ depends on the input $$x[n]$$ and on outputs at previous instants.
</p>
<p align="justify">
The difference equation for $$y[n]$$ can be given by:
</p>

$$
y[n] = x[n] + \alpha \cdot y[n - L]
$$

<p align="justify">
The output signal $$y[n]$$ is given by:
</p>

$$
y[n] =
\begin{cases}
\bar{x}[n], & \text{for } 0 \leq n < L \\
\alpha \ \cdot y[n - L], & \text{for } n \geq L
\end{cases}
$$

<p align="justify">
In this context, $$\bar{x}[n]$$ represents the finite-support input signal (duration $$"L"$$), and $$α$$ controls the decay of the signal in the feedback loop. When $$α = 1$$, the signal repeats indefinitely, while values of $$α < 1$$ result in an exponential decay of the signal over time.
</p>
<p align="justify">
From the implementation of the MATLAB codes $$"ImpulseResponse"$$ and $$"FrequencyResponse"$$, it is possible to obtain the Impulse Response, Magnitude $$|H(e^{j\omega})|$$, and Phase $$\theta(e^{j\omega})$$ for specific cases of $$"L"$$ and $$α$$.
</p>

# Signal Synthesis

<p align="justify">
Using the MATLAB code $$"SignalSynthesis"$$, we obtained signals of Sine, Triangle, Square, and Random (with Normal Distribution and Standard Deviation equal to 1) with $$L = 100$$ samples and 10 periods. Using the MATLAB code $$“PlayAudio”$$, it is possible to play the synthesized signals.
</p>
<p align="justify">
Additionally, using the MATLAB code $$"SynthMagnitudePhase"$$, the Magnitude and Phase Responses of each synthesized signal were obtained.
</p>

# Tone Generator and C Major Diatonic Scale

<p align="justify">
Using the MATLAB code $$"RandomSignals"$$, we obtained different waveform plots of the notes C, D, E, F, G, A, B within the A base (220 Hz), simulating the effect of strings through excitation by a random signal. The initial random signal plays a crucial role in the Karplus-Strong method, which is widely used for string sound synthesis in digital signal processing. This method simulates the vibration of a plucked string by using a digital filter based on a sample buffer. The initial random signal, often generated from a sequence of random values, is essential because it represents the initial excitation of the string, imitating the complex and chaotic vibrations that occur when a string is plucked or struck. Thus, using the MATLAB code $$"CScaleDiatonic"$$, it is possible to play the notes of the C Major Diatonic Scale in the 3rd Octave.
</p>

# Graphical Interface

<p align="justify">
The graphical interface, present in the $$“InterfaceGrafica”$$ file, developed in MATLAB using the App Designer, aims to facilitate user interaction with the Karplus-Strong algorithm, allowing the generation and manipulation of the seven notes of the C Major Diatonic Scale in the third octave. The interface consists of buttons corresponding to each of the notes (C, D, E, F, G, A, B), which, when pressed, trigger the playback of the corresponding note through a sound synthesis algorithm.
</p>
<p align="justify">
In addition to the note buttons, the interface includes two numeric controls (spinners) that allow the user to adjust the duration and volume of each note. The duration control sets the time in seconds for which the note will be played, while the volume control adjusts the amplitude of the sound, directly influencing the perceived loudness.
</p>

# Python Codes

<p align="justify">
The Python codes in this project require some libraries, which are listed in the <code>requirements.txt</code> file. All dependencies can be installed at once using the command:
</p>

```bash
pip install -r requirements.txt
