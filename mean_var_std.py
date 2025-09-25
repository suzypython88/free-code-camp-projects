
# Create function calculate() to take a list of 9 numbers and return specific statistics
# Project reference at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

# Import libraries 
import numpy as np

# Build function calculate()
def calculate(x):
  if len(x) != 9:
      raise ValueError('List must contain nine numbers.')
  else:
    b = np.array(x).reshape(3,3)
    statistics = {
      "mean": [b.mean(axis=0).tolist(),b.mean(axis=1).tolist(),b.flatten().mean().tolist()],
      "variance": [b.var(axis=0).tolist(),b.var(axis=1).tolist(),b.flatten().var().tolist()],
      "standard deviation": [b.std(axis=0).tolist(),b.std(axis=1).tolist(),b.flatten().std().tolist()],
      "max": [b.max(axis=0).tolist(),b.max(axis=1).tolist(),b.flatten().max().tolist()],
      "min": [b.min(axis=0).tolist(),b.min(axis=1).tolist(),b.flatten().min().tolist()],
      "sum": [b.sum(axis=0).tolist(),b.sum(axis=1).tolist(),b.flatten().sum().tolist()]
    }
  return statistics