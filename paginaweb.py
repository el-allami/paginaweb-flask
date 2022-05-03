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

@app.route('/pagina12', methods=['GET'])
def pagina12():
    return render_template("pagina12.html")

@app.route('/maglietta uomo nike sb', methods=['GET'])
def magliettauomonikesb():
    return render_template("maglietta uomo nike sb.html")

@app.route('/magliette uomo adida-skateboard', methods=['GET'])
def maglietteuomoadidaskateboard():
    return render_template("magliette uomo adida-skateboard.html")

@app.route('/magliette uomo anti-hero', methods=['GET'])
def maglietteuomoantihero():
    return render_template("magliette uomo anti-hero.html")
 
@app.route('/magliette uomo baker', methods=['GET'])
def maglietteuomobaker():
    return render_template("magliette uomo baker.html")

@app.route('/magliette uomo thrasher', methods=['GET'])
def maglietteuomothrasher():
    return render_template("magliette uomo thrasher.html")

@app.route('/pagina8', methods=['GET'])
def pagina8():
    return render_template("pagina8.html")

@app.route('/pagina9', methods=['GET'])
def pagina9():
    return render_template("pagina9.html")

@app.route('/pagina2', methods=['GET'])
def pagina2():
    return render_template("pagina2.html")

@app.route('/viti ace', methods=['GET'])
def vitiace():
    return render_template("viti ace.html")

@app.route('/viti bones', methods=['GET'])
def vitibones():
    return render_template("viti bones.html")

@app.route('/viti independent', methods=['GET'])
def vitiindependent():
    return render_template("viti independent.html")

@app.route('/viti mino-logo', methods=['GET'])
def vitiminologo():
    return render_template("viti mino-logo.html")

@app.route('/grip grizzly', methods=['GET'])
def gripgrizzly():
    return render_template("grip grizzly.html")

@app.route('/grip mob', methods=['GET'])
def gripmob():
    return render_template("grip mob.html")

@app.route('/grip toy machine', methods=['GET'])
def griptoymachine():
    return render_template("grip toy machine.html")
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)