import DataPreprocessing
import DataCleaning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy

vectorizedData = DataPreprocessing.getVectorizedData()
targetY = []
targetYPositive = [1 for i in range(DataCleaning.getCountPostiveReviews())]
targetYNegative = [0 for i in range(DataCleaning.getCountNegativeReviews())]
targetY = targetYPositive + targetYNegative

# Setting train_test split for positive data
x = vectorizedData
y = targetY
xTrainPositive, xTestPositive, yTrainPositive, yTestPositive = train_test_split(x, y, test_size = 0.3)


# Training model
c= [0.01,0.05,0.1, 0.5,1]

for i in c:
    model = LogisticRegression(C=i)
    model.fit(xTrainPositive, yTrainPositive)

    # accuracy
    print("For c = %s"%(i))
    print(round(metrics.accuracy_score(yTestPositive, model.predict(xTestPositive)),4))
    print(float("{0:.4f}".format(metrics.f1_score(yTestPositive, model.predict(xTestPositive), average="weighted"))))

