from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def HomeP():
    return render_template("pagina1.html")

@app.route('/HOME', methods=['GET'])
def Home():
    return render_template("pagina1.html")

@app.route('/come nasce lo skate1', methods=['GET'])
def comenasceloskate1():
    return render_template("come nasce lo skate1.html")

@app.route('/come scegliere un setup', methods=['GET'])
def comescegliereunsetup():
    return render_template("come scegliere un setup.html")

@app.route('/come scegliere una tavola1', methods=['GET'])
def comescegliereunatavola1():
    return render_template("come scegliere una tavola1.html")

@app.route('/come scegliere dei truck', methods=['GET'])
def comesceglieredeitruck():
    return render_template("come scegliere dei truck.html")

@app.route('/come scegliere delle ruote', methods=['GET'])
def comesceglieredelleruote():
    return render_template("come scegliere delle ruote.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)