from flask import Flask, render_template, request
from jisho_api.word import Word
import controller as c
import helpers  as h
from jisho_api.sentence import Sentence

app = Flask(__name__)

# jisho

@app.route('/jisho')
def jisho():
    data = {
        'title': "jisho",
        'curr_search': '',
    }
    return render_template('jisho/home.html', data=data)

@app.route('/jisho/search', methods=['GET', 'POST'])
def search_keyword():
    if request.method == 'POST' or request.method == 'GET':
        keyword = request.args.get('keyword')
        data = {
            'title': "jisho | search",
            'curr_search': keyword,
            'res': [],
            'sentence': None,
            'error': False
        }
        try:
            r = Word.request(keyword)
            s = Sentence.request(keyword)
            for response_item in r.data:
                response_str = str(response_item)
                item_data = {
                    "japanese": c.get_japanese(response_str),
                    "is_common": c.is_common(response_str),
                    "wanikani": c.get_wanikani(response_str),
                    "jlpt": c.get_jlpt(response_str),
                    "english_def": [(h.clean_string(item[0]), item[1]) for item in c.get_english_def(response_str)]
                }
                data['res'].append(item_data)
            data['sentence'] = c.get_sentences(s)

        except Exception as e:
            data['error'] = True
            print(e)

        print(data['res'])
        return render_template('jisho/home.html', data=data)

@app.route('/jisho/reference')
def reference():
    data = {
        'title': "jisho | reference"
    }
    return render_template('jisho/reference.html', data=data)


# home
@app.route('/')
def home():
    data = {
        'title': "home"
    }
    return render_template('portfolio/home.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
