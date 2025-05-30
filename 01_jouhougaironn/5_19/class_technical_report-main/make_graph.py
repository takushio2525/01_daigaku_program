import pandas as pd
import matplotlib.pyplot as plt

# Load the data
bi_result = pd.read_csv("bi_result.csv", header=None)
new_result = pd.read_csv("new_result.csv", header=None)

# Configure the plotting environment
plt.rcParams.update({
    'font.size': 25,
    'font.family': 'Times New Roman',
    'axes.labelsize': 25,
    'axes.titlesize': 25
})

# Create the figure
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# First subplot
axs[0].plot(bi_result.iloc[:, 0], bi_result.iloc[:, 2], '-b', linewidth=2, label='Bisection Method')
axs[0].plot(new_result.iloc[:, 0], new_result.iloc[:, 2], '-r', linewidth=2, label='Newton Method')
axs[0].set_xlabel("Iteration Number: $n$")
axs[0].set_ylabel("Estimate: $x_n$")
axs[0].legend()
axs[0].grid(True)

# Second subplot
axs[1].semilogy(bi_result.iloc[:, 0], bi_result.iloc[:, 1], '-b', linewidth=2, label='Bisection Method')
axs[1].semilogy(new_result.iloc[:, 0], new_result.iloc[:, 1], '-r', linewidth=2, label='Newton Method')
axs[1].set_xlabel("Iteration Number: $n$")
axs[1].set_ylabel("Error: $|x_{n-1} - x_n|$")
axs[1].legend()
axs[1].grid(True)

# Display the plot
plt.tight_layout()
plt.show()
