def create_pairs_dict(phrase, pos):
    phrase = phrase.strip("'")
    pos = pos.strip("'")
    
    phrase_words = phrase.split(", ")
    pos_words = pos.split(", ")
    
    last_word_phrase = phrase_words[-1]
    last_word_pos = pos_words[-1] 
    
    remaining_phrase = ', '.join(phrase_words[:-1])
    remaining_pos = ', '.join(pos_words[:-1])

    remaining_phrase = remaining_phrase.replace("'", "").replace('"', "")
    last_word_phrase = last_word_phrase.replace("'", "").replace('"', "")
    remaining_pos = remaining_pos.replace("'", "").replace('"', "")
    last_word_pos = last_word_pos.replace("'", "").replace('"', "")
    
    pairs_dict = {
        'phrase': (remaining_phrase, last_word_phrase),
        'pos': (last_word_pos)
    }
    
    return pairs_dict