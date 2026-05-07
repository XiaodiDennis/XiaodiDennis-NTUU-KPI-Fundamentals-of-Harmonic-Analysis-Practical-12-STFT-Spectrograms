"""
Task 1. Generate and plot the test signal for STFT analysis.
The signal contains a 5 Hz sinusoid in the first half and a 50 Hz burst in the second half.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from common_stft_utils import (
    FS,
    DURATION,
    LOW_FREQ,
    HIGH_FREQ,
    OUTPUT_DIR,
    generate_test_signal,
    save_console_snapshot,
    save_figure,
)


def main() -> None:
    t, signal_test = generate_test_signal()
    midpoint = len(t) // 2

    plt.figure(figsize=(10, 3.5))
    plt.plot(t, signal_test, linewidth=1.2)
    plt.axvline(DURATION / 2, linestyle='--', linewidth=1.0, label='Transition at 1.0 s')
    plt.title('Time-Domain Test Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend(loc='upper right')
    save_figure(OUTPUT_DIR / 'task1_test_signal.png')

    console_text = f"""Task 1: Generate Test Signal
Sampling frequency: {FS} Hz
Duration: {DURATION:.1f} s
Number of samples: {len(signal_test)}
First half: {LOW_FREQ:.1f} Hz sinusoid, samples 0 to {midpoint - 1}
Second half: {HIGH_FREQ:.1f} Hz sinusoid, samples {midpoint} to {len(signal_test) - 1}
Transition time: {DURATION / 2:.2f} s
Output figure: outputs/task1_test_signal.png"""
    print(console_text)
    save_console_snapshot(console_text, 'task1_console.png')


if __name__ == '__main__':
    main()
