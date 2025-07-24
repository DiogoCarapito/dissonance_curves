import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dissonance Curves",
    page_icon=":musical_note:",
    layout="wide",
)

st.title("Dissonance Curves")

st.sidebar.header("Settings")

fundamental_frequency = st.sidebar.number_input(
    "Fundamental Frequency (Hz)",
    min_value=20,
    max_value=20000,
    value=1000,
    step=1,
)

overtone_frequency_ratio = st.sidebar.number_input(
    "Overtone Frequency Ratio",
    min_value=0.05,
    max_value=10.0,
    value=1.0,
    step=0.05,
)

overtone_amplitude_decay = st.sidebar.number_input(
    "Overtone Amplitude Decay",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01,
)

overtone_amplitude_decay = np.sqrt(
    overtone_amplitude_decay
)  # Adjust decay to be more visually appealing


def calculate_dissonance(fundamental, overtone_ratio, decay):
    freqs = [fundamental]
    last_freq = fundamental
    while last_freq <= 20000 or len(freqs) < 100:
        last_freq = last_freq + fundamental * overtone_ratio
        freqs.append(int(last_freq))
    amps = [1.0 * (decay**i) for i in range(len(freqs))]
    return freqs, amps


freqs_all, amps_all = calculate_dissonance(
    fundamental_frequency, overtone_frequency_ratio, overtone_amplitude_decay
)


def waveform(freqs, amps, duration=1.0, sample_rate=44100):
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sig = np.zeros_like(time)
    for f, a in zip(freqs, amps):
        sig += a * np.sin(2 * np.pi * f * time)
    return time, sig


time_all, sig_all = waveform(freqs_all, amps_all)

fig_waveform, ax_waveform = plt.subplots()
ax_waveform.plot(time_all[:1000], sig_all[:1000])  # Plot only the first 1000 samples
ax_waveform.set_title("Waveform")
ax_waveform.set_xlabel("Time (s)")
ax_waveform.set_ylabel("Amplitude")
st.pyplot(fig_waveform)

# spectrogram
st.subheader("Spectrogram")
fig_spectrogram, ax_spectrogram = plt.subplots()
Pxx, freqs_spec, bins, im = ax_spectrogram.specgram(
    sig_all, NFFT=1024, Fs=44100, noverlap=512
)
ax_spectrogram.set_title("Spectrogram")
ax_spectrogram.set_xlabel("Time (s)")
ax_spectrogram.set_ylabel("Frequency (Hz)")
ax_spectrogram.set_ylim(0, 22000)  # Limit y-axis to 20 kHz
st.pyplot(fig_spectrogram)

# Large alpha to match your plot
alpha = 32

# Time axis focused on the short duration
time_alpha = np.linspace(0, 1, 1000)

# Heaviside step function (optional since t >= 0)
theta = np.heaviside(time_alpha, 1)

# Define the function
alpha_t = (alpha**2) * time_alpha * np.exp(-alpha * time_alpha) * theta * 440

# Plot
fig_2, ax_2 = plt.subplots(figsize=(10, 5))
ax_2.plot(time_alpha, alpha_t, color="black")
ax_2.set_title(r"$\alpha(t) = \alpha^2 t e^{-\alpha t} \Theta(t)$, $\alpha = 32$")
ax_2.set_xlabel("time")
ax_2.set_ylabel(r"$\alpha(t)$")
st.pyplot(fig_2)

# Compute overtones up to the first octave (<= 2 * fundamental)
octave_limit = fundamental_frequency * 2
freqs_octave = [f for f in freqs_all if f <= octave_limit]
amps_octave = amps_all[: len(freqs_octave)]

# Generate waveform for these overtones
time_octave = np.linspace(0, 0.01, 1000)  # Short time window for clarity
waveform_octave = np.zeros_like(time_octave)
for f_oct, a_oct in zip(freqs_octave, amps_octave):
    waveform_octave += a_oct * np.sin(2 * np.pi * f_oct * time_octave)

# Plot the waveform for fundamental to first octave
st.subheader("Waveform: Fundamental to First Octave")
fig_octave, ax_octave = plt.subplots(figsize=(10, 4))
ax_octave.plot(time_octave, waveform_octave, color="blue")
ax_octave.set_title("Summed Waveform (Fundamental to First Octave)")
ax_octave.set_xlabel("Time (s)")
ax_octave.set_ylabel("Amplitude")
st.pyplot(fig_octave)
