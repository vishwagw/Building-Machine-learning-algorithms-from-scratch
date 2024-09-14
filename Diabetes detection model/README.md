This is a simple machine laerning model that we can use to detect diabetes among patients based on their input data. 
There are many M.L models in the modern world that can perform this activity.
In this project, i am goig to demonstrate the process of creating a supervised learning model from uploading data file to final functions.
This is a step by step proess with descriptions and definitions. So, any one can use this as a laerning project about the world of machine learning.

the process is simple.
I have included the process flowchart sketch wit this document.
process is divided to these main parts:
1. patient data input
2. data pre-processing
3. train-test split
4. out put data and analysing
5. demonstrate the output results.

first we have to import the tools we need to create our model.
important libraies:
numpy
pandas
sklearn

then we are loading the data set with pandas dataframe.
If we want to see the parameters for the data set, we can simply write - d_data.read_csv?

If we want to see the first look of the data set with its first few raws(typically first 5 raws), we can use the head function.
If we want understand the number of columns or raws of the dataset: we can use shape function.

We can classify the non-diabetic and diabetic patients into two labels - 
0 = non-diabetic
1 = diabetic

then we can drop a new column with the label of 'outcome' to separate the data set.

After completing the data strandadization process, we are now ready to train and test the model.

svm = Support Vector Machine classifier

After creating a predictive model, we can get our final output that tells/print whether "This patient does or does not have diabetis."
