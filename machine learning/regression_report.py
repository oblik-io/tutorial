# -*- coding: utf-8 -*-
"""regression_report.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NRmkEOyBQNm-Vx2Hc5M-XogppnJQxy8o
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def regression_report(test_set = None, target = None, predictions = None ):
  """
  Return the calculation of different regression metric
  INPUT
  test_set = test dataset
  target = the target variable as np.array or a list
  prediction = the prediction of the model, np.array or a list
  OUTPUT
  print the dataframe as a table
  return a pandas data.frame

  EXAMPLE USAGE
  import xgboost
  from xgboost import XGBRegressor
  from sklearn.model_selection import train_test_split
  import pandas as pd
  #boston dataset
  data_dir = "https://raw.githubusercontent.com/SalvatoreRa/tutorial/main/datasets/Boston.csv"
  df = pd.read_csv(data_dir)
  #separing the input features from the target variable
  y = df["medv"]
  X = df.drop(["medv"], axis=1)
  #splitting the dataset
  X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 42) 
  # generate an xgboost regression model
  model = XGBRegressor()
  #fit the model
  model.fit(X_train, y_train)
  #predict for the test dataset
  pred = model.predict(X_test)
  _ = regression_report(test_set = X_test, target = y_test, predictions = pred )

  """
  df = pd.DataFrame(columns = ["Metric", "Acronym", "Value"])
  metric_list = ["Mean Square Error", "Root Mean Square Error", "Max Error", "Mean Absolute Error", "Mean squared logarithmic error",
                 "Mean Absolute Percentage Error", "R squared", "adjusted R squared", "Normalized RMSE (range)", "Normalized RMSE (quartile)"]
  acron_list  = ["MAE", "RMSE", "max_err", "MAE", "MSLE", "MAPE", "R2", "adj_R2", "NRMSE", "NRMSE"]
  df["Metric"], df["Acronym"]  = metric_list, acron_list
  df.iloc[0,2] = MSE(target, predictions)
  df.iloc[1,2] = RMSE(target, predictions)
  df.iloc[2,2] = Max_error(target, predictions)
  df.iloc[3,2] = MAE(target, predictions)
  df.iloc[4,2] = MSLE(target, predictions)
  df.iloc[5,2] = MAPE(target, predictions)
  df.iloc[6,2] = R_squared(target, predictions)
  df.iloc[7,2] = adj_R_squared(target, predictions,  n = len(target), k = test_set.shape[1] )
  df.iloc[8,2] = NRMSE(target, predictions)
  df.iloc[9,2] = NRMSE(target, predictions, norm_method = "quartile")
  df1 = df.copy()
  df1["Metric"]= df1.Value.astype("float32").round(decimals = 3)
  print(df1)
  return df


def MSE(y = None, y_hat = None, avg = True ):
    """ Mean Square Error 
    """
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the squared error
    err = [(y[i] - y_hat[i])**2 for i in range(len(y)) ]
    #calculate the mean
    if avg == True:
        err = np.sum(err)/len(y)
    return err

def RMSE(y = None, y_hat = None, avg = True ):
    """ Root Mean Square Error """
    
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the squared error
    err = [(y[i] - y_hat[i])**2 for i in range(len(y)) ]
    err = np.sum(err)/len(y)
    return np.sqrt(err) 

def NRMSE(y = None, y_hat = None, norm_method = "range" ):
    """ Normalized Root Mean Square Error """
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the squared error
    err = [(y[i] - y_hat[i])**2 for i in range(len(y)) ]
    err = np.sum(err)/len(y)
    if norm_method == "range":
      norm_p = max(y) -min(y)
      return np.sqrt(err) /norm_p
    if norm_method == "mean":
      norm_p = np.mean(y)
      return np.sqrt(err) /norm_p
    if norm_method == "st_dev":
      norm_p = np.std(y)
      return np.sqrt(err) /norm_p
    if norm_method == "quartile":
      norm_p = np.quantile(y, 0.75) - np.quantile(y, 0.25)
      return np.sqrt(err) /norm_p

def MAE(y = None, y_hat = None, avg = True):
    """ Mean Absolute Error """
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the absolute error
    err = [np.abs(y[i] - y_hat[i]) for i in range(len(y)) ]
    #calculate the mean
    if avg:
        err = np.sum(err)/len(y)
    return err

def MSLE(y = None, y_hat = None, avg = True):
    """ Mean squared logarithmic error  """
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the squared error
    err = [(np.log(1 + y[i])- np.log(1 + y_hat[i]))**2 for i in range(len(y)) ]
    #calculate the mean
    if avg:
        err = np.sum(err)/len(y)
    return err

def RMSLE(y = None, y_hat = None):
    """ Root Mean Squared Logarithmic Error  """
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the squared error
    err = [(np.log(1 + y[i])- np.log(1 + y_hat[i]))**2 for i in range(len(y)) ]
    err = np.sum(err)/len(y)
    err = np.sqrt(err) #square root
    return err

def MAPE(y = None, y_hat = None, avg = True ):
    """ Mean Absolute Percentage Error  """
    y = np.array(y)
    y_hat = np.array(y_hat)
    epsilon = np.finfo(np.float64).eps
    err = np.abs(y_hat - y) / np.maximum(np.abs(y), epsilon)
    #calculate the mean
    if avg:
        err = np.sum(err)/len(y)
    return err

def R_squared(y = None, y_hat = None):
    """ Calculate R squared """
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the squared error and sum it
    se = [(y[i] - y_hat[i])**2 for i in range(len(y)) ]
    se = np.sum(se)
    #calculate the squared difference from the mean
    mean = np.mean(y)
    sd = [(y[i] - mean)**2 for i in range(len(y)) ]
    sd = np.sum(sd)
    #calculater R2
    err = 1 - (se/sd)
    return err

def adj_R_squared(y = None, y_hat = None, n = 1, k = 1):
  """ calculate adjusted r squared
      n = number of examples in the dataset
      k = number of features in the dataset """
  err = R_squared(y , y_hat)
  num = (1 - err)* (n-1) #calculate the numerator
  den = (n -k -1) #calculate the denominator
  err = 1 -(num/den)
  return err

def Max_error(y = None, y_hat = None):
    y = np.array(y)
    y_hat = np.array(y_hat)
    #calculate the absolute error
    err = [np.abs(y[i] - y_hat[i]) for i in range(len(y)) ]
    #calculate the maximum
    return np.max(err)


