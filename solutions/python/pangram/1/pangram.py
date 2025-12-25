def is_pangram(sentance):

    abc = set("abcdefghijklmnopqrstuvwxyz")
    sentance_set = {i for i in sentance.lower() if i.isalpha()}
    if abc == sentance_set:
        return True
    else:
        return False


is_pangram("the quick brown fox jumps over the lazy dog")
