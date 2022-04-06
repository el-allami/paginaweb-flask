from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def HomeP():
    return render_template("pagina1.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)