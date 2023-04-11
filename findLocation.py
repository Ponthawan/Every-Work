import networkx as nx
import matplotlib.pyplot as plt
from geopy import distance as Distance

networkx = nx.Graph()
color_map = []

sub_districts = ['KMUTNB Prachinburi','Thetsaban Mueang Prachin Buri','Thetsaban Bannaprue','Thetsaban Khokmakok',
                 'SAO Rop Mueang','SAO Wat Bot','SAO Bang Decha','SAO Tha Ngam','SAO Dong Phra Ram','SAO Ban Phra',
                 'SAO Khok Mai Lai','SAO Mai Khet','SAO Dong Khilek','SAO Noen Hom' ,'SAO Non Hom',
                 '7-11 Noen Hom','7-11 Naresuan about','7-11 Phrom Yothi','7-11 Mai Khet','7-11 Mueng',
                 '7-11 Nha Mueng','7-11 Thetsaban Mueang','7-11 Sri Mahosot','7-11 Sri Maha Phot','7-11 Khok kwang',
                 '7-11 Klong rang','7-11 Nikom 304','7-11 Naphawee','7-11 The Master life Klong rang','7-11 Kabin',
                 '7-11 Transport Co Kabin','7-11 Industry Kabin','7-11 Nadee','7-11 Ban Sang','Robinson Prachinburi']

kmutnb_location = (14.0539, 101.9022) # latitude, longitude of KMUTNB Prachinburi campus
thetsaban_mueang_prachin_buri_location = (14.112074, 101.373244)
thetsaban_bannaprue_location = (14.121067, 101.378208)
thetsaban_khokmakok_location = (14.067620, 101.361590)
subdistrict_administrative_organization_rop_mueang = (14.111153, 101.383803)
subdistrict_administrative_organization_wat_bot = (14.114527, 101.366754)
subdistrict_administrative_organization_bang_decha = (14.126868, 101.364242)
subdistrict_administrative_organization_tha_ngam = (14.088626, 101.348141)
subdistrict_administrative_organization_dong_phra_ram = (14.062893, 101.379836)
subdistrict_administrative_organization_ban_phra = (14.050975, 101.377175)
subdistrict_administrative_organization_khok_mai_lai = (14.045970, 101.354717)
subdistrict_administrative_organization_mai_khet = (14.030997, 101.377074)
subdistrict_administrative_organization_Dong_khilek = (14.027205, 101.402829)
subdistrict_administrative_organization_noen_hom = (14.021902, 101.381739)
subdistrict_administrative_organization_non_hom = (14.016599, 101.365278)

pin_location = {
    'KMUTNB Prachinburi' : (14.0539, 101.9022),
    'Thetsaban Mueang Prachin Buri' : (14.112074, 101.373244),
    'Thetsaban Bannaprue' : (14.121067, 101.378208),
    'Thetsaban Khokmakok' : (14.067620, 101.361590),
    'SAO Rop Mueang' : (14.111153, 101.383803),
    'SAO Wat Bot' : (14.114527, 101.366754),
    'SAO Bang Decha' : (14.126868, 101.364242),
    'SAO Tha Ngam' : (14.088626, 101.348141),
    'SAO Dong Phra Ram' : (14.062893, 101.379836),
    'SAO Ban Phra' : (14.050975, 101.377175),
    'SAO Khok Mai Lai' : (14.045970, 101.354717),
    'SAO Mai Khet' : (14.030997, 101.377074),
    'SAO Dong Khilek' : (14.027205, 101.402829),
    'SAO Noen Hom' : (14.021902, 101.381739),
    'SAO Non Hom' : (14.016599, 101.365278),
    
}

all_locations = {
    
    
    'KMUTNB Prachinburi' : (14.0539, 101.9022),
    'Thetsaban Mueang Prachin Buri' : (14.112074, 101.373244),
    'Thetsaban Bannaprue' : (14.121067, 101.378208),
    'Thetsaban Khokmakok' : (14.067620, 101.361590),
    'SAO Rop Mueang' : (14.111153, 101.383803),
    'SAO Wat Bot' : (14.114527, 101.366754),
    'SAO Bang Decha' : (14.126868, 101.364242),
    'SAO Tha Ngam' : (14.088626, 101.348141),
    'SAO Dong Phra Ram' : (14.062893, 101.379836),
    'SAO Ban Phra' : (14.050975, 101.377175),
    'SAO Khok Mai Lai' : (14.045970, 101.354717),
    'SAO Mai Khet' : (14.030997, 101.377074),
    'SAO Dong Khilek' : (14.027205, 101.402829),
    'SAO Noen Hom' : (14.021902, 101.381739),
    'SAO Non Hom' : (14.016599, 101.365278),
    
    '7-11 Noen Hom': (14.154163847657905, 101.36638094043381),
    '7-11 Naresuan about' : (14.134395674842901, 101.37293565259067),
    '7-11 Phrom Yothi' : (14.134636225500829, 101.37748200086266),
    '7-11 Mai Khet' : (14.102372816484712, 101.37038668579187),    
    '7-11 Mueng' : (14.06488760978069, 101.37297715624717),
    '7-11 Nha Mueng' : (14.054200439669685, 101.39572119116544),
    '7-11 Thetsaban Mueang' : (14.05214044440797, 101.36822171734045),
    '7-11 Sri Mahosot' : (13.891741992841354, 101.40319459096399),
    '7-11 Sri Maha Phot' : (13.971516285738526, 101.51152514241873),
    '7-11 Khok kwang' : (13.951778599669533, 101.50801981971453),
    '7-11 Klong rang' : (13.899487965286866, 101.58319472962825),
    '7-11 Nikom 304' : (13.916350035110748, 101.57435509272486),
    '7-11 Naphawee' : (13.904626031330713, 101.55929197027669),
    '7-11 The Master life Klong rang' : (13.936433402564184, 101.5522161724525),
    '7-11 Kabin' : (13.991206704797426, 101.72042228517178),
    '7-11 Transport Co Kabin' : (13.984727537922021, 101.76197413779647),
    '7-11 Industry Kabin' : (14.07434226902785, 101.81620863985609),
    '7-11 Nadee' : (14.01650199628191, 101.7768880138743),
    '7-11 Ban Sang' : (13.99849344211129, 101.22304704662726),
    'Robinson Prachinburi' : (14.058846637854892, 101.39594802609889)
}

seven_eleven_all_locations = {
    '7-11 Noen Hom': (14.154163847657905, 101.36638094043381),
    '7-11 Naresuan about' : (14.134395674842901, 101.37293565259067),
    '7-11 Phrom Yothi' : (14.134636225500829, 101.37748200086266),
    '7-11 Mai Khet' : (14.102372816484712, 101.37038668579187),    
    '7-11 Mueng' : (14.06488760978069, 101.37297715624717),
    '7-11 Nha Mueng' : (14.054200439669685, 101.39572119116544),
    '7-11 Thetsaban Mueang' : (14.05214044440797, 101.36822171734045),
    '7-11 Sri Mahosot' : (13.891741992841354, 101.40319459096399),
    '7-11 Sri Maha Phot' : (13.971516285738526, 101.51152514241873),
    '7-11 Khok kwang' : (13.951778599669533, 101.50801981971453),
    '7-11 Klong rang' : (13.899487965286866, 101.58319472962825),
    '7-11 Nikom 304' : (13.916350035110748, 101.57435509272486),
    '7-11 Naphawee' : (13.904626031330713, 101.55929197027669),
    '7-11 The Master life Klong rang' : (13.936433402564184, 101.5522161724525),
    '7-11 Kabin' : (13.991206704797426, 101.72042228517178),
    '7-11 Transport Co Kabin' : (13.984727537922021, 101.76197413779647),
    '7-11 Industry Kabin' : (14.07434226902785, 101.81620863985609),
    '7-11 Nadee' : (14.01650199628191, 101.7768880138743),
    '7-11 Ban Sang' : (13.99849344211129, 101.22304704662726),
    'Robinson Prachinburi' : (14.058846637854892, 101.39594802609889)
    
}


G = nx.Graph()
G.add_nodes_from(sub_districts)
G.add_node('KMUTNB Prachinburi', pos=(9,10))
G.add_node('Thetsaban Mueang Prachin Buri', pos=(5,9))
G.add_node('Thetsaban Khokmakok', pos=(11,10))
G.add_node('SAO Rop Mueang', pos=(7,6))
G.add_node('SAO Wat Bot', pos=(6,6))
G.add_node('SAO Bang Decha', pos=(6,5))
G.add_node('SAO Tha Ngam', pos=(8,3))
G.add_node('SAO Dong Phra Ram', pos=(8,6))
G.add_node('SAO Ban Phra', pos=(8,8))
G.add_node('SAO Khok Mai Lai', pos=(3,9))
G.add_node('SAO Mai Khet', pos=(6,7))
G.add_node('SAO Dong Khilek', pos=(10,9))
G.add_node('SAO Noen Hom', pos=(8,10))
G.add_node('SAO Non Hom', pos=(12,9))
G.add_node('')

G.add_edges_from([
    
])


for sub_district in sub_districts:
    for store, location in all_locations.items():
        distance_km = Distance.distance(location, all_locations[sub_district]).km
        G.add_edge(sub_district, store, weight=distance_km)


start_sub_district = str(input("Where do want to start: "))
destination_seven_eleven = str(input("Where do you want to end: "))

shortest_path = nx.dijkstra_path(G, start_sub_district, destination_seven_eleven)


total_distance_km = 0
for i in range(len(shortest_path)-1):
    distance_km = G[shortest_path[i]][shortest_path[i+1]]['weight']
    total_distance_km += distance_km
    print(f"{shortest_path[i]} -> {shortest_path[i+1]}: {distance_km:.2f} km")
print(f"Total distance: {total_distance_km:.2f} km")


plt.title("Test")

nx.draw_networkx(G, with_labels=True)

plt.show()