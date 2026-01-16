# 🎸 Karplus-Strong Sound Synthesizer

<p align="justify">
Audio synthesis plays a fundamental role in the development of electronic musical instruments and in various signal processing applications. One of the classic synthesis methods is the Karplus-Strong algorithm, introduced in the 1980s, which is highly effective for generating sounds similar to string instruments such as guitars, bass guitars, and harps. This algorithm combines concepts from digital signal processing with feedback and filtering techniques to produce realistic and pleasant sounds.
</p>
<p align="justify">
This project implements and analyzes the Karplus-Strong algorithm, covering everything from the mathematical formulation to the generation of specific musical notes.
</p>

# Difference Equations

<p align="justify">
The difference equation for the Karplus-Strong algorithm is derived by considering that the system consists of a short-duration waveform generator and a feedback loop with $$L$$ delay units and a gain factor $$\alpha$$.
</p>
<p align="justify">
The output $$y[n]$$ at a given time step $$n$$ depends on the input $$x[n]$$ and the outputs at previous time steps. The algorithm can be described using a difference equation that incorporates a delay filter (with a delay of $$L$$ samples) and multiplication by the gain $$\alpha$$.
</p>
<p align="justify">
The difference equation for $$y[n]$$ is given by:
</p>

$$
y[n] = x[n] + \alpha \cdot y[n - L]
$$

<p align="justify">
More specifically, the output signal $$y[n]$$ is:
</p>

$$
y[n] =
\begin{cases}
\bar{x}[n], & \text{for } 0 \leq n < L \\
\alpha \cdot y[n - L], & \text{for } n \geq L
\end{cases}
$$

<p align="justify">
Here, $$\bar{x}[n]$$ represents the finite-support input signal of duration $$L$$, and $$\alpha$$ controls the decay of the signal in the feedback loop. When $$\alpha = 1$$, the signal repeats indefinitely; values of $$\alpha < 1$$ result in an exponential decay over time.
</p>
<p align="justify">
Using the MATLAB codes "ImpulseResponse" and "FrequencyResponse", it is possible to obtain the Impulse Response, Magnitude $$|H(e^{j\omega})|$$, and Phase $$\theta(e^{j\omega})$$ for specific values of $$L$$ and $$\alpha$$.
</p>

# Signal Synthesis

<p align="justify">
The MATLAB code "SignalSynthesis" was used to generate signals of Sine, Triangle, Square, and Random types (with Normal Distribution and standard deviation equal to 1), with $$L = 100$$ samples and 10 periods. The code "PlayAudio" allows the synthesized signals to be played.
</p>
<p align="justify">
Additionally, using the MATLAB code "SynthMagnitudePhase", the Magnitude and Phase Responses of each synthesized signal were obtained.
</p>

# Tone Generator and C Major Diatonic Scale

<p align="justify">
The MATLAB code "RandomSignals" was used to generate waveform plots of the notes C, D, E, F, G, A, B using A4 (220 Hz) as the reference pitch, simulating string excitation via a random input signal. The initial random signal is crucial in the Karplus-Strong method, as it simulates the excitation of a plucked string through a digital filter with a sample buffer. By using "CScaleDiatonic", the notes of the C Major Diatonic Scale in the 3rd octave can be played.
</p>

# Graphical Interface

<p align="justify">
The graphical interface, implemented in "KarplusStrongGUI" (MATLAB - App Designer, Python - Tkinter), facilitates user interaction with the Karplus-Strong algorithm. Users can generate and manipulate the seven notes of the C Major Diatonic Scale in the third octave. Each note is triggered via a dedicated button. In addition, two numeric controls (spinners) allow users to adjust the duration and volume of each note.
</p>

# MATLAB Codes

<p align="justify">
All MATLAB codes were developed and tested using **MATLAB 2024a**.
</p>

# Python Codes

<p align="justify">
All Python codes were developed and tested using **Python 3.13.3**.
</p>

<p align="justify">
Also, the Python codes in this project require additional libraries, which are listed in the <code>requirements.txt</code> file. All dependencies can be installed at once in your Python environment using the following command:
</p>

```bash
pip install -r requirements.txt
