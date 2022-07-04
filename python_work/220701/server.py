from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      p::first-letter {
        font-size: 3em;
      }
      p::first-line {
        color: tomato;
      }
    </style>
  </head>
  <body>
    <h1>head</h1>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim recusandae
      nobis iure cumque, architecto voluptatem nulla minus exercitationem facere
      voluptas, deserunt animi! Accusantium consectetur fuga deleniti autem
      perspiciatis expedita aut.
    </p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim recusandae
      nobis iure cumque, architecto voluptatem nulla minus exercitationem facere
      voluptas, deserunt animi! Accusantium consectetur fuga deleniti autem
      perspiciatis expedita aut.
    </p>
  </body>
</html>
'''

app.run(host="192.168.0.12",port=5000)