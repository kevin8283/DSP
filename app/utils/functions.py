import numpy as np

def sine_wave(A, f, phi, t):
    """
    Generate a sine wave.

    Parameters:
        A: Amplitude
        f: Frequency
        phi: Phase
        t: Time

    Returns:
        y: Sine wave
    """
    return A * np.sin(2 * np.pi * f * t + phi)