import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk

G = nx.Graph()

G.add_edges_from([
    ('KMUTNB Prachinburi', '7-11 Noen Hom', {'distance': 1.1}),
    ('7-11 Noen Hom', '7-11 Naresuan', {'distance': 2.4}),
    ('7-11 Naresuan', '7-11 Phrom Yothi', {'distance': 0.6}),
    ('7-11 Naresuan', '7-11 Mai Khet', {'distance': 3.7}),
    ('7-11 Phrom Yothi', '7-11 Mai Khet', {'distance': 4.1}),
    ('7-11 Phrom Yothi', '7-11 Prachantakham', {'distance': 21.2}),
    ('7-11 Phrom Yothi', '7-11 Mueng', {'distance': 7}),
    ('7-11 Mai Khet', '7-11 Mueng', {'distance': 5.8}),
    ('7-11 Mueng', '7-11 Nha Mueng', {'distance': 1.3}),
    ('7-11 Mueng', '7-11 Ban Sang', {'distance': 25.8}),
    ('7-11 Nha Mueng', '7-11 Ban Sang', {'distance': 25.3}),
    ('7-11 Nha Mueng', '7-11 Sri Mahosot', {'distance': 29.2}),
    ('7-11 Nha Mueng', '7-11 Sri Maha Phot', {'distance': 30.4}),
    ('7-11 Ban Sang', '7-11 Sri Mahosot', {'distance': 29.9}),
    ('Ban Sang', '7-11 Ban Sang', {'distance': 8}),
    ('7-11 Sri Mahosot', '7-11 Khok kwang', {'distance': 13.7}),
    ('Sri Mahosot', '7-11 Sri Mahosot', {'distance': 4.5}),
    ('Sri Maha Phot', '7-11 Sri Maha Phot', {'distance': 14}),
    ('Sri Maha Phot', '7-11 Khok kwang', {'distance': 2.5}),
    ('7-11 Sri Maha Phot', '7-11 Khok kwang', {'distance': 2}),
    ('7-11 Sri Maha Phot', '7-11 Nadee', {'distance': 49.2}),
    ('7-11 Khok kwang', '7-11 Nadee', {'distance': 55.3}),
    ('7-11 Khok kwang', '7-11 Nikom 304', {'distance': 8.8}),
    ('Prachantakham','7-11 Prachantakham', {'distance': 0.4}),
    ('7-11 Prachantakham','7-11 Nadee', {'distance': 32.7}),
    ('7-11 Prachantakham','7-11 Sri Maha Phot', {'distance': 12.3}),
    ('Nadee','7-11 Nadee', {'distance': 13.7}),
    ('7-11 Nadee','7-11 Nikom 304', {'distance': 46.7}),
    ('7-11 Nikom 304','7-11 Kabin', {'distance': 45.8}),
    ('Kabin Buri','7-11 Kabin', {'distance': 21.4}) 
    ])


pos = {'KMUTNB Prachinburi':(1,9),'Kabin Buri':(0,11.5),'Nadee':(10,7.6),'Ban Sang':(0.8,0.9),'Prachantakham':(6.5,9.2),'Sri Maha Phot':(7.4,3.5),'Sri Mahosot':(4,1.5)
       ,'7-11 Noen Hom':(2.1,8),'7-11 Naresuan':(2.65,7.35),'7-11 Phrom Yothi':(4.5,6.5),'7-11 Mai Khet':(2.3,5.6),'7-11 Mueng':(2.3,3.9),'7-11 Nha Mueng':(2.88,3.9),'7-11 Ban Sang':(2,1.3)
       ,'7-11 Sri Mahosot':(4,1.6),'7-11 Sri Maha Phot':(7,5.2),'7-11 Khok kwang':(5,1.3),'7-11 Nikom 304':(10,3.56),'7-11 Kabin':(9.2,1.7),'7-11 Nadee':(9.6,6.2), '7-11 Prachantakham':(7.4,7.9)}




def search_nodes():
    global shortest_path
    valid_nodes = ['KMUTNB Prachinburi', 'Kabin Buri', 'Nadee', 'Ban Sang', 'Prachantakham', 'Sri Maha Phot', 'Sri Mahosot',
                   '7-11 Noen Hom','7-11 Naresuan','7-11 Phrom Yothi','7-11 Mai Khet','7-11 Mueng','7-11 Nha Mueng','7-11 Thetsaban Mueang'
                    ,'7-11 Sri Mahosot','7-11 Sri Maha Phot','7-11 Khok kwang','7-11 Nikom 304','7-11 Kabin','7-11 Nadee']
    source = source_entry.get()
    while source not in valid_nodes:
        source = input(f"{source} is not a valid node. Please enter a valid source node: ")
    dest = dest_entry.get()
    while dest not in valid_nodes:
        dest = input(f"{dest} is not a valid node. Please enter a valid destination node: ")
    shortest_path = nx.shortest_path(G, source=source, target=dest, weight='distance')
    shortest_path_length = nx.shortest_path_length(G, source=source, target=dest, weight='distance')
    shortest_path_length = ("%.2f"%(shortest_path_length))
    path_label.config(text=f"Shortest path from {source} to {dest}: {shortest_path}\nShortest path length: {shortest_path_length} km")
    
    node_color_map = []
    for node in G.nodes():
        if node == shortest_path[0]:
            node_color_map.append('green')
        elif node == shortest_path[-1]:
            node_color_map.append('red')
        elif node in shortest_path:
            node_color_map.append('orange')
        else:
            node_color_map.append('gray')

    plt.figure(figsize=(12,8))
    nx.draw_networkx(G, pos, with_labels=True, node_color=node_color_map, node_size=1000)
    edge_labels = nx.get_edge_attributes(G, 'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edge_list = list(zip(shortest_path, shortest_path[1:]))
    plt.title("Distance of University", size=12)
    plt.show()


root = tk.Tk()
root.title("University Distance")

canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()

photo = tk.PhotoImage(file="University.png")
canvas.create_image(400, 300, image=photo)

frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM)

source_label = tk.Label(frame, text="Enter beginning from: ")
source_label.grid(row=0, column=0)

source_entry = tk.Entry(frame)
source_entry.grid(row=0, column=1)

dest_label = tk.Label(frame, text="Enter destination: ")
dest_label.grid(row=1, column=0)

dest_entry = tk.Entry(frame)
dest_entry.grid(row=1, column=1)

search_button = tk.Button(frame, text="Find shortest path", command=search_nodes)
search_button.grid(row=2, column=1)

path_label = tk.Label(frame, text="")
path_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
