def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv') 

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # Create first line of best fit
    # Find the line of best fit by performing linear regression
    fit1 = linregress(y=df['CSIRO Adjusted Sea Level'], x=df['Year'])
    # Set the range of projected x values (i.e. Year) from 1880 to 2050
    x_pred1 = pd.Series([i for i in range(1880, 2050)])
    # Use the slope and intercept to construct the best fit line
    y_pred1 = fit1.intercept + fit1.slope * x_pred1
    # Plotting the best fit line
    plt.plot(x_pred1, y_pred1, color='red', label=f'Best fit line 1')


    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    fit2 = linregress(y=df2['CSIRO Adjusted Sea Level'], x=df2['Year'])
    # Set the range of projected x values (i.e. Year) from 1880 to 2050
    x_pred2 = pd.Series([i for i in range(2000, 2050)])
    # Use the slope and intercept to construct the best fit line for the new prediction
    y_pred2 = fit2.intercept + fit2.slope * x_pred2

    # Plot the second line of best fit
    plt.plot(x_pred2, y_pred2, color='green', label=f'Best fit line 2')
   

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Adding the legend
    plt.legend();

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()