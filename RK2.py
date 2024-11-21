def RK2(odeFunction, initialY, startX, endX, stepSize):
    """
    Implements the 2nd order Runge-Kutta method to solve the ODE y' = f(t, y)
    
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
        k2 = stepSize * odeFunction(currentX + stepSize, currentY + (k1 * stepSize))
        
        currentY = currentY + (k1 + k2)/2
        currentX += stepSize

        valuesX.append(currentX)
        valuesY.append(currentY)

    return valuesX, valuesY