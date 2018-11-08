from zSaad_Test.Backend.words.Words_Rating import Words_Rating


def show_test_stat(status):
    correct = 0
    wrong = 0

    for the_key, the_value in status.items():
        if the_value[1] == the_value[0]:
            correct += 1
        else:
            wrong += 1
    return correct, wrong


def rating_change(status, words):
    for the_key, the_value in status.items():
        status_word = the_key
        for word in words:
            if word[1] == status_word:
                rat_obj = Words_Rating.objects(wordID=word[0])[0]
                if the_value[1] == the_value[0]:
                    rat_obj.Ratings[0] = rat_obj.Ratings[0] - 1
                else:
                    rat_obj.Ratings[0] = rat_obj.Ratings[0] + 1
                rat_obj.save()