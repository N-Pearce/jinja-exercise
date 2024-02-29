from flask import Flask, request, render_template
from stories import stories

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('madlibs.html')

@app.route('/story')
def generate_story():
    print(request.args)
    story_num = int(request.args['story'])
    words = request.args
    text = stories[story_num].generate(words)
    return render_template('story.html', story=text)