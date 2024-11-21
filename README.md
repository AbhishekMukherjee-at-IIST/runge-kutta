# Runge-Kutta Family of Methods to Solve First-Order Ordinary Differential Equations

## Overview

This repository contains implementations of the Runge-Kutta family of methods to solve systems of first-order ordinary differential equations (ODEs). These methods are widely used in numerical analysis for solving initial value problems.

## Methods Implemented

- **Euler Method (1st Order)**
- **RK2 (Runge-Kutta 2nd Order Method)**
- **RK4 (Runge-Kutta 4th Order Method)**

## Files

- `euler.py`: Implementation of the Euler method.
- `RK2.py`: Implementation of the RK2 method.
- `RK4.py`: Implementation of the RK4 method.
- `main.py`: Example usage of the implemented methods.
- `README.md`: This file.
- `.gitignore`: Git ignore file to exclude unnecessary files from the repository.

## Usage

To use any of the methods, import the corresponding module and call the function with the appropriate parameters. For example, to use the RK4 method:

```python
from rk4 import rk4

# Define the system of ODEs
def f(t, y):
    dydt = -2 * t * y
    return dydt

# Initial conditions
t0 = 0
y0 = 1
t_end = 2
h = 0.1

# Solve the ODE
t_values, y_values = rk4(f, t0, y0, t_end, h)
```

## Requirements

- Python 3.x
- NumPy (for numerical operations)
- Pandas (for handling data in a tabular format)

## Installation

Clone the repository and navigate to the directory:

```sh
git clone https://github.com/yourusername/runge-kutta-methods.git
cd runge-kutta-methods
```

Install the required packages:

```sh
pip install numpy
pip install matplotlib pandas
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

This project was developed as part of the Mathematical Methods in Aerospace Engineering course at the Indian Institute of Space Science and Technology.