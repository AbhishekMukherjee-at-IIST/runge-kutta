import matplotlib.pyplot as plt
from RK4 import RK4
from RK2 import RK2
from euler import euler
import math
import pandas as pd

if __name__ == "__main__":
    # Define the ODE to be solved
    def odeFunction(x, y):
        return math.exp(-x) - (4*y)
    
    # Exact Solution of the ODE solved analytically
    def exactSolution(x):
        return - (x + 1) + (2 * math.exp(x))
    
    initialY = 1
    startX = 0
    endX = 5
    stepSize = 0.01

    Xvalues, YvaluesRK4 = RK4(odeFunction, initialY, startX, endX, stepSize)
    _, YvaluesRK2 = RK2(odeFunction, initialY, startX, endX, stepSize)
    _, YvaluesEuler = euler(odeFunction, initialY, startX, endX, stepSize)

    # Save the results in a dataframe
    df = pd.DataFrame({'X': Xvalues, 'Y (RK4)': YvaluesRK4, 'Y (RK2)': YvaluesRK2, 'Y (Euler)': YvaluesEuler})
    print(df)

    # Plot the results
    printFlags = {
        'RK4': True,
        'RK2': True,
        'Euler': True
    }

    if printFlags['RK4']:
        plt.plot(Xvalues, YvaluesRK4, 'ro', label='Runge-Kutta 4th Order')
    if printFlags['RK2']:
        plt.plot(Xvalues, YvaluesRK2, 'b*', label='Runge-Kutta 2nd Order')
    if printFlags['Euler']:
        plt.plot(Xvalues, YvaluesEuler, 'g^', label='Euler Method (1st Order)')
    
    plt.plot(Xvalues, [exactSolution(x) for x in Xvalues], 'k-', label='Exact Solution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Comparison of ODE solvers')
    plt.grid()
    plt.legend()
    plt.show()

