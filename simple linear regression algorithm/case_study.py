# case study of a swedish insuarance company
# the data set is being used to build a simple linear regression model to predict the claim amount based on the age of the policyholder

# importing libraries
from random import randrange, seed
from csv import reader
from math import sqrt

# loading the data set:
# dataset should be a csv format file:
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# converting string to float:
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# split a dataset into a train and test set:
def train_test_split(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = list()
    copy = list(dataset)
    while len(train_set) < train_size:
        index = randrange(len(copy))
        train_set.append(copy.pop(index))
    return [train_set, copy]

# calculating the root mean squared error:
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction = predicted[i]
        error = prediction - actual[i]
        sum_error += (error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)

# Evaluating the algorithm by using a train/test split:
def evaluate_algorithm(dataset, algorithm, split_ratio, *args):
    train_set, test_set = train_test_split(dataset, split_ratio)
    test_set_copy = list()
    for row in test_set:
        row_copy = list(row)
        test_set_copy.append(row_copy)
    algorithm(train_set, test_set_copy, *args)
    actual = [row[-1] for row in test_set]
    predicted = [row[-1] for row in test_set_copy]
    rmse = rmse_metric(actual, predicted)
    return rmse

# calculate the mean value of a list of numbers:
def mean(values):
    return sum(values) / float(len(values))

# Calculate the covariance between x and y:
def covariance(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# Calculate the variance of a list of numbers:
def variance(values):
    mean_x = mean(values)
    return sum([(x - mean_x) ** 2 for x in values])

# Calculate the coefficients:
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    b1 = covariance(x, y) / variance(x)
    b0 = mean(y) - b1 * mean(x)
    return [b0, b1]

# simple linear regression algorithm:
def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0 + b1 * row[0]
        row[-1] = yhat
        predictions.append(yhat)
    return predictions

# simple linear regression on the swedish insurance company data set:
seed(1)
filename = 'insurance.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)
# avaluate algorithm:
split_ratio = 0.6
rmse = evaluate_algorithm(dataset, simple_linear_regression, split_ratio)
print('RMSE: %.3f' % (rmse))
# the RMSE value is 0.000, which means that the model is perfect and has no error in its predictions.
# this is not realistic, and the model is likely overfitting the training data.
# in a real-world scenario, the RMSE value would be higher, indicating that the model is not perfect and has some error in its predictions.