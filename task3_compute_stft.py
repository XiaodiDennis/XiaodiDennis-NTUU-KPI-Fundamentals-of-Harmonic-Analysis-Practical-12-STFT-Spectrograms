"""
Task 3. Compute STFT spectrograms using long and short Hann windows.
The result demonstrates the time-frequency trade-off of fixed-window STFT.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

from common_stft_utils import FS, OUTPUT_DIR, generate_test_signal, save_console_snapshot, save_figure


def _plot_single_stft(frequencies, times, zxx, title, filename):
    magnitude = np.abs(zxx)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(times, frequencies, magnitude, shading='gouraud')
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.ylim(0, 100)
    plt.colorbar(label='Magnitude')
    save_figure(OUTPUT_DIR / filename)


def main() -> None:
    _, signal_test = generate_test_signal()
    window_lengths = [256, 32]
    summary_lines = []

    stft_results = {}
    for win_len in window_lengths:
        noverlap = win_len // 2
        frequencies, times, zxx = stft(
            signal_test,
            fs=FS,
            window='hann',
            nperseg=win_len,
            noverlap=noverlap,
            boundary=None,
        )
        stft_results[win_len] = (frequencies, times, zxx)
        delta_t = (win_len - noverlap) / FS
        delta_f = FS / win_len
        summary_lines.append(
            f"Window {win_len:3d}: window duration = {win_len / FS:.3f} s, "
            f"hop = {delta_t:.3f} s, frequency bin spacing = {delta_f:.3f} Hz"
        )
        _plot_single_stft(
            frequencies,
            times,
            zxx,
            f'STFT Magnitude with Hann Window = {win_len} Samples',
            f'task3_stft_window_{win_len}.png',
        )

    # Combined comparison figure for the report.
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    for ax, win_len in zip(axes, window_lengths):
        frequencies, times, zxx = stft_results[win_len]
        mesh = ax.pcolormesh(times, frequencies, np.abs(zxx), shading='gouraud')
        ax.set_title(f'STFT Magnitude, Hann Window = {win_len} Samples')
        ax.set_ylabel('Frequency (Hz)')
        ax.set_ylim(0, 100)
        ax.grid(False)
        fig.colorbar(mesh, ax=ax, label='Magnitude')
    axes[-1].set_xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'task3_stft_comparison.png', dpi=180, bbox_inches='tight')
    plt.close()

    console_text = """Task 3: STFT with Long and Short Windows
""" + "\n".join(summary_lines) + """

Interpretation:
- The 256-sample window gives better frequency resolution but weaker time localization.
- The 32-sample window gives better time localization but broader frequency peaks.
Output figures:
  outputs/task3_stft_window_256.png
  outputs/task3_stft_window_32.png
  outputs/task3_stft_comparison.png"""
    print(console_text)
    save_console_snapshot(console_text, 'task3_console.png', height=4.8)


if __name__ == '__main__':
    main()
