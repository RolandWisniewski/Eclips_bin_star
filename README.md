# Analysis of EZ Hydrae Binary System

This project analyzes the EZ Hydrae (EZ Hya) binary star system, which is a contact eclipsing binary system. A contact eclipsing binary consists of two stars orbiting each other in such a way that one star partially obscures the other during their orbit, causing periodic dips in observed brightness. This type of variability in brightness is what makes these stars so interesting to astronomers, as it allows for detailed studies of their masses, sizes, and other physical parameters. The analysis here focuses on calculating the **orbital period**, **orbital velocities**, and **brightness variations** during eclipses.

The code is split into two main scripts:
1. `date_calc.py`: Calculates and predicts the next eclipses for the system based on a given observation date.
2. `orbital_calc.py`: Computes the orbital parameters of the system, including the semi-major axis, masses of the stars, orbital speeds, and brightness.

## Binary Star System Overview

The EZ Hya system is a binary star system, meaning it consists of two stars orbiting around a common center of mass. The stars in this system are typical examples of contact eclipsing binaries, where the orbital plane is aligned in such a way that the stars periodically eclipse each other. This results in noticeable periodic dips in brightness that can be used to derive key parameters of the system, such as the **orbital period**, **orbital velocity**, and **luminosity**.

The periodic dimming caused by these eclipses is the key feature that makes studying these systems so useful. By observing the light curves (graphs of brightness over time) of such systems, astronomers can infer the sizes, masses, and distances of the stars, as well as the geometry of their orbits.

## Files

### `date_calc.py`

This script calculates the dates of the next eclipses in the EZ Hya system based on the initial eclipse date and the orbital period. The script takes the observation date from the user and returns the next 10 predicted eclipses after that date.

**Functions:**

* `get_date_from_user(prompt)`: Prompts the user to input a date in the `DD-MM-YYYY` format and ensures it's in the correct format.
* `calc_next_eclipse(p, m0)`: Calculates the Julian Date (JD) of the next eclipse based on the orbital period (`p`) and the initial eclipse date (`m0`).
* `main()`: Main function that calls the necessary functions to get the observation date and display the next 10 predicted eclipses.

### `orbital_calc.py`

This script computes various orbital parameters for the EZ Hya system using Kepler's third law and other formulas. It calculates the system's **semi-major axis**, **masses** of the stars, **orbital period**, **orbital speeds**, and **brightness** of the stars during the eclipses.

**Functions:**

* `calculate_orbital_parameters()`: Calculates key orbital parameters:
  * Semi-major axis of the orbit
  * Masses of the stars
  * Orbital period of the binary system
  * Mass ratio of the two stars
* `calculate_orbital_speeds(P, R1, R2)`: Computes the orbital speeds of both stars based on the orbital period and their radii.
* `calculate_brightness(R1, R2)`: Calculates the brightness of the system during different phases of the eclipses (total, primary, and secondary).

### **Key Equations and Concepts:**
The calculations in the code rely on fundamental principles of orbital mechanics and stellar astrophysics:
* **Kepler's Third Law**: This law relates the orbital period of a binary system to the semi-major axis of the orbit and the total mass of the system. It’s used to calculate the orbital period (P) of the stars in the system.

$$P=\sqrt{\frac{(2\pi)^{2}a^{3}}{GM}}$$
 
  Where:
  
  * $P$ is the orbital period,
  * $a$ is the semi-major axis,
  * $G$ is the gravitational constant,
  * $M$ is the total mass of the binary system.

* **Orbital Speed**: The speed of each star in its orbit is determined by its distance from the center of mass and the orbital period. The orbital speed is calculated using:

$$v=\frac{2\pi R}{P}$$

Where $R$ is the radius of the star’s orbit and $P$ is the orbital period.

* **Brightness Calculation**: The total luminosity of a star is calculated using the **Stefan-Boltzmann law**:

$$B=4\pi R^{2}\sigma T^{4}$$

Where:

* $B$ is the brightness,
* $R$ is the radius of the star,
* $σ$ is the Stefan-Boltzmann constant,
* $T$ is the temperature of the star.

Brightness variations are calculated for different phases of the eclipse (total, primary, and secondary).

## Requirements
* Python 3.x
* `juliandate` library (Install using `pip install juliandate`)
* `numpy` library (Install using `pip install numpy`)

## Usage

### 1. Running `date_calc.py`:

This script allows you to input a date and calculates the next 10 predicted eclipses for the EZ Hya binary system. It will display the predicted dates and times (in UT1) of the next eclipses starting from the date you provide.

Example:

```bash
$ python date_calc.py
Enter observation date (DD-MM-YYYY):
01-01-2025
Next eclipse: 05-01-2025 02:34:21
Next eclipse: 08-01-2025 02:34:21
...
```

### 2. Running `orbital_calc.py`:
This script computes the key orbital parameters and brightness of the stars in the EZ Hya system. It uses Kepler's third law, orbital speed calculations, and Stefan-Boltzmann's law to compute the system’s characteristics.

Example:

```bash
$ python orbital_calc.py
Semi-major axis: 2070.52 km
Mass of the first star: 2.74e+30 kg
Mass of the second star: 6.87e+29 kg
Total mass of the system: 3.42e+30 kg
Mass ratio: 0.25
Orbital period: 0.45 days
Orbital speed of the first star: 173.17 km/s
Orbital speed of the second star: 511.77 km/s
Total brightness outside eclipse: 1.23e+28 L
Brightness during primary eclipse: 4.56e+27 L
Brightness during secondary eclipse: 1.23e+28 L
```

## Contributing

Feel free to fork this project, report issues, or submit pull requests with improvements or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
