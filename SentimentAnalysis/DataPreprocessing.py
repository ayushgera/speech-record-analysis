import os as os
import fnmatch as fnmatch
import re as regex

REPLACE_WITH_NO_SPACE = regex.compile("(\()|(\,)|(\))|(\–)|(\.)|(\;)|(\!)|(\-)|(<br />)|(\:)|(\“)|(\’)|(\‘)|(\”)|(\')")

filePath = os.path.abspath("../../Dataset/SentimentAnalysis/train/Merged")
trainDataReview = []
for file in os.listdir(os.chdir(filePath)):
    if fnmatch.fnmatch(file, '*.txt'):
        fileContents = open(file, encoding="utf-8")
        content = (regex.sub(REPLACE_WITH_NO_SPACE, "", fileContents.readline()).lower())
        if len(content) != 0:
            trainDataReview.append(content)

print(trainDataReview)