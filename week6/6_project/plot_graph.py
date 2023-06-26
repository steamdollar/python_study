import matplotlib.pyplot as plt

def plot_graph(data, title, xlabel, ylabel, filename, legends, date_col='Date'):
    plt.figure(figsize=(16, 8))
    plt.title(title)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    plt.plot(data)
    plt.legend(legends, loc='lower right')
    plt.savefig(filename)