In this machine learning project, we are going to create a rock and mine detection and prediction model for a submarine.
This model will use data from the sonar unit of the submarine to detect objects and predicit them as eitherrocks or mine based on the previous input/trainin data sets.

First we need relevant libraires and tools for the project.
we need: 
numpy
sklearn - train test split, logistic regression
pandas

after that, we have to import the data set file into our model.
Then we can see the data set inside the editor.
If we want to see shape of the data set(number of columns and rows), we can use the shape function.

To understand the data set we can use the fucntions such as: 
1. head() - to get the first columns and rows of the data set.(first look) 
2. shape - to understand the overall shape(number of columns and rows)
3. describe() - to understand the statistical data frames of the data set.

For te easier using capability, we will introduce rocks as 'R' variable and mine as 'M' variable.

After observing the data set, now we are going to create the model.
For this project we have use a 'Logistic Regression model'.

First, we can split the data into training and testing data.
x_test, x_train, y_test, y_train data sets
Usually we will give 80:20 ratio for the training and test data sets when we splitting.

Then we will train our model with the training data.
Then we can create the function to test the accuracy of the data set for training data.

Then we can apply the same functions to our testing data set.

After testing the accuracy, we can start to write the codes for predictions.

