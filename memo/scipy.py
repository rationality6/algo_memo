from scipy import interpolate
# choose eight points between 0 and 10
    x = np.linspace(0, 10, 8)
    y = np.sin(x)

    # create a cubic interpolation function
    func = interpolate.interp1d(x, y, kind='cubic')

    # interpolate on a grid of 1,000 points
    x_interp = np.linspace(0, 10, 1000)
    y_interp = func(x_interp)

# plot the results
    plt.figure()
# new figure
    plt.plot(x, y, 'o')
    plt.plot(x_interp, y_interp)
