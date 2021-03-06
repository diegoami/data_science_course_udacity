import numpy
import pandas

import numpy
import pandas

def normalize_features(array):
    array_normalized = (array-array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()
    
    return array_normalized, mu, sigma



def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    theta_flipped = numpy.array(theta).reshape(numpy.size(theta,1),numpy.size(theta,0))
    features_flipped = numpy.array(features).reshape(numpy.size(features,1),numpy.size(features,0))
    sum_of_square_errors = numpy.square(numpy.dot(theta, features_flipped)- values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """
    count = 0
    cost_history = []
    m = len(values)
    values_flipped = numpy.array(values).reshape(numpy.size(values,1),numpy.size(values,0))
    while count < num_iterations:
        if theta is not None:
            theta_flipped = numpy.array(theta).reshape(numpy.size(theta,1),numpy.size(theta,0))
            predicted_values = numpy.dot(features,theta_flipped)
            theta = theta - (alpha / m ) * numpy.dot((predicted_values - values_flipped),features) 
        else:
            theta = - (alpha / m) * numpy.dot(-values_flipped,features)
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
        count = count+1
    return theta, pandas.Series(cost_history)


data = pandas.read_csv('baseball_data.csv')
features = data[['height','weight']].fillna(0)
values = data[['avg']].fillna(0)
m = len(values)

#values = numpy.array(values)


result = gradient_descent(features, values,None, +0.00000001, 5000)
print(result[1])
print(result[0])
