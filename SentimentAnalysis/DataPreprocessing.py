from sklearn.feature_extraction.text import CountVectorizer
import DataCleaning
import numpy

def getVectorizedData():
    cleanedData = DataCleaning.getPreProcessedData()
    vectorizedData = {}

    #vectorization - one-hot encoding
    vectorizer = CountVectorizer(binary=True)
    vectorizedData = vectorizer.fit_transform(cleanedData)
    return vectorizedData
