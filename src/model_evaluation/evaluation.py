import sys
import os

#Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), 'src')))


from model_training import training as tr
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score
)

#We will use some 'dumb' models to see if our model performs better
#For example, if our complex models perform worse than a simple mean of the last 5 day's vol, we are 
#pretty useless.





def evaluate_model(X, y_pred, y_test, model):
    results = {}
    results['model'] = model.class.name
    results['mse'] = mean_squared_error(y_test, y_pred)
    results['mae'] = mean_absolute_error(y_test, y_pred)
    results['r2'] = r2_score(y_test, y_pred)
    return results