import pylab
import urllib.request, json 

with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
    res = json.loads(url.read().decode())


days = []
results = []

for i in res:
    days.append(i["data"][5:10])
    v = 0.0
    v = (i["totale_casi"] / i["tamponi"]) * 100
    results.append(v)

pylab.figure("Risultati COVID-19 Italia")
pylab.plot(days, results, 'b-+', label="andamento")
pylab.legend()

pylab.show()
    