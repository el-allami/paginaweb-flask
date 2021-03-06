from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
app = Flask(__name__)

import pandas as pd
import geopandas as gpd
import folium


caschi1 = pd.read_csv('static/file/caschi.csv')
ceraskate1= pd.read_csv('static/file/ceraskate.csv')
crashpants1= pd.read_csv('static/file/crashpants.csv')
cuscinettibones1= pd.read_csv('static/file/cuscinettibones.csv')
cuscinettibronsor1= pd.read_csv('static/file/cuscinettibronsor.csv')
ginocchiere1=pd.read_csv('static/file/ginocchiere.csv')
gomitiere1=pd.read_csv('static/file/gomitiere.csv')
gombones1=pd.read_csv('static/file/gomminibones.csv')
gomindipendent1=pd.read_csv('static/file/gomminiindependent.csv')
tool1=pd.read_csv('static/file/tool.csv')
santa1=pd.read_csv('static/file/tavolasantacruz.csv')
girl1=pd.read_csv('static/file/tavolegirl.csv')
ace1=pd.read_csv('static/file/truckace.csv')
indi1=pd.read_csv('static/file/truckindipendent.csv')
trkven1=pd.read_csv('static/file/truckventure.csv')
ruotbon1=pd.read_csv('static/file/ruotebones.csv')
ruotspit1=pd.read_csv('static/file/ruotespitfire.csv')
polsiere1=pd.read_csv('static/file/polsiere.csv')


skateparkdf= pd.read_csv("/workspace/paginaweb-flask/static/file/skatepark.csv")
skatepark= gpd.GeoDataFrame(skateparkdf,geometry=gpd.points_from_xy(skateparkdf.LON,skateparkdf.LAT))
skatepark=skatepark.set_crs(4326)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        psw = request.form.get("pwd")
        email = request.form.get("email")
        dati = pd.read_csv("/workspace/paginaweb-flask/static/file/dati.csv")
        for _, r in dati.iterrows():
            print(r['email'])
            if email == r['email'] and psw == r['psw']:
                return render_template("pagina1.html")
        return render_template("errore.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form.get("name")
        surname = request.form.get("surname")
        psw = request.form.get("pwd")
        cpsw = request.form.get("cpwd")
        email = request.form.get("email")

        utente = [{"name": name, "surname": surname,
                   "psw": psw, "email": email}]

        # controllo password
        if cpsw != psw:
            return 'le password non corrispondono'
        else:
            dati = pd.read_csv("/workspace/paginaweb-flask/static/file/dati.csv")
            dati = dati.append(utente, ignore_index=True)
            dati.to_csv('/workspace/paginaweb-flask/static/file/dati.csv')
            return render_template('login.html', name=name, surname=surname, psw=psw, utente=utente, email=email)

@app.route('/HOME', methods=['GET'])
def Home():
    return render_template("pagina1.html")

@app.route('/pagina2', methods=['GET'])
def pagina2():
    return render_template("pagina2.html")

@app.route('/pagina3', methods=['GET'])
def pagina3():
    return render_template("pagina3.html")

@app.route('/pagina4', methods=['GET'])
def pagina4():
    return render_template("pagina4.html")

@app.route('/pagina5', methods=['GET'])
def pagina5():
    return render_template("pagina5.html")

@app.route('/pagina6', methods=['GET'])
def pagina6():
    return render_template("pagina6.html")

@app.route('/pagina7', methods=['GET'])
def pagina7():
    return render_template("pagina7.html")

@app.route('/pagina8', methods=['GET'])
def pagina8():
    return render_template("pagina8.html")

@app.route('/pagina9', methods=['GET'])
def pagina9():
    return render_template("pagina9.html")

@app.route('/pagina10', methods=['GET'])
def pagina10():
    return render_template("pagina10.html")

@app.route('/pagina11', methods=['GET'])
def pagina11():
    return render_template("pagina11.html")

@app.route('/pagina12', methods=['GET'])
def pagina12():
    return render_template("pagina12.html")

@app.route('/skatepark', methods=['GET'])
def skatepark():
    skateparkdf= pd.read_csv("/workspace/paginaweb-flask/static/file/skatepark.csv")
    skatepark= gpd.GeoDataFrame(skateparkdf,geometry=gpd.points_from_xy(skateparkdf.LON,skateparkdf.LAT))
    skatepark=skatepark.set_crs(4326)

    map = folium.Map(location=[45.490943,9.2417171],zoom_start=12,tiles="openstreetmap")
    for i in range(0,len(skatepark)):
        folium.Marker(
        location=[skatepark.iloc[i]['LAT'], skatepark.iloc[i]['LON']],
        popup=skatepark.iloc[i][['SKATEPARK', 'LAT','LON']],
        ).add_to(map)
    return render_template("mappa.html", map = map._repr_html_())

@app.route('/skateshop', methods=['GET'])
def skateshop():
    skateshopdf= pd.read_csv("/workspace/paginaweb-flask/static/file/skateshop.csv")
    skateshop= gpd.GeoDataFrame(skateshopdf,geometry=gpd.points_from_xy(skateshopdf.LON,skateshopdf.LAT))
    skateshop=skateshop.set_crs(4326)

    map = folium.Map(location=[45.490943,9.2417171],zoom_start=12,tiles="openstreetmap")
    for i in range(0,len(skateshop)):
        folium.Marker(
        location=[skateshop.iloc[i]['LAT'], skateshop.iloc[i]['LON']],
        popup=skateshop.iloc[i][['SKATESHOP', 'LAT','LON']],
        ).add_to(map)
    return render_template("mappa.html", map = map._repr_html_())

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

@app.route('/viti ace', methods=['GET'])
def vitiace():
    return render_template("viti ace.html")

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

@app.route('/tool', methods=['GET'])
def tool():
    return render_template("tool.html",risultato=tool1['foto'].to_list())

@app.route("/tool_ris/<foto>", methods=["GET"])
def dettaglio_tool(foto):
    tol=tool1[tool1['foto']==foto]
    return render_template("tool_ris.html",modello=list(tol.modello),prezzo=list(tol.prezzo),foto=list(tol.foto))

@app.route('/cera skate', methods=['GET'])
def ceraskate():
    return render_template("cera skate.html",risultato=ceraskate1['foto'].to_list())

@app.route("/ceraskate_ris/<foto>", methods=["GET"])
def dettaglio_cera(foto):
    cera=ceraskate1[ceraskate1['foto']==foto]
    return render_template("ceraskate_ris.html",modello=list(cera.modello),prezzo=list(cera.prezzo),foto=list(cera.foto))

@app.route('/caschi', methods=['GET'])
def caschi12():
    return render_template("caschi.html",risultato=caschi1['foto'].to_list())

@app.route("/caschi_ris/<foto>", methods=["GET"])
def dettaglio_caschi(foto):
    cas=caschi1[caschi1['foto']==foto]
    return render_template("caschi_ris.html",modello=list(cas.modello),prezzo=list(cas.prezzo),foto=list(cas.foto))

@app.route('/ginocchiere', methods=['GET'])
def ginocchiere():
   return render_template("ginocchiere.html",risultato=ginocchiere1['foto'].to_list())

@app.route("/ginocchiere_ris/<foto>", methods=["GET"])
def dettaglio_ginocchiere(foto):
    ginocchiere2=ginocchiere1[ginocchiere1['foto']==foto]
    return render_template("ginocchiere_ris.html",modello=list(ginocchiere2.modello),prezzo=list(ginocchiere2.prezzo),foto=list(ginocchiere2.foto))

@app.route('/crashpants', methods=['GET'])
def crashpants():
    return render_template("crashpants.html",risultato=crashpants1['foto'].to_list())

@app.route("/crashpants_ris/<foto>", methods=["GET"])
def dettaglio_crashpants(foto):
    crash=crashpants1[crashpants1['foto']==foto]
    return render_template("crashpants_ris.html",modello=list(crash.modello),prezzo=list(crash.prezzo),foto=list(crash.foto))

@app.route('/polsiere', methods=['GET'])
def polsiere():
    return render_template("polsiere.html",risultato=polsiere1['foto'].to_list())

@app.route("/polsiere_ris/<foto>", methods=["GET"])
def dettaglio_polsiere(foto):
    pols1=polsiere1[polsiere1['foto']==foto]
    return render_template("polsiere_ris.html",modello=list(pols1.modello),prezzo=list(pols1.prezzo),foto=list(pols1.foto))
    
@app.route('/gomitiere', methods=['GET'])
def gomitiere():
     return render_template("gomitiere.html",risultato=gomitiere1['foto'].to_list())

@app.route("/gomitiere_ris/<foto>", methods=["GET"])
def dettaglio_gomitiere(foto):
    gomit=gomitiere1[gomitiere1['foto']==foto]
    return render_template("gomitiere_ris.html",modello=list(gomit.modello),prezzo=list(gomit.prezzo),foto=list(gomit.foto))

@app.route('/setup protezioni', methods=['GET'])
def setupprotezioni():
    return render_template("setup protezioni.html")

@app.route('/cuscinetti  bones', methods=['GET'])
def cuscinettibones():
    return render_template("cuscinetti  bones.html",risultato=cuscinettibones1['foto'].to_list())

@app.route("/cuscinettibones_ris/<foto>", methods=["GET"])
def dettaglio_bones(foto):
    bones1=cuscinettibones1[cuscinettibones1['foto']==foto]
    return render_template("cuscinettibones_ris.html",modello=list(bones1.modello),prezzo=list(bones1.prezzo),foto=list(bones1.foto))

@app.route('/cuscinetti bronsor', methods=['GET'])
def cuscinettibronsor():
    return render_template("cuscinetti bronsor.html",risultato=cuscinettibronsor1['foto'].to_list())

@app.route("/cuscinettibronsor_ris/<foto>", methods=["GET"])
def dettaglio_bronsor(foto):
    bronsor1=cuscinettibronsor1[cuscinettibronsor1['foto']==foto]
    return render_template("cuscinettibronsor_ris.html",modello=list(bronsor1.modello),prezzo=list(bronsor1.prezzo),foto=list(bronsor1.foto))


@app.route('/gommini bones', methods=['GET'])
def gomminibones():
    return render_template("gommini bones.html",risultato=gombones1['foto'].to_list())

@app.route("/gomminibones_ris/<foto>", methods=["GET"])
def dettaglio_gomminibones(foto):
    gomi=gombones1[gombones1['foto']==foto]
    return render_template("gomminibones_ris.html",modello=list(gomi.modello),prezzo=list(gomi.prezzo),foto=list(gomi.foto))


@app.route('/gommini independent', methods=['GET'])
def gomminiindependent():
    return render_template("gommini independent.html",risultato=gomindipendent1['foto'].to_list())

@app.route("/gomminiindependent_ris/<foto>", methods=["GET"])
def dettaglio_gomminiindependent(foto):
    gomind=gomindipendent1[gomindipendent1['foto']==foto]
    return render_template("gomminiindependent_ris.html",modello=list(gomind.modello),prezzo=list(gomind.prezzo),foto=list(gomind.foto))

@app.route('/ruote bones', methods=['GET'])
def ruotebones():
    return render_template("ruote bones.html",risultato=ruotbon1['foto'].to_list())

@app.route("/ruotebones_ris/<foto>", methods=["GET"])
def dettaglio_ruotebones(foto):
    bonru=ruotbon1[ruotbon1['foto']==foto]
    return render_template("ruotebones_ris.html",modello=list(bonru.modello),prezzo=list(bonru.prezzo),foto=list(bonru.foto))

@app.route('/ruote santacuz', methods=['GET'])
def ruotesantacuz():
    return render_template("ruote santacuz.html")

@app.route('/ruote spitfire', methods=['GET'])
def ruotespitfire():
    return render_template("ruote spitfire.html",risultato=ruotspit1['foto'].to_list())

@app.route("/ruotespitfire_ris/<foto>", methods=["GET"])
def dettaglio_ruotespitfire(foto):
    spitru=ruotspit1[ruotspit1['foto']==foto]
    return render_template("ruotespitfire_ris.html",modello=list(spitru.modello),prezzo=list(spitru.prezzo),foto=list(spitru.foto))

@app.route('/tavola santacruz', methods=['GET'])
def tavolasantacruz():
    return render_template("tavola santacruz.html",risultato=santa1['foto'].to_list())

@app.route("/tavolasantacruz_ris/<foto>", methods=["GET"])
def dettaglio_tavolasantacruz(foto):
    san=santa1[santa1['foto']==foto]
    return render_template("tavolasantacruz_ris.html",modello=list(san.modello),prezzo=list(san.prezzo),foto=list(san.foto))

@app.route('/tavole girl', methods=['GET'])
def tavolegirl():
    return render_template("tavole girl.html",risultato=girl1['foto'].to_list())

@app.route("/tavolegirl_ris/<foto>", methods=["GET"])
def dettaglio_tavolegirl(foto):
    tavgirl=girl1[girl1['foto']==foto]
    return render_template("tavolegirl_ris.html",modello=list(tavgirl.modello),prezzo=list(tavgirl.prezzo),foto=list(tavgirl.foto))

@app.route('/truck ace', methods=['GET'])
def truckace():
    return render_template("truck ace.html",risultato=ace1['foto'].to_list())

@app.route("/truckace_ris/<foto>", methods=["GET"])
def dettaglio_truckace(foto):
    trukace=ace1[ace1['foto']==foto]
    return render_template("truckace_ris.html",modello=list(trukace.modello),prezzo=list(trukace.prezzo),foto=list(trukace.foto))

@app.route('/truck indipendent', methods=['GET'])
def trukindipendent():
    return render_template("truck indipendent.html",risultato=indi1['foto'].to_list())

@app.route("/truckindipendent_ris/<foto>", methods=["GET"])
def dettaglio_trukindipendent(foto):
    trukindi=indi1[indi1['foto']==foto]
    return render_template("truckindipendent_ris.html",modello=list(trukindi.modello),prezzo=list(trukindi.prezzo),foto=list(trukindi.foto))

@app.route('/truck venture', methods=['GET'])
def truckventure():
    return render_template("truck venture.html",risultato=trkven1['foto'].to_list())

@app.route("/truckventure_ris/<foto>", methods=["GET"])
def dettaglio_truckventure(foto):
    vent1=trkven1[trkven1['foto']==foto]
    return render_template("truckventure_ris.html",modello=list(vent1.modello),prezzo=list(vent1.prezzo),foto=list(vent1.foto))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3247, debug=True)