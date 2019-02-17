import DataPreprocessing
import DataCleaning
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split

vectorizedData = DataPreprocessing.getVectorizedData()
targetY = {}
targetY["postiveReviewsY"] = [1 for i in range(DataCleaning.getCountPostiveReviews())]
targetY["negativeReviewsY"] = [0 for i in range(DataCleaning.getCountNegativeReviews())]
