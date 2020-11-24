from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    ("I know you are, but what am I?", "iknowyouare.gif"),
    ("I don’t make monkeys. I just train them.", "monkeys.gif"),
    ("That’s my name. Don’t wear it out.", "iknowyouare.gif"),
    ("You don’t wanna get mixed up with a guy like me. I’m a loner, a rebel.", "rebel.gif"),
    ("What exactly leads you to believe the Soviets were involved?", "soviets.gif"),
    ("Go ahead, scream your head off! We’re miles from where anyone can hear you!", "pool.gif"),
    ("Is there something you could share with the rest of us, Amazing Larry?", "larry.gif"),
    ("Why don’t you take a picture? It’ll last longer.", "picture.gif"),
    ("Be sure and tell 'em Large Marge sent you.", "marge.gif"),
    ("Everyone I know has a big but. Let’s talk about your big but.", "simone.gif")
]
# https://consequenceofsound.net/2020/08/10-pee-wees-big-adventure-quotes-you-probably-say-all-the-time/


@app.route('/')
def index():
    quote, url = random.choice(images)
    return render_template('index.html', quote=quote, url=url)

@app.route('/<id>')
def quote(id):
    try:
        quote, url = images[int(id)]
    except:
        quote, url = random.choice(images)
    finally:
        return render_template('index.html', quote=quote, url=url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
