import re
import helpers as help

def get_japanese(data_str):
    pattern = r"Japanese\(word='([^']+)', reading='([^']+)'"
    match = re.search(pattern, data_str)
    if match:
        return {
            "word" : match.group(1),
            "reading" : match.group(2)
        }
    else:
        return None
    
def is_common(data_str):
    pattern = r"is_common=(\w+)"
    match = re.search(pattern, data_str)
    if match:
        value = match.group(1)
        if value.lower() == "true":
            return True
        else:
            return False
    else:
        return False
    
def get_wanikani(data_str):
    pattern = r"tags=\['wanikani(\d+)'"
    match = re.search(pattern, data_str)
    if match:
        return match.group(1)
    
def get_jlpt(data_str):
    pattern = r"jlpt=\['jlpt-n(\d+)'"
    match = re.search(pattern, data_str)
    if match:
        return match.group(1)
    
def get_english_def(data_str):
    pattern = r"Sense\(english_definitions=\[(.*?)\], parts_of_speech=\[(.*?)\]"
    matches = re.findall(pattern, data_str)
    return matches

def get_sentences(res):
    pattern = r"SentenceConfig\(japanese='(.*?)', en_translation='(.*?)'\)"
    matches = re.findall(pattern, str(res))
    sentence_configs = []
    for match in matches:
        japanese, en_translation = match
        sentence_configs.append({'japanese': japanese, 'en_translation': en_translation})
    return sentence_configs