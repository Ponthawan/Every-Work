import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([
    ('KMUTNB Prachinburi', '7-11 Noen Hom', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Naresuan', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('KMUTNB Prachinburi', '7-11 Mai Khet', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Mueng', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Nha Mueng', {'distance': 9.5})
    ,('KMUTNB Prachinburi', '7-11 Thetsaban Mueang', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Sri Mahosot', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('KMUTNB Prachinburi', '7-11 Khok kwang', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Nikom 304', {'distance': 9.5}),('KMUTNB Prachinburi', '7-11 Kabin', {'distance': 9.5})
    ,('KMUTNB Prachinburi','7-11 Nadee', {'distance': 9.5})
    
    ,('Mueang Prachin Buri', '7-11 Noen Hom', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Naresuan', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Mueang Prachin Buri', '7-11 Mai Khet', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Mueng', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Mueang Prachin Buri', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Sri Mahosot', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Mueang Prachin Buri', '7-11 Khok kwang', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Nikom 304', {'distance': 9.5}),('Mueang Prachin Buri', '7-11 Kabin', {'distance': 9.5})
    ,('Mueang Prachin Buri','7-11 Nadee', {'distance': 9.5})
    
    ,('Kabin Buri', '7-11 Noen Hom', {'distance': 9.5}),('Kabin Buri', '7-11 Naresuan', {'distance': 9.5}),('Kabin Buri', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Kabin Buri', '7-11 Mai Khet', {'distance': 9.5}),('Kabin Buri', '7-11 Mueng', {'distance': 9.5}),('Kabin Buri', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Kabin Buri', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Kabin Buri', '7-11 Sri Mahosot', {'distance': 9.5}),('Kabin Buri', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Kabin Buri', '7-11 Khok kwang', {'distance': 9.5}),('Kabin Buri', '7-11 Nikom 304', {'distance': 9.5}),('Kabin Buri', '7-11 Kabin', {'distance': 9.5})
    ,('Kabin Buri','7-11 Nadee', {'distance': 9.5})
    
    ,('Nadee', '7-11 Noen Hom', {'distance': 9.5}),('Nadee', '7-11 Naresuan', {'distance': 9.5}),('Nadee', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Nadee', '7-11 Mai Khet', {'distance': 9.5}),('Nadee', '7-11 Mueng', {'distance': 9.5}),('Nadee', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Nadee', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Nadee', '7-11 Sri Mahosot', {'distance': 9.5}),('Nadee', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Nadee', '7-11 Khok kwang', {'distance': 9.5}),('Nadee', '7-11 Nikom 304', {'distance': 9.5}),('Nadee', '7-11 Kabin', {'distance': 9.5})
    ,('Nadee','7-11 Nadee', {'distance': 9.5})
    
    ,('Ban Sang', '7-11 Noen Hom', {'distance': 9.5}),('Ban Sang', '7-11 Naresuan', {'distance': 9.5}),('Ban Sang', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Ban Sang', '7-11 Mai Khet', {'distance': 9.5}),('Ban Sang', '7-11 Mueng', {'distance': 9.5}),('Ban Sang', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Ban Sang', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Ban Sang', '7-11 Sri Mahosot', {'distance': 9.5}),('Ban Sang', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Ban Sang', '7-11 Khok kwang', {'distance': 9.5}),('Ban Sang', '7-11 Nikom 304', {'distance': 9.5}),('Ban Sang', '7-11 Kabin', {'distance': 9.5})
    ,('Ban Sang','7-11 Nadee', {'distance': 9.5})
    
    ,('Prachantakham', '7-11 Noen Hom', {'distance': 9.5}),('Prachantakham', '7-11 Naresuan', {'distance': 9.5}),('Prachantakham', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Prachantakham', '7-11 Mai Khet', {'distance': 9.5}),('Prachantakham', '7-11 Mueng', {'distance': 9.5}),('Prachantakham', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Prachantakham', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Prachantakham', '7-11 Sri Mahosot', {'distance': 9.5}),('Prachantakham', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Prachantakham', '7-11 Khok kwang', {'distance': 9.5}),('Prachantakham', '7-11 Nikom 304', {'distance': 9.5}),('Prachantakham', '7-11 Kabin', {'distance': 9.5})
    ,('Prachantakham','7-11 Nadee', {'distance': 9.5})
    
    ,('Si Maha Phot', '7-11 Noen Hom', {'distance': 9.5}),('Si Maha Phot', '7-11 Naresuan', {'distance': 9.5}),('Si Maha Phot', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Si Maha Phot', '7-11 Mai Khet', {'distance': 9.5}),('Si Maha Phot', '7-11 Mueng', {'distance': 9.5}),('Si Maha Phot', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Si Maha Phot', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Si Maha Phot', '7-11 Sri Mahosot', {'distance': 9.5}),('Si Maha Phot', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Si Maha Phot', '7-11 Khok kwang', {'distance': 9.5}),('Si Maha Phot', '7-11 Nikom 304', {'distance': 9.5}),('Si Maha Phot', '7-11 Kabin', {'distance': 9.5})
    ,('Si Maha Phot','7-11 Nadee', {'distance': 9.5})
    
    ,('Si Mahosot', '7-11 Noen Hom', {'distance': 9.5}),('Si Mahosot', '7-11 Naresuan', {'distance': 9.5}),('Si Mahosot', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Mai Khet', {'distance': 9.5}),('Si Mahosot', '7-11 Mueng', {'distance': 9.5}),('Si Mahosot', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Si Mahosot', '7-11 Sri Mahosot', {'Si Mahosot': 9.5}),('Si Mahosot', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Khok kwang', {'distance': 9.5}),('Si Mahosot', '7-11 Nikom 304', {'distance': 9.5}),('Si Mahosot', '7-11 Kabin', {'distance': 9.5})
    ,('Si Mahosot','7-11 Nadee', {'distance': 9.5})
    
    ,('7-11 Noen Hom', '7-11 Naresuan', {'distance': 9.5}),('7-11 Noen Hom', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('7-11 Noen Hom', '7-11 Mai Khet', {'distance': 9.5}),('7-11 Noen Hom', '7-11 Mueng', {'distance': 9.5}),('7-11 Noen Hom', '7-11 Nha Mueng', {'distance': 9.5})
    ,('7-11 Noen Hom', '7-11 Thetsaban Mueang', {'distance': 9.5}),('7-11 Noen Hom', '7-11 Sri Mahosot', {'7-11 Noen Hom': 9.5}),('Si Mahosot', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('7-11 Noen Hom', '7-11 Khok kwang', {'distance': 9.5}),('7-11 Noen Hom', '7-11 Nikom 304', {'distance': 9.5}),('7-11 Noen Hom', '7-11 Kabin', {'distance': 9.5})
    ,('7-11 Noen Hom','7-11 Nadee', {'distance': 9.5})
    
    ,('7-11 Naresuan', '7-11 Noen Hom', {'distance': 9.5}), ('7-11 Naresuan', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('7-11 Naresuan', '7-11 Mai Khet', {'distance': 9.5}),('7-11 Naresuan', '7-11 Mueng', {'distance': 9.5}),('7-11 Naresuan', '7-11 Nha Mueng', {'distance': 9.5})
    ,('7-11 Naresuan', '7-11 Thetsaban Mueang', {'distance': 9.5}),('7-11 Naresuan', '7-11 Sri Mahosot', {'7-11 Naresuan': 9.5}),('7-11 Naresuan', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('7-11 Naresuan', '7-11 Khok kwang', {'distance': 9.5}),('7-11 Naresuan', '7-11 Nikom 304', {'distance': 9.5}),('7-11 Naresuan', '7-11 Kabin', {'distance': 9.5})
    ,('7-11 Naresuan','7-11 Nadee', {'distance': 9.5})
    
    ,('Si Mahosot', '7-11 Noen Hom', {'distance': 9.5}),('Si Mahosot', '7-11 Naresuan', {'distance': 9.5}),('Si Mahosot', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Mai Khet', {'distance': 9.5}),('Si Mahosot', '7-11 Mueng', {'distance': 9.5}),('Si Mahosot', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Si Mahosot', '7-11 Sri Mahosot', {'Si Mahosot': 9.5}),('Si Mahosot', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Khok kwang', {'distance': 9.5}),('Si Mahosot', '7-11 Nikom 304', {'distance': 9.5}),('Si Mahosot', '7-11 Kabin', {'distance': 9.5})
    ,('Si Mahosot','7-11 Nadee', {'distance': 9.5})
    
    ,('Si Mahosot', '7-11 Noen Hom', {'distance': 9.5}),('Si Mahosot', '7-11 Naresuan', {'distance': 9.5}),('Si Mahosot', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Mai Khet', {'distance': 9.5}),('Si Mahosot', '7-11 Mueng', {'distance': 9.5}),('Si Mahosot', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Si Mahosot', '7-11 Sri Mahosot', {'Si Mahosot': 9.5}),('Si Mahosot', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Khok kwang', {'distance': 9.5}),('Si Mahosot', '7-11 Nikom 304', {'distance': 9.5}),('Si Mahosot', '7-11 Kabin', {'distance': 9.5})
    ,('Si Mahosot','7-11 Nadee', {'distance': 9.5})
    
    ,('Si Mahosot', '7-11 Noen Hom', {'distance': 9.5}),('Si Mahosot', '7-11 Naresuan', {'distance': 9.5}),('Si Mahosot', '7-11 Phrom Yothi', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Mai Khet', {'distance': 9.5}),('Si Mahosot', '7-11 Mueng', {'distance': 9.5}),('Si Mahosot', '7-11 Nha Mueng', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Thetsaban Mueang', {'distance': 9.5}),('Si Mahosot', '7-11 Sri Mahosot', {'Si Mahosot': 9.5}),('Si Mahosot', '7-11 Sri Maha Phot', {'distance': 9.5})
    ,('Si Mahosot', '7-11 Khok kwang', {'distance': 9.5}),('Si Mahosot', '7-11 Nikom 304', {'distance': 9.5}),('Si Mahosot', '7-11 Kabin', {'distance': 9.5})
    ,('Si Mahosot','7-11 Nadee', {'distance': 9.5})
])

pos = {'KMUTNB Prachinburi':(),'Kabin Buri':(),'Nadee':(),'Ban Sang':(),'Prachantakham':(),'Si Maha Phot':(),'Si Mahosot':()
       ,'7-11 Noen Hom':(),'7-11 Naresuan':(),'7-11 Phrom Yothi':(),'7-11 Mai Khet':(),'7-11 Mueng':(),'7-11 Nha Mueng':(),'7-11 Thetsaban Mueang':()
       ,'7-11 Sri Mahosot':(),'7-11 Sri Maha Phot':(),'7-11 Khok kwang':(),'7-11 Nikom 304':(),'7-11 Kabin':(),'7-11 Nadee':()}
