import folium, re
from folium.plugins import MiniMap, FloatImage, MeasureControl, MousePosition, TagFilterButton
from influxClient import InfluxClient

#   QUERY

IC = InfluxClient("Bo6LdE_XVqMZrC6hAu_OUZwhRYxwqFiea01RJx9sdPdtcxbfE0mzPi32spI2JFWkQwpQcUl5Y15Rg2NCX1WrwA==","Boias Livres","bucket-boias")
query1 = 'from(bucket: "bucket-boias")\
  |> range(start: 1633124983)\
  |> filter(fn: (r) => r["_measurement"] == "boiasLivres")\
  |> filter(fn: (r) => r["boia_id"] == "2")\
  |> filter(fn: (r) => r["_field"] == "latitude" or r["_field"] == "longitude")\
  |> group(columns: ["_time", "tag"])\
  |> yield(name: "mean")'
c = IC.query_data(query1)
c = [i[0] for i in c]
final = [*zip(c[::2], c[1::2])]

#   CONFIG MAPA
caminhoArquivoLaranja = 'python\laranja.txt'
rosaDosVentos = ("https://raw.githubusercontent.com/ocefpaf/secoora_assets_map/a250729bbcf2ddd12f46912d36c33f7539131bec/secoora_icons/rose.png")
formatter = "function(num) {return L.Util.formatNum(num, 3) + ' &deg; ';};" #formatador pros pontos da posição do mouse
florianopolis_coords = [-27.5973002, -48.5496098] # Coordenadas aproximadas do centro de Florianópolis
laranja = 'orange'; verde = 'green'; preto = 'black'; vermelho = 'red'; roxo = 'purple'
bv = 'Boia Vermelha'; bvd = 'Boia Verde'; bl = 'Boia Laranja'; bp = 'Boia Preta'; br = 'Boia Roxa'
circle = 'circle'; flag = 'glyphicon-flag'
# -------------
mapa = folium.Map(location=florianopolis_coords, zoom_start=12)
MiniMap(toggle_display=True).add_to(mapa)
FloatImage(rosaDosVentos, bottom=70, left=4).add_to(mapa)
mapa.add_child(MeasureControl())
MousePosition(position="bottomleft", separator=" | ", lat_formatter=formatter, lng_formatter=formatter, prefix="Coordinates:").add_to(mapa) #posicao mouse
folium.plugins.LocateControl(auto_start=False).add_to(mapa) #local user

#   Criar grupos de pontos para as boias
grupoVermelho = folium.FeatureGroup("Boia Vermelha").add_to(mapa)
grupoVerde = folium.FeatureGroup("Boia Verde").add_to(mapa)
grupoPreto = folium.FeatureGroup("Boia Preta").add_to(mapa)
grupoLaranja = folium.FeatureGroup("Boia Laranja").add_to(mapa)

#       FUNÇÕES
def trilhaDaBoia(coordenadas,  corDaBoia, grupoBoia):
    folium.PolyLine(coordenadas, dash_array="5,10", color=corDaBoia, smooth_factor=30).add_to(mapa)
    for coordenada in coordenadas[1:]:
        marcadorDeBoia(coordenada, corDaBoia, circle, grupoBoia)

def marcadorDeBoia(coordenadaDaBoia, corDaBoia, icone, grupoBoia):
    folium.Marker(coordenadaDaBoia, popup=folium.Popup(str(coordenadaDaBoia), max_width=100), icon=folium.Icon(color=corDaBoia, icon=icone, popup=coordenadaDaBoia)).add_to(grupoBoia)
    print(str(coordenadaDaBoia))


def criaListaDeCoordenadas(caminhoArquivo):
    coordenadasLidas = []
    with open(caminhoArquivo) as arquivo:
        temp = []
        for lat_long_str in arquivo:
            lat_long = [float(x) for x in re.split(r',\s*', lat_long_str)]
            if tuple(lat_long) not in coordenadasLidas:
                coordenadasLidas.append(tuple(lat_long))
    return coordenadasLidas

def plotarBoia(listaCoordenadasBoia, corDaBoia, grupoBoia):
    marcadorDeBoia(listaCoordenadasBoia[0],corDaBoia, flag, grupoBoia)
    trilhaDaBoia(listaCoordenadasBoia, corDaBoia, grupoBoia)

#   PLOTANDO
plotarBoia(final, preto, grupoPreto)

folium.FitOverlays(fly=True).add_to(mapa) #centrar nos marcadores 
folium.LayerControl().add_to(mapa)
mapa.save('mapaQuery.html')