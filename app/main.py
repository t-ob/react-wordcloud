import json
import os
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/words.json', methods=['GET', 'POST'])
def words_handler():

    with open('data/words.json', 'r') as file:
        comments = json.loads(file.read())

    # if request.method == 'POST':
    #     comments.append(request.form.to_dict())

    #     with open('data/comments.json', 'w') as file:
    #         file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",3000)))
