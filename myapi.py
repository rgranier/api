from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# Home
@app.route('/', methods=['GET'])
def home():
    html = '''
    <!doctype html>

    <html lang="en">
    <head>
      <meta charset="utf-8">

      <title>API Test</title>
      <meta name="description" content="API Test">
      <meta name="author" content="Randall">

      <style>
      body {background-color: powderblue;}
      h1   {color: blue;}
      p    {color: red;}
      </style>

    </head>

    <body>

    <h1>API Test</h1>
    <p>We have added internal styles and will be attempting a full build.</p>
    </body>
    </html>
    '''

    mydata = 'Some test log info.  Is this written to the log?'
    LOG.info(f"My output: {mydata}")
    return html

    @app.route('/foo/', methods=['POST'])
    def my_post():
        html = '''foo
        '''

        mydata = 'This is a POST.'
        LOG.info(f"My output: {mydata}")
        return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
