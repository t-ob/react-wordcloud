import json
import os
from flask import Flask, Response, request
import tweets

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/words.json', methods=['POST'])
def words_handler():

    form = request.form.to_dict()
    screen_name = form['screen_name']

    recent_tweets = tweets.get_tweets(screen_name)
    tokens = tweets.tokenize_tweets(recent_tweets)

    result = []
    for token, size in tweets.top_tokens(tokens):
        data = {
            'text': token.upper(),
            'size': size
        }
        result.append(data)

    return Response(json.dumps(result), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",3000)))
