"""
Common utilities for Practical 12: Short-Time Fourier Transform and spectrograms.
All functions are intentionally simple and explicit for educational reporting.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

FS = 500
DURATION = 2.0
LOW_FREQ = 5.0
HIGH_FREQ = 50.0


def generate_test_signal(fs: int = FS, duration: float = DURATION) -> tuple[np.ndarray, np.ndarray]:
    """Generate a two-part test signal: 5 Hz first half and 50 Hz second half."""
    t = np.linspace(0.0, duration, int(fs * duration), endpoint=False)
    signal_test = np.zeros_like(t)
    midpoint = len(t) // 2
    signal_test[:midpoint] = np.sin(2 * np.pi * LOW_FREQ * t[:midpoint])
    signal_test[midpoint:] = np.sin(2 * np.pi * HIGH_FREQ * t[midpoint:])
    return t, signal_test


def save_console_snapshot(text: str, filename: str, width: float = 10.5, height: float = 4.0) -> Path:
    """Save terminal-style text as a PNG image for easy inclusion in the report."""
    path = OUTPUT_DIR / filename
    fig = plt.figure(figsize=(width, height))
    ax = fig.add_subplot(111)
    ax.axis('off')
    ax.text(
        0.02,
        0.98,
        text,
        va='top',
        ha='left',
        family='monospace',
        fontsize=10,
        transform=ax.transAxes,
    )
    fig.tight_layout(pad=0.5)
    fig.savefig(path, dpi=180, bbox_inches='tight')
    plt.close(fig)
    return path


def save_figure(path: Path) -> None:
    """Apply common export settings and save the current matplotlib figure."""
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches='tight')
    plt.close()
