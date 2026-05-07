"""
Task 2. Compute the standard FFT of the complete signal.
The FFT reveals frequency components but does not show when each component occurs.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

from common_stft_utils import FS, OUTPUT_DIR, generate_test_signal, save_console_snapshot, save_figure


def main() -> None:
    t, signal_test = generate_test_signal()
    n_samples = len(signal_test)
    freqs = fftfreq(n_samples, 1 / FS)
    spectrum = fft(signal_test)

    positive = freqs >= 0
    positive_freqs = freqs[positive]
    magnitude = np.abs(spectrum[positive])

    # Find the most visible low-frequency and high-frequency peaks.
    peak_indices = np.argsort(magnitude)[-8:][::-1]
    peak_lines = []
    for idx in peak_indices:
        if positive_freqs[idx] <= 120:
            peak_lines.append(f"  {positive_freqs[idx]:7.2f} Hz -> magnitude {magnitude[idx]:9.2f}")
    peak_text = "\n".join(peak_lines[:6])

    plt.figure(figsize=(10, 4))
    plt.plot(positive_freqs, magnitude, linewidth=1.2)
    plt.xlim(0, 120)
    plt.title('Standard FFT Magnitude of the Full Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('|S(f)|')
    plt.grid(True)
    save_figure(OUTPUT_DIR / 'task2_standard_fft.png')

    console_text = f"""Task 2: Standard FFT
Number of samples: {n_samples}
Frequency resolution: {FS / n_samples:.3f} Hz
The FFT magnitude contains both the 5 Hz and 50 Hz components.
However, the full-signal FFT does not show that 5 Hz occurs before 1 s
and 50 Hz occurs after 1 s.

Largest positive-frequency components below 120 Hz:
{peak_text}
Output figure: outputs/task2_standard_fft.png"""
    print(console_text)
    save_console_snapshot(console_text, 'task2_console.png', height=4.8)


if __name__ == '__main__':
    main()
