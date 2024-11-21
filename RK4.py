def RK4(odeFunction, initialY, startX, endX, stepSize):
    """
    Implements the 4th order Runge-Kutta method to solve the ODE y' = f(t, y)
    
    Parameters:
        ode_function : function
            The function f(t, y) that defines the ODE
        initial_value : float
            Initial value of y at start_time
        start_time : float
            Initial time
        end_time : float
            Final time
        step_size : float
            Step size

    Returns:
        time_values : list
            List of time values
        solution_values : list
            List of y values corresponding to the time values
    """
    valuesX = [startX]
    valuesY = [initialY]

    currentX = startX
    currentY = initialY
    while currentX < endX:
        k1 = stepSize * odeFunction(currentX, currentY)
        k2 = stepSize * odeFunction(currentX + stepSize/2, currentY + k1/2)
        k3 = stepSize * odeFunction(currentX + stepSize/2, currentY + k2/2)
        k4 = stepSize * odeFunction(currentX + stepSize, currentY + k3)

        currentY = currentY + (k1 + 2*k2 + 2*k3 + k4)/6
        currentX += stepSize

        valuesX.append(currentX)
        valuesY.append(currentY)

    return valuesX, valuesY