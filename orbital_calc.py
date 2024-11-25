import math
import numpy as np

# Constants
PI = 3.14159265359  # Pi
G = 6.6743e-11  # Gravitational constant

R_Sun = 696340e3  # Sun's radius [m]
M_Sun = 1.989e30  # Sun's mass [kg]
SIGMA = 5.67e-8  # Stefan-Boltzmann constant [J/K]
T1 = 5721  # Temperature of the first star [K]
T2 = 6100  # Temperature of the second star [K]

def calculate_orbital_parameters():
    """
    Function to calculate orbital parameters for the EZ Hya binary system.
    - Semi-major axis
    - Star masses
    - Orbital period
    """
    a = 2.98 * R_Sun  # Semi-major axis [m]
    M1 = 1.37 * M_Sun  # Mass of the first star [kg]
    M2 = 0.35 * M_Sun  # Mass of the second star [kg]
    M = M1 + M2  # Total mass of the system [kg]
    q = M2 / M1  # Mass ratio

    P = ( ( ( (2 * PI)**2 * a**3 ) / (G * M) )**0.5 )  # Orbital period [s]

    return a, M1, M2, M, q, P

def calculate_orbital_speeds(P, R1, R2):
    """
    Function to calculate orbital speeds of the two stars in the binary system.
    """
    v1 = (2 * PI * R1 / P) / 1000  # Orbital speed of the first star (in km/s)
    v2 = (2 * PI * R2 / P) / 1000  # Orbital speed of the second star (in km/s)

    return v1, v2

def calculate_brightness(R1, R2):
    """
    Function to calculate the brightness of both stars in the binary system.
    """
    B_tot = (4 * PI * R1**2 * SIGMA * T1**4) + (4 * PI * R2**2 * SIGMA * T2**4)  # Total brightness outside eclipse [L]
    B_pri = 4 * PI * (R1**2 - R2**2) * SIGMA * T1**4 + (4 * PI * R2**2 * SIGMA * T2**4)  # Brightness during primary eclipse [L]
    B_sec = 4 * PI * R1**2 * SIGMA * T1**4  # Brightness during secondary eclipse [L]

    return B_tot, B_pri, B_sec

def main():
    R1 = 1.54 * R_Sun  # Radius of the first star [m]
    R2 = 0.85 * R_Sun  # Radius of the second star [m]

    # Calculate orbital parameters
    a, M1, M2, M, q, P = calculate_orbital_parameters()
    print(f'Semi-major axis: {a / 1000:.2f} km')
    print(f'Mass of the first star: {M1:.2e} kg')
    print(f'Mass of the second star: {M2:.2e} kg')
    print(f'Total mass of the system: {M:.2e} kg')
    print(f'Mass ratio: {q:.2f}')
    print(f'Orbital period: {P / 86400:.2f} days')

    # Calculate orbital speeds
    v1, v2 = calculate_orbital_speeds(P, R1, R2)
    print(f'Orbital speed of the first star: {v1:.2f} km/s')
    print(f'Orbital speed of the second star: {v2:.2f} km/s')

    # Calculate brightnesses
    B_tot, B_pri, B_sec = calculate_brightness(R1, R2)
    print(f'Total brightness outside eclipse: {B_tot:.2e} L')
    print(f'Brightness during primary eclipse: {B_pri:.2e} L')
    print(f'Brightness during secondary eclipse: {B_sec:.2e} L')

if __name__ == "__main__":
    main()