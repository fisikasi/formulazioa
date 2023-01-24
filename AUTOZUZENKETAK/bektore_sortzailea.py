import streamlit as st
import pandas as pd
import numpy as np
import random
import math
from pathlib import Path

#------------------------------------HIDRUROAK----------------------------------------------------
                    #------------FORMULAK IDAZTEKO----------------
def df_hidruroak_formulak():
    print(Path().cwd())
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Hidruro Metalikoa","Hidruro Ez metalikoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_hidruro_form(n):
    df=df_hidruroak_formulak()
    vector = np.array([random.randint(0, len(df)-1) for i in range(n)])
    #print(df.shape)
    #print("hidruroak:",vector)
    emaitza = df.iloc[vector, 0:5]
    return emaitza
                        #------------IZENAK IDAZTEKO---------------
def df_hidruroak_izena():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK1.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Hidruro Metalikoa","Hidruro Ez metalikoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_hidruro_izena(n):
    df=df_hidruroak_izena()
    vector = np.array([random.randint(0, len(df)) for i in range(n)])
    #print(vector)
    emaitza = df.iloc[vector, 0:6]
    return emaitza

#------------------------------------OXIDOAK----------------------------------------------------
                    # ------------FORMULAK IDAZTEKO----------------

def df_oxidoak_formulak():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Oxido Metalikoa", "Anhidridoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_oxido_form(n):
    df=df_oxidoak_formulak()
    vector = np.array([random.randint(0, len(df)-1) for i in range(n)])
    #print(df.shape)
    #print("oxidoak:", vector)
    emaitza = df.iloc[vector, 0:6]
    return emaitza
                # ------------IZENAK IDAZTEKO---------------
def df_oxidoak_izena():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK1.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Oxido Metalikoa", "Anhidridoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_oxido_izena(n):
    df=df_oxidoak_izena()
    vector = np.array([random.randint(0, len(df)) for i in range(n)])
    emaitza = df.iloc[vector, 0:6]
    return emaitza


#------------------------------------GATZ BITARRAK----------------------------------------------------
                    # ------------FORMULAK IDAZTEKO----------------

def df_gatzbitarrak_formulak():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Gatz Bitarra (M+EM)","Gatz bitarra (EM+EM)"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_gatzbitarra_form(n):
    df=df_gatzbitarrak_formulak()
    vector = np.array([random.randint(0, len(df)-1) for i in range(n)])
    #print(df.shape)
    #print("gatz2:", vector)
    emaitza = df.iloc[vector, 0:6]
    return emaitza
                    # ------------IZENAK IDAZTEKO---------------
def df_gatzbitarrak_izena():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK1.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Gatz Bitarra (M+EM)","Gatz bitarra (EM+EM)"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_gatzbitarra_izena(n):
    df=df_gatzbitarrak_izena()
    vector = np.array([random.randint(0, len(df)) for i in range(n)])
    emaitza = df.iloc[vector, 0:6]
    return emaitza
#------------------------------------HIDROXIDOAK----------------------------------------------------
 # ------------FORMULAK IDAZTEKO----------------
def df_hidroxidoak_formulak():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Hidroxidoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_hidroxido_form(n):
    df=df_hidroxidoak_formulak()
    vector = np.array([random.randint(0, len(df)-1) for i in range(n)])
    #print(df.shape)
    #print("hidroxido:", vector)
    emaitza = df.iloc[vector, 0:6]
    return emaitza
 # ------------IZENAK IDAZTEKO---------------
def df_hidroxidoak_izena():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK1.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Hidroxidoa"])]
    emaitza = df_hidruroak  # .to_numpy()
    return emaitza


def bekt_hidroxido_izena(n):
    df = df_hidroxidoak_izena()
    vector = np.array([random.randint(0, len(df)) for i in range(n)])
    emaitza = df.iloc[vector, 0:6]
    return emaitza
#------------------------------------OXOAZIDOAK----------------------------------------------------
 # ------------FORMULAK IDAZTEKO----------------
def df_oxoazidoak_formulak():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Oxoazidoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza


def bekt_oxoazido_form(n):
    df=df_oxoazidoak_formulak()
    vector = np.array([random.randint(0, len(df)-1) for i in range(n)])
    #print(df.shape)
    #print("oxoazido:", vector)
    emaitza = df.iloc[vector, 0:6]
    return emaitza
 # ------------IZENAK IDAZTEKO---------------
def df_oxoazidoak_izena():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK1.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Oxoazidoa"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza


def bekt_oxoazido_izena(n):
    df=df_oxoazidoak_izena()
    vector = np.array([random.randint(0, len(df)) for i in range(n)])
    emaitza = df.iloc[vector, 0:6]
    return emaitza
#------------------------------------GATZ HIRUTARRAK----------------------------------------------------
 # ------------FORMULAK IDAZTEKO----------------
def df_gatzhirutarrak_izena():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK1.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Gatz hirutarrak"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_gatzhirutarra_izena(n):
    df=df_gatzhirutarrak_izena()
    vector = np.array([random.randint(0, len(df)) for i in range(n)])
    emaitza = df.iloc[vector, 0:6]
    return emaitza
 # ------------IZENAK IDAZTEKO---------------
def df_gatzhirutarrak_formulak():
    df = pd.read_excel(r'./AUTOZUZENKETAK/DATUAK.xlsx')
    df_hidruroak = df[df[df.columns[4]].isin(["Gatz hirutarrak"])]
    emaitza=df_hidruroak#.to_numpy()
    return emaitza

def bekt_gatzhirutarra_form(n):
    df=df_gatzhirutarrak_formulak()
    vector = np.array([random.randint(0, len(df)-1) for i in range(n)])
    #print(df.shape)
    #print("gatz3:", vector)
    emaitza = df.iloc[vector, 0:6]
    return emaitza



def generate_vector(n, m):
    vector = []
    suma=0
    for i in range(m-1):
        a=random.randint(1,2)
        if a==1:
            suma=suma+math.floor(n/m)
            vector.append(math.floor(n/m))
        else:
            suma = suma + math.ceil(n / m)
            vector.append(math.ceil(n / m))
    if (n-suma)<0:
            vector.append(0)
    else:
        vector.append(n-suma)
    random.shuffle(vector)
    return vector

#1.mailako bektorea sortzeko (Hidruroak)
def formula_sortu_1(n):
    df1=bekt_hidruro_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_hidruro_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(1, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(1, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#2.mailako bektorea sortzeko (Oxidoak)
def formula_sortu_2(n):
    df1=bekt_oxido_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_oxido_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(1, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(1, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#3.mailako bektorea sortzeko (Hirdruroak + Oxidoak)
def formula_sortu_3(n):
    ordena=generate_vector(n,2)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko


#4.mailako bektorea sortzeko (GatzBitarrak)
def formula_sortu_4(n):
    df1=bekt_gatzbitarra_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_gatzbitarra_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(1, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(1, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#5.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak)
def formula_sortu_5(n):
    ordena=generate_vector(n,3)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#6.mailako bektorea sortzeko (Hidroxidoak)
def formula_sortu_6(n):
    df1=bekt_hidroxido_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_hidroxido_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(1, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(1, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#7.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak, Hidroxidoak)
def formula_sortu_7(n):
    ordena=generate_vector(n,4)
    #print(ordena)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    hidroxidoak=formula_sortu_6(ordena[3])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2], hidroxidoak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3], hidroxidoak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4], hidroxidoak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5], hidroxidoak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0], hidroxidoak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1], hidroxidoak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#8.mailako bektorea sortzeko (Oxoazidoak)
def formula_sortu_8(n):
    df1=bekt_oxoazido_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_oxoazido_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(1, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(1, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#9.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak + Hidroxidoak + Oxoazidoak)
def formula_sortu_9(n):
    ordena=generate_vector(n,5)
    #print(ordena)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    hidroxidoak=formula_sortu_6(ordena[3])
    azidoak=formula_sortu_8(ordena[4])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2], hidroxidoak[2], azidoak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3], hidroxidoak[3], azidoak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4], hidroxidoak[4], azidoak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5], hidroxidoak[5], azidoak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0], hidroxidoak[0], azidoak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1], hidroxidoak[1], azidoak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#10.mailako bektorea sortzeko (Oxoazidoak)
def formula_sortu_10(n):
    df1=bekt_gatzhirutarra_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_gatzhirutarra_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(1, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(1, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#11.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak + Hidroxidoak + Oxoazidoak + GatzHirutarrak)
def formula_sortu_11(n):
    ordena=generate_vector(n,6)
    #print(ordena)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    hidroxidoak=formula_sortu_6(ordena[3])
    azidoak=formula_sortu_8(ordena[4])
    gatzhirutarrak=formula_sortu_10(ordena[5])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2], hidroxidoak[2], azidoak[2], gatzhirutarrak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3], hidroxidoak[3], azidoak[3], gatzhirutarrak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4], hidroxidoak[4], azidoak[4], gatzhirutarrak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5], hidroxidoak[5], azidoak[5], gatzhirutarrak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0], hidroxidoak[0], azidoak[0], gatzhirutarrak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1], hidroxidoak[1], azidoak[1], gatzhirutarrak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

@st.cache
@st.experimental_memo
def formulak_sortu(n, maila):
    #MAILAK (Hidruroak=1; Oxidoak=2; Hidr+Oxid =3; GatzBitarrak=4; Hidr+Oxid+Gatz2=5; Hidroxid=6; Hidr+Oxid+Gatz2+Hidrox=7...
    #...Azidoak=8; Hidr+Oxid+Gatz2+Hidrox+Azid=9; GatzHiru=10; Denak=11)
    if maila==1:
        emaitza=formula_sortu_1(n)
    elif maila==2:
        emaitza=formula_sortu_2(n)
    elif maila==3:
        emaitza=formula_sortu_3(n)
    elif maila==4:
        emaitza=formula_sortu_4(n)
    elif maila==5:
        emaitza=formula_sortu_5(n)
    elif maila==6:
        emaitza=formula_sortu_6(n)
    elif maila==7:
        emaitza=formula_sortu_7(n)
    elif maila==8:
        emaitza=formula_sortu_8(n)
    elif maila==9:
        emaitza=formula_sortu_9(n)
    elif maila==10:
        emaitza=formula_sortu_10(n)
    elif maila==11:
        emaitza=formula_sortu_11(n)
    return emaitza


#--------------TRADIZIONALIK GABE----------------------------
def formula_sortu_1_no_trad(n):
    df1=bekt_hidruro_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_hidruro_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(2, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(2, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#2.mailako bektorea sortzeko (Oxidoak)
def formula_sortu_2_no_trad(n):
    df1=bekt_oxido_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_oxido_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(2, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(2, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#3.mailako bektorea sortzeko (Hirdruroak + Oxidoak)
def formula_sortu_3_no_trad(n):
    ordena=generate_vector(n,2)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko


#4.mailako bektorea sortzeko (GatzBitarrak)
def formula_sortu_4_no_trad(n):
    df1=bekt_gatzbitarra_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_gatzbitarra_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(2, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(2, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#5.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak)
def formula_sortu_5_no_trad(n):
    ordena=generate_vector(n,3)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#6.mailako bektorea sortzeko (Hidroxidoak)
def formula_sortu_6_no_trad(n):
    df1=bekt_hidroxido_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_hidroxido_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(2, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(2, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#7.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak, Hidroxidoak)
def formula_sortu_7_no_trad(n):
    ordena=generate_vector(n,4)
    #print(ordena)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    hidroxidoak=formula_sortu_6(ordena[3])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2], hidroxidoak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3], hidroxidoak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4], hidroxidoak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5], hidroxidoak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0], hidroxidoak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1], hidroxidoak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#8.mailako bektorea sortzeko (Oxoazidoak)
def formula_sortu_8_no_trad(n):
    df1=bekt_oxoazido_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_oxoazido_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(2, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(2, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#9.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak + Hidroxidoak + Oxoazidoak)
def formula_sortu_9_no_trad(n):
    ordena=generate_vector(n,5)
    #print(ordena)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    hidroxidoak=formula_sortu_6(ordena[3])
    azidoak=formula_sortu_8(ordena[4])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2], hidroxidoak[2], azidoak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3], hidroxidoak[3], azidoak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4], hidroxidoak[4], azidoak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5], hidroxidoak[5], azidoak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0], hidroxidoak[0], azidoak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1], hidroxidoak[1], azidoak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#10.mailako bektorea sortzeko (Oxoazidoak)
def formula_sortu_10_no_trad(n):
    df1=bekt_gatzhirutarra_form(n)
    formulen_matrizea=df1.to_numpy()
    galderak_formula=formulen_matrizea[:,0]
    erantzunak_tradizionala= formulen_matrizea[:,1]
    erantzunak_stock=formulen_matrizea[:,2]
    erantzunak_sistematiko=formulen_matrizea[:,3]
    df2=bekt_gatzhirutarra_izena(n)
    izena_matrizea=df2.to_numpy()
    erantzunak_formulak =izena_matrizea[:,0]
    galderak_izena = np.empty(n, dtype=object)
    for i in range(n):
        a = random.randint(2, 3)
        while izena_matrizea[i][a] == "Ez da izendatzen":
            a = random.randint(2, 3)
            #print(a)
        galderak_izena[i]=izena_matrizea[i][a]
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko

#11.mailako bektorea sortzeko (Hidruroak + Oxidoak + GatzBitarrak + Hidroxidoak + Oxoazidoak + GatzHirutarrak)
def formula_sortu_11_no_trad(n):
    ordena=generate_vector(n,6)
    #print(ordena)
    hidruroak=formula_sortu_1(ordena[0])
    oxidoak=formula_sortu_2(ordena[1])
    gatzbitarrak=formula_sortu_4(ordena[2])
    hidroxidoak=formula_sortu_6(ordena[3])
    azidoak=formula_sortu_8(ordena[4])
    gatzhirutarrak=formula_sortu_10(ordena[5])
    galderak_formula=np.concatenate((hidruroak[2], oxidoak[2],gatzbitarrak[2], hidroxidoak[2], azidoak[2], gatzhirutarrak[2]), axis=0)
    erantzunak_tradizionala=np.concatenate((hidruroak[3], oxidoak[3],gatzbitarrak[3], hidroxidoak[3], azidoak[3], gatzhirutarrak[3]), axis=0)
    erantzunak_stock=np.concatenate((hidruroak[4], oxidoak[4],gatzbitarrak[4], hidroxidoak[4], azidoak[4], gatzhirutarrak[4]), axis=0)
    erantzunak_sistematiko = np.concatenate((hidruroak[5], oxidoak[5],gatzbitarrak[5], hidroxidoak[5], azidoak[5], gatzhirutarrak[5]), axis=0)
    erantzunak_formulak=np.concatenate((hidruroak[0],oxidoak[0],gatzbitarrak[0], hidroxidoak[0], azidoak[0], gatzhirutarrak[0]),axis=0)
    galderak_izena =np.concatenate((hidruroak[1],oxidoak[1],gatzbitarrak[1], hidroxidoak[1], azidoak[1], gatzhirutarrak[1]),axis=0)
    return erantzunak_formulak, galderak_izena, galderak_formula, erantzunak_tradizionala, erantzunak_stock, erantzunak_sistematiko


@st.cache
@st.experimental_memo
def formulak_sortu_no_trad(n, maila):
    #MAILAK (Hidruroak=1; Oxidoak=2; Hidr+Oxid =3; GatzBitarrak=4; Hidr+Oxid+Gatz2=5; Hidroxid=6; Hidr+Oxid+Gatz2+Hidrox=7...
    #...Azidoak=8; Hidr+Oxid+Gatz2+Hidrox+Azid=9; GatzHiru=10; Denak=11)
    if maila==1:
        emaitza=formula_sortu_1_no_trad(n)
    elif maila==2:
        emaitza=formula_sortu_2_no_trad(n)
    elif maila==3:
        emaitza=formula_sortu_3_no_trad(n)
    elif maila==4:
        emaitza=formula_sortu_4_no_trad(n)
    elif maila==5:
        emaitza=formula_sortu_5_no_trad(n)
    elif maila==6:
        emaitza=formula_sortu_6_no_trad(n)
    elif maila==7:
        emaitza=formula_sortu_7_no_trad(n)
    elif maila==8:
        emaitza=formula_sortu_8_no_trad(n)
    elif maila==9:
        emaitza=formula_sortu_9_no_trad(n)
    elif maila==10:
        emaitza=formula_sortu_10_no_trad(n)
    elif maila==11:
        emaitza=formula_sortu_11_no_trad(n)
    return emaitza

def check_answer(user_formulazioa, matrizea):
    n=len(user_formulazioa)
    nota=0
    for i in range(n):
        if user_formulazioa[i] == matrizea[0][i]:
            with col2:
                st.markdown(f"**{i + 1 + n}.-**  **{matrizea[0][i]}** ")
                st.success("Erantzun zuzena!")
            nota=nota+1
        else:
            with col2:
                st.markdown(f"**{i + 1 + n}.-**  **{matrizea1[0][i]}** ")
                st.error(f"Ez, {i+1+n}. galderaren erantzun zuzena hurrengoa da:")
                st.markdown(f" Formula:  {emaitzen_matr[0][i]} ")
    return nota

def check_answer_1(tradizionala_bek, stock_bek, sistematiko_bek, emaitzen_matr, i, nota):
    if tradizionala_bek[i].lower()==emaitzen_matr[i][1].lower():
        if stock_bek[i].lower() == emaitzen_matr[i][2].lower():
            if sistematiko_bek[i].lower() == emaitzen_matr[i][3].lower():
                with col2:
                    st.markdown(f"**{i + 1}.-**  **{matrizea[i][0]}** ")
                    st.success("Erantzun zuzena!")
                nota = nota + 1
            else:
                with col2:
                    st.markdown(f"**{i + 1}.-**  **{matrizea[i][0]}** ")
                    st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                    st.markdown(f" Tradizionala:  {emaitzen_matr[i][1]} ")
                    st.markdown(f" Stock:  {emaitzen_matr[i][2]} ")
                    st.markdown(f" Sistematikoa:  {emaitzen_matr[i][3]} ")
        else:
            with col2:
                st.markdown(f"**{i + 1}.-**  **{matrizea[i][0]}** ")
                st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                st.markdown(f" Tradizionala:  {emaitzen_matr[i][1]} ")
                st.markdown(f" Stock:  {emaitzen_matr[i][2]} ")
                st.markdown(f" Sistematikoa:  {emaitzen_matr[i][3]} ")
    else:
        with col2:
            st.markdown(f"**{i+1}.-**  **{matrizea[i][0]}** ")
            st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
            st.markdown(f" Tradizionala:  {emaitzen_matr[i][1]} ")
            st.markdown(f" Stock:  {emaitzen_matr[i][2]} ")
            st.markdown(f" Sistematikoa:  {emaitzen_matr[i][3]} ")
    return nota