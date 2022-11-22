#consider following obserbvation/data.And apply

#out estimated coefficient b0 and b1.(use
# =[0,1,23,4,5,6,7,8,9,11,13]

import numpy as np 
import matplotlib.pyplot as plt

def estimate_coef(x, y):
 #number of observation/point
 n=np.size(x)
 #mean of x and y vector
 m_x=np.mean(x)
 m_y=np.mean(y)

 # caliculating cross-deviation and deviation about x
 ss_xy=np.sum(y*x) - n*m_y*m_x
 ss_xx=np.sum(x*x) - n*m_x*m_x
 # calicuating regression coefficent
 b_1=ss_xy / ss_xx
 b_0=m_y - b_1*m_x 
 return (b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual point as scatter plot
     plt.scatter(x,y,color ="m", marker ="o", s=30)
     #predicted response vector
     y_pred = b[0] + b[1]*x
     #plotting the regression line 
     plt.plot(x, y_pred ,color ="g")
     #putting labels
     plt.xlabel('x')
     plt.ylabel('y')

     # function to show plot
     plt.show()

def main():
     #observation / data
      x =np.array([0,1,2,3,4,5,6,7,8,9,11,13])
      y = np.array([1,3,2,5,7,8,9,10,12,16,18])
     # estimate coefficent
      b = estimate_coef(x, y)
      print("estimat coeffiecent:\nb_0 {} \ \nb_1 = {}".format(b[0],b[1]))

     #plotting regression line
def plot_regresion_line(x, y, b):
if __name__ == "__main__":
         main()




 
