import os as os
import fnmatch as fnmatch
import re as regex

REPLACE_WITH_NO_SPACE = regex.compile("(\()|(\,)|(\))|(\–)|(\.)|(\;)|(\!)|(\-)|(<br />)|(\:)|(\“)|(\’)|(\‘)|(\”)|(\')")

trainDataReviewPositive = []
trainingDataReviewPreprocessed={}

def getPreProcessedData():
    trainingData = []
    filePathPositiveReviews = os.path.abspath("../../Dataset/SentimentAnalysis/train/pos")
    filePathNegtiveReviews = os.path.abspath("../../Dataset/SentimentAnalysis/train/neg")
    trainingDataReviewPreprocessed["trainedPositiveReview"] = preProcessingData(filePathPositiveReviews)
    trainingDataReviewPreprocessed["trainedNegativeReview"] = preProcessingData(filePathNegtiveReviews)
    trainingData = trainingDataReviewPreprocessed["trainedPositiveReview"] + trainingDataReviewPreprocessed["trainedNegativeReview"]
    return trainingData

def preProcessingData(filePath):
    trainDataReview =[]
    for file in os.listdir(os.chdir(filePath)):
        if fnmatch.fnmatch(file, '*.txt'):
            fileContents = open(file, encoding="utf-8")
            content = (regex.sub(REPLACE_WITH_NO_SPACE, "", fileContents.readline()).lower())
            if len(content) != 0:
                trainDataReview.append(content)
    return trainDataReview

def getCountPostiveReviews():
    return len(trainingDataReviewPreprocessed["trainedPositiveReview"])

def getCountNegativeReviews():
    return len(trainingDataReviewPreprocessed["trainedNegativeReview"])