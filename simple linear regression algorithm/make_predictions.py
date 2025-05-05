# simple linear regression standalone model:
from math import sqrt

# Calculate root mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)

# Evaluate regression algorithm on training dataset:
def evaluate_algorithm(dataset, algorithm):
    # prepare train and test sets
    #train_set = list(dataset)
    test_set = list(dataset)
    for raw in dataset:
        row_copy = list(raw)
        row_copy[-1] = None  # remove the class value from the row copy
        test_set.append(row_copy)
    predicted = algorithm(dataset, test_set)
    print(predicted)
    actual = [row[-1] for row in dataset]
    rmse = rmse_metric(actual, predicted)
    return rmse

# calculate the mean value:
def mean(values):
    return sum(values) / float(len(values))

# covariane :
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# calculate the variance of list of values:
def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values]) / float(len(values) - 1)

# Calculate coefficients:
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    mean_x, mean_y = mean(x), mean(y)
    b1 = covariance(x, mean_x, y, mean_y) / variance(x, mean_x)
    b0 = mean_y - (b1 * mean_x)
    return [b0, b1]

# Simple linear regression algorithm:
def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0 + (b1 * row[0])
        predictions.append(yhat)
    return predictions

# tesing the simple linear regression algorithm:
dataset = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
rmse = evaluate_algorithm(dataset, simple_linear_regression)
print('RMSE: %.3f' % (rmse))




