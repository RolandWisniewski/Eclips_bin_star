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

`orbital_calc.py`

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

$$\left( 𝑃=$`\sqrt{(2𝜋)^2𝑎^3/𝐺𝑀`$ \right)$$
 
  Where:
  
  * P is the orbital period,
  * a is the semi-major axis,
  * G is the gravitational constant,
  * M is the total mass of the binary system.
