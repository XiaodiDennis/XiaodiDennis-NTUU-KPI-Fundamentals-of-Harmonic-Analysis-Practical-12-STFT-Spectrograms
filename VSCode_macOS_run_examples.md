# Practical 12 - VS Code on macOS Run Examples

## 1. Open the folder in VS Code

Unzip the package, then open the folder `Practical12_Xiaodi_Wang_package` in VS Code.

## 2. Open the integrated terminal

In VS Code:

`Terminal` -> `New Terminal`

## 3. Create and activate a virtual environment

```bash
cd /path/to/Practical12_Xiaodi_Wang_package
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 4. Run each task separately

```bash
python3 task1_generate_test_signal.py
python3 task2_standard_fft.py
python3 task3_compute_stft.py
python3 task4_time_frequency_tradeoff_analysis.py
```

## 5. What to screenshot

Take screenshots of:

1. The terminal after each script runs successfully.
2. The generated PNG files inside the `outputs` folder.
3. The file list showing the separated task scripts.

## 6. Main output files

- `outputs/task1_test_signal.png`
- `outputs/task1_console.png`
- `outputs/task2_standard_fft.png`
- `outputs/task2_console.png`
- `outputs/task3_stft_window_256.png`
- `outputs/task3_stft_window_32.png`
- `outputs/task3_stft_comparison.png`
- `outputs/task3_console.png`
- `outputs/task4_tradeoff_summary.png`
- `outputs/task4_console.png`

## 7. Clean screenshot-friendly example

```bash
cd /path/to/Practical12_Xiaodi_Wang_package
source .venv/bin/activate
python3 task3_compute_stft.py
```

This command prints the window-resolution comparison and saves the long-window and short-window STFT figures.
