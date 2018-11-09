from App_Main.Backend.DictionaryCard.Translation import Translation
from App_Main.Backend.DictionaryCard.Audio import Audio
from App_Main.Backend.DictionaryCard.RatingG import RatingG
from App_Main.Backend.DictionaryCard.RatingU import RatingU
from App_Main.Backend.DictionaryMaker.DictionaryMaker import DictionaryMaker
from App_Main.Backend.Words.Words_Rating import Words_Rating
from zMA_Test.Backend.app.model import user_word_history


class UserDict(DictionaryMaker):
    """
    Override the factory method to return an instance of a
    ConcreteProduct1.
    """

    def build(self):
        ratings = None

        if (self.query == 'all'):
            ratings = Words_Rating.objects
        else:
            ratings = Words_Rating.objects(wordID__startswith=self.query)

        for r in ratings:
            if(self.dict.get(r.id) is not None):
                self.dict[r.id] = RatingG(self.dict[r.id])
                self.dict[r.id].setData(r.Ratings[0])
            else:
                self.dict[r.id] = RatingG(self.dict[r.id])
                self.dict[r.id].setData(5)

        ratings = user_word_history.objects(username=self.userid)
        if len(ratings) == 0:
            ratings = {}
        else:
            ratings = ratings[0]['status']

        for key, value in self.dict.items():
            if (ratings.get(key) is None):
                self.dict[key] = RatingU(self.dict[key])
                self.dict[key].setData('red')
            else:
                self.dict[key] = RatingU(self.dict[key])
                self.dict[key].setData(ratings[key])

        for w in self.words:
            self.dict[w.wordID] = Translation(self.dict[w.wordID])
            self.dict[w.wordID].setData(w.translations)
            self.dict[w.wordID] = Audio(self.dict[w.wordID])
            self.dict[w.wordID].setData("/words/audio/"+w.word+".mp3")


    def get(self):
        ret = [value.get_dict() for key, value in self.dict.items()]
        return ret

    def setUser(self, id):
        self.userid = id