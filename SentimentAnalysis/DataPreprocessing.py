from sklearn.feature_extraction.text import CountVectorizer
import DataCleaning

def getVectorizedData():
    cleanedData = DataCleaning.getPreProcessedData()
    vectorizedData = {}
    #vectorization - one-hot encoding
    vectorizer = CountVectorizer(binary=True)
    vectorizedData["vectorizedPositiveData"] = vectorizer.fit_transform(cleanedData["trainedPositiveReview"])
    vectorizedData["vectorizedDataNegative"] = vectorizer.fit_transform(cleanedData["trainedNegativeReview"])
    return vectorizedData
