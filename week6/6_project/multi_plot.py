import matplotlib.pyplot as plt
import pandas as pd

def plot_multi_graph(historical_data, future_predictions, title, x_label, y_label, save_as, legend_labels):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot historical data
    for attr in historical_data.columns:
        ax.plot(historical_data.index, historical_data[attr], label=f'Historical {attr}')
        
    # Plot future predictions
    for attr in future_predictions.columns:
        ax.plot(future_predictions.index, future_predictions[attr], label=f'Future {attr}', linestyle='dashed')
    
    # Add labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    
    # Add legend
    ax.legend()
    
    # Save the plot to file
    plt.savefig(save_as)
    
    # Show the plot
    plt.show()

# Example usage:

# Generating future dates
# last_date = pd.Timestamp(df.index[-1]).to_pydatetime()
# future_dates = [last_date + timedelta(days=i+1) for i in range(future_days)]

# # Construct DataFrame for future_predictions (assuming future_predictions is a 2D array with 4 columns: Open, High, Low, Close)
# future_predictions_df = pd.DataFrame(future_predictions, columns=['Open', 'High', 'Low', 'Close'], index=future_dates)

# # Historical data
# historical_data = df.filter(['Open', 'High', 'Low', 'Close'])

# # Call the function
# plot_multi_graph(historical_data, future_predictions_df, 'Stock Price Prediction', 'Date', 'Price USD ($)', 'multi_pred.png', ['Historical Data', 'Future Predictions'])
