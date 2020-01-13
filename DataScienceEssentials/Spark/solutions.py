# solutions.py

import pyspark
from pyspark.sql import SparkSession
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator as MCE


# ---------------------------- Helper Functions ---------------------------- #

def plot_prob4(data, category):
    """
    Helper function that plots the crime and income data from problem 4.

    Parameters:
        data ((n, 3) nparray, dtype=str (or '<U22')); format should be:
            First Column:   borough name
            Second Column:  crime rate (i.e. avg crimes per month)
            Third Column:   category (i.e. minor category) of crime

    Returns: None
    """
    domain = np.arange(len(data))
    fig, ax = plt.subplots()

    # plot number of months with
    p1 = ax.plot(domain, data[:, 1].astype(float) , color='red', label='Months w/ 1+ {}'.format(category))

    # create and plot on second axis
    ax2 = ax.twinx()
    p2 = ax2.plot(domain, data[:, 2].astype(float), color='green', label='Median Income')

    # create legend
    plots = p1 + p2
    labels = [line.get_label() for line in plots]
    ax.legend(plots, labels, loc=0)

    plt.title('Months w/ 1+ {} with Median Income'.format(category))

    plt.show()



# --------------------- Resilient Distributed Datasets --------------------- #

def word_count(filename='data-files/huck_finn.txt'):
    """
    A function that counts the number of occurrences unique occurrences of each
    word. Sorts the words by count in descending order.

    Parameters:
        filename (str): filename or path to a text file

    Returns:
        word_counts (list): list of (word, count) pairs for the 20 most used words
    """
    # start the SparkSession
    spark = SparkSession.builder\
                        .appName("Word Count Solutions")\
                        .getOrCreate()

    # load the file as an RDD
    text_file = spark.sparkContext.textFile(filename)

    # split the RDD into individual words
    text_file = text_file.flatMap(lambda line: line.split())

    # create (word, 1) tuples so that we can count occurrences
    text_file = text_file.map(lambda word: (word, 1))

    # reduce the RDD by each word; i.e. sum the occurrences of each word
    text_file = text_file.reduceByKey(lambda x, y: x + y)

    # sort the RDD in descending order
    text_file = text_file.sortBy(lambda counts: -counts[1])

    # collect the results
    word_counts = text_file.collect()

    # end the SparkSession
    spark.stop()

    return word_counts[:20]

def monte_carlo(n=10**5, parts=6):
    """
    Runs a Monte Carlo simulation to estimate the value of pi.

    Parameters:
        n (int): number of sample points per partition
        parts (int): number of partitions

    Returns:
        pi_est (float): estimated value of pi
    """
    # start the SparkSession
    spark = SparkSession.builder\
                        .appName("Monte Carlo Estimation Solutions")\
                        .getOrCreate()

    # initialize an RDD with n*parts elements and parts partitions
    samples = spark.sparkContext.parallelize(range(n*parts), parts)

    # map each element to a point in [-1, 1]x[-1, 1] and take the norm
    samples = samples.map(lambda x: la.norm(2*np.random.rand(2) - 1))

    # filter the samples to include only those in the unit circle (norm <= 1)
    samples = samples.filter(lambda x: x <= 1)

    # get the number of samples in the unit circle
    samples = samples.count()

    # end the SparkSession
    spark.stop()

    # divide by total samples and multiply by 4 to get the estimate for pi
    pi_est = 4*samples/(n*parts)

    return pi_est


# ------------------------------- DataFrames ------------------------------- #

def titanic_df():
    """
    Extracts various statistics from the titanic dataset. The dataset has the
    following structure:

    Survived | Class | Name | Sex | Age | Siblings/Spouses Aboard | Parents/Children Aboard | Fare

    Returns:

        """
    # start the SparkSession
    spark = SparkSession.builder\
                        .appName("Problem 3 Solutions")\
                        .getOrCreate()

    # load the dataset into a DataFrame
    schema = ('survived INT, pclass INT, name STRING, sex STRING, '
              'age FLOAT, sibsp INT, parch INT, fare FLOAT'
             )
    titanic = spark.read.csv('titanic.csv', schema=schema)

    # how many males/females onboard
    male_count = titanic.filter(titanic.sex == 'male')\
                        .count()

    female_count = titanic.filter(titanic.sex == 'female')\
                          .count()

    # female/male survival rate (sort ensures correct ordering)
    f_surv, m_surv = titanic.groupBy('sex')\
                            .avg('survived')\
                            .sort('sex')\
                            .collect()[0]

    # extract the female and male survival rates from the row objects
    f_sr, m_sr = f_surv[1], m_surv[1]

    return male_count, female_count, f_sr, m_sr


def crime_and_income(f1='london_crime_by_lsoa.csv',
                     f2='london_income_by_borough.csv', min_cat='Murder'):
    """
    Explores crime by borough and income for the specified min_cat

    Parameters:
        f1 (str): path to csv file containing crime dataset
        f2 (str): path to csv file containing income dataset
        min_cat (str): crime minor category to analyze

    returns:
        list: borough names sorted by percent months with crime, descending
    """
    # start the SparkSession
    spark = SparkSession.builder\
                        .appName('London {} and Income Analysis'.format(min_cat))\
                        .getOrCreate()

    # initialize DataFrames from crime file
    crime = spark.read.csv(f1, header=True, inferSchema=True)
    # load f2 into DataFrame and discard 'mean-08-16' column
    income = spark.read.csv(f2, header=True, inferSchema=True)\
                       .select('borough', 'median-08-16')

    # line by line explanation of the following code
        # filter crime to only 'min_cat' entries
        # group crime by borough and average monthly offenses
        # join crime DF with income DF on column 'borough'
        # sort the combined DF by 'avg(value)', descending
        # collect DF into numpy array 'data'

    data = np.array(crime.filter(crime.minor_category==min_cat)\
                         .groupBy('borough').avg('value')\
                         .join(income, on='borough')\
                         .sort('avg(value)', ascending=False)\
                         .collect()
                    )
    # stop the SparkSession
    spark.stop()

    plot_crime_income(data, min_cat)

    return list(data[:, 0])


def titanic_classifier(filename='titanic.csv'):
    """
    Implements a logistic regression to classify the Titanic dataset.

    Parameters:
        filename (str): path to the dataset

    Returns:
        lr_metrics (list): a list of metrics gauging the performance of the model
            ('f1', 'accuracy', 'weightedPrecision', 'weightedRecall')
    """
    # start the SparkSession
    spark = SparkSession.builder\
                        .appName('Titanic Classifier')\
                        .getOrCreate()

    # load the data
    schema = ('survived INT, pclass INT, name STRING, sex STRING, '
              'age FLOAT, sibsp INT, parch INT, fare FLOAT'
             )
    titanic = spark.read.csv('titanic.csv', schema=schema)

    # convert 'sex' column to numbers
    indexer = [StringIndexer(inputCol='sex', outputCol='sex_index').fit(titanic)]
    titanic = Pipeline(stages=indexer).fit(titanic)\
                                      .transform(titanic)

    # drop 'name' and 'sex' column (no longer needed)
    titanic = titanic.drop('name', 'sex')

    # vectorize the features
    feature = VectorAssembler(inputCols=titanic.columns[1:],
                                outputCol='features')

    feature_vector = feature.transform(titanic)

    # split test and train data
    train, test = feature_vector.randomSplit([0.8, 0.2], seed=42)

    # initialize logistic regression object
    lr = LogisticRegression(labelCol='survived', featuresCol='features')

    # train the model
    lr_model = lr.fit(train)

    # make predictions
    lr_preds = lr_model.transform(test)

    # obtain performance metrics
    metrics = ['f1', 'accuracy', 'weightedPrecision', 'weightedRecall']
    lr_eval = MCE(labelCol='survived', predictionCol='prediction')

    lr_metrics = [lr_eval.evaluate(lr_preds, {lr_eval.metricName: metric})
                    for metric in metrics]

    # stop the SparkSession
    spark.stop()

    return lr_metrics
