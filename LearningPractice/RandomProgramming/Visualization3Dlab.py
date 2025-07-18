


import numpy as np
# %matplotlib widget
import matplotlib.pyplot as plt
from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl
plt.style.use('seaborn-v0_8-darkgrid')

#print(plt.style.available)

#You would like a model which can predict housing prices given the size of the house.
#Let's use the same two data points as before the previous lab- a house with 1000 square feet sold for $300,000 and a house with 2000 square feet sold for $500,000.

x_train = np.array([1000, 2000])           #square feet)
y_train = np.array([300000, 500000])           #dollars)


# x_train is the input variable (size in square feet)
# y_train is the target (dollars)


def compute_cost(x, y, w, b): 
    """
    Computes the cost function for linear regression.
    
    Args:
      x (ndarray (m,)): Data, m examples 
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters  
    
    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    # number of training examples
    m = x.shape[0] 
   

    cost_sum = 0 
    for i in range(m): 
        f_wb = w * x[i] + b   
        cost = (f_wb - y[i]) ** 2  
        cost_sum = cost_sum + cost  
    total_cost = (1 / (2 * m)) * cost_sum  

    return total_cost

plt.clf()  # Clear the current figure

plt_intuition(x_train,y_train)

#b = 4.38

# m is the number of training examples



# You will use (x (𝑖), y (𝑖) to denote the  𝑖𝑡ℎ training example. Since Python is zero indexed, (x (0), y (0)) is (1.0, 300.0) and (x (1) , y (1) ) is (2.0, 500.0).

# To access a value in a Numpy array, one indexes the array with the desired offset. For example the syntax to access location zero of x_train is x_train[0]. Run the next code block below to get the  𝑖𝑡ℎ
  # training example.
