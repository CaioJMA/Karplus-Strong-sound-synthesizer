import tkinter as tk
import numpy as np
import sounddevice as sd
import threading

# =========================
# Karplus-Strong
# =========================
def karplus_strong(frequency, duration, volume, fs=48000):
    N = int(duration * fs)
    L = int(fs / frequency)
    y = np.zeros(N)
    y[:L] = (2 * np.random.rand(L) - 1) * volume
    for i in range(L, N):
        y[i] = 0.5 * (y[i - L] + y[i - L + 1])
    if np.max(np.abs(y)) > 0:
        y = y / np.max(np.abs(y)) * volume
    return y

# =========================
# Frequências C Major 3ª oitava
# =========================
note_frequencies = {
    'C': 262,
    'D': 294,
    'E': 330,
    'F': 349,
    'G': 392,
    'A': 440,
    'B': 494
}

# =========================
# Tocar nota em thread separada
# =========================
def play_note_thread(note_name):
    freq = note_frequencies[note_name]
    duration = duration_var.get()
    volume = volume_var.get()
    sound = karplus_strong(freq, duration, volume)
    sd.play(sound, 48000)
    sd.wait()

def play_note(note_name):
    # Cada nota toca em uma thread independente para sobreposição
    threading.Thread(target=play_note_thread, args=(note_name,), daemon=True).start()

# =========================
# GUI Tkinter
# =========================
root = tk.Tk()
root.title("Karplus-Strong Synth - Teclado Estilizado")

# Controles de duração e volume
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Duração (s):").grid(row=0, column=0)
duration_var = tk.DoubleVar(value=1.0)
duration_spin = tk.Spinbox(control_frame, from_=0.1, to=5.0, increment=0.1,
                           textvariable=duration_var, width=5)
duration_spin.grid(row=0, column=1, padx=5)

tk.Label(control_frame, text="Volume:").grid(row=0, column=2)
volume_var = tk.DoubleVar(value=1.0)
volume_spin = tk.Spinbox(control_frame, from_=0.0, to=1.0, increment=0.1,
                         textvariable=volume_var, width=5)
volume_spin.grid(row=0, column=3, padx=5)

# =========================
# Teclado estilizado (botões)
# =========================
keys_frame = tk.Frame(root)
keys_frame.pack(pady=10)

white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for i, note in enumerate(white_keys):
    btn = tk.Button(keys_frame, text=note, width=5, height=10,
                    bg='white', fg='black',
                    command=lambda n=note: play_note(n))
    btn.grid(row=0, column=i, padx=1)

# =========================
# Teclado do PC
# =========================
def key_pressed(event):
    key_map = {'a':'C', 's':'D', 'd':'E', 'f':'F', 'g':'G', 'h':'A', 'j':'B'}
    note = key_map.get(event.char)
    if note:
        play_note(note)

root.bind("<Key>", key_pressed)

# =========================
# Instruções
# =========================
instr_label = tk.Label(root, text="Use teclas do PC: A=C, S=D, D=E, F=F, G=G, H=A, J=B")
instr_label.pack(pady=5)

root.mainloop()
