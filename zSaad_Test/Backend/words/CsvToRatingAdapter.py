import pandas as pd

from zSaad_Test.Backend.initDB import initDB_Config as Conf
from zSaad_Test.Backend.words.Words_Rating import Words_Rating
import random

class CsvToRatingAdapter():

    def __init__(self,this_word):
        wordID = "" + this_word["word"][0] + "_[" + this_word["word"] + "]"
        Ratings = [1 + random.randint(1, 10) % 10 for i in range(200)]
        self.RatingObj = Words_Rating(wordID=wordID,Ratings = Ratings)

    def save(self):
        self.RatingObj.save()

