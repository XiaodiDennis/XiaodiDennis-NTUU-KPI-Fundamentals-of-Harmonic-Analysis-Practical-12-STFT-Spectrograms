"""
Task 4. Analyze the STFT time-frequency trade-off quantitatively.
This task summarizes why window length controls time and frequency resolution.
"""
from __future__ import annotations

import matplotlib.pyplot as plt

from common_stft_utils import FS, OUTPUT_DIR, save_console_snapshot, save_figure


def main() -> None:
    window_lengths = [256, 32]
    rows = []
    for win_len in window_lengths:
        noverlap = win_len // 2
        window_duration = win_len / FS
        hop_duration = (win_len - noverlap) / FS
        frequency_spacing = FS / win_len
        rows.append((win_len, window_duration, hop_duration, frequency_spacing))

    fig, ax = plt.subplots(figsize=(11.5, 4.1))
    ax.axis('off')
    table_data = [
        ['Window length', 'Window duration', 'Hop duration', 'Frequency spacing', 'Main consequence'],
        [
            f'{rows[0][0]} samples',
            f'{rows[0][1]:.3f} s',
            f'{rows[0][2]:.3f} s',
            f'{rows[0][3]:.3f} Hz',
            'Better frequency resolution;\npoorer time localization',
        ],
        [
            f'{rows[1][0]} samples',
            f'{rows[1][1]:.3f} s',
            f'{rows[1][2]:.3f} s',
            f'{rows[1][3]:.3f} Hz',
            'Better time localization;\npoorer frequency resolution',
        ],
    ]
    table = ax.table(
        cellText=table_data,
        loc='center',
        cellLoc='center',
        colWidths=[0.15, 0.16, 0.16, 0.18, 0.35],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1, 2.15)
    for (r, c), cell in table.get_celld().items():
        if r == 0:
            cell.set_text_props(weight='bold')
        cell.set_linewidth(0.6)
    ax.set_title('STFT Time-Frequency Trade-Off Summary', fontsize=13, weight='bold', pad=12)
    save_figure(OUTPUT_DIR / 'task4_tradeoff_summary.png')

    console_text = f"""Task 4: Time-Frequency Trade-Off Analysis
Sampling frequency: {FS} Hz

Long window ({rows[0][0]} samples):
  window duration = {rows[0][1]:.3f} s
  hop duration = {rows[0][2]:.3f} s
  frequency spacing = {rows[0][3]:.3f} Hz
  interpretation = high frequency resolution but smeared time localization

Short window ({rows[1][0]} samples):
  window duration = {rows[1][1]:.3f} s
  hop duration = {rows[1][2]:.3f} s
  frequency spacing = {rows[1][3]:.3f} Hz
  interpretation = high time resolution but blurred frequency localization

This confirms the STFT fixed-resolution limitation: improving time resolution reduces frequency resolution, and vice versa.
Output figure: outputs/task4_tradeoff_summary.png"""
    print(console_text)
    save_console_snapshot(console_text, 'task4_console.png', height=5.4)


if __name__ == '__main__':
    main()
