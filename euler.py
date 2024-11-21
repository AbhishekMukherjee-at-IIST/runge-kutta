def euler(odeFunction, initialY, startX, endX, stepSize):
    """
    Implements the Euler method to solve the ODE y' = f(t, y)

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
        currentY = currentY + stepSize * odeFunction(currentX, currentY)
        currentX += stepSize

        valuesX.append(currentX)
        valuesY.append(currentY)

    return valuesX, valuesY

if __name__ == "__main__":
    def test_euler():
        import math

        def ode_function(t, y):
            return t + y**2

        initial_value = 1
        start_time = 0
        end_time = 0.2
        step_size = 0.1

        Xvalues, Yvalues = euler(ode_function, initial_value, start_time, end_time, step_size)

        for t, y in zip(Xvalues, Yvalues):
            print(f"t = {t:.2f}, y = {y:.4f}, exact = {math.exp(-2*t):.4f}")

    test_euler()