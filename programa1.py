import streamlit as st
import pandas as pd
import numpy as np
import random
import math
from PIL import Image
import AUTOZUZENKETAK.bektore_sortzailea as bs

#image = Image.open(r'C:\Users\Regato\Desktop\STREAMLIT\FORMULAZIOA\AUTOZUZENKETAK\fisikasi.png')
image = Image.open(r'./AUTOZUZENKETAK/fisikasi.png')
#STREAMLIT ORRIALDEA
#--------------------------------------------------
st.set_page_config(layout="wide")
container1=st.container()
link = '[F i s i k a s i/Formulazioa](https://www.youtube.com/watch?v=O-t8mW5ODVA&list=PL9OLH4hN0qlrpRazhdB210OQEy5HkrwdO)'
st.markdown(link, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Formulazio ez-organikoa Euskeraz</h1>", unsafe_allow_html=True)
#container1=st.container()
with container1:
    st.image(image, width=200)
container2=st.container()
expander = st.expander("Frogaren konfigurazioa")
with expander:
    ariketa_mota = st.selectbox(
            'Aukeratu frogaren zailtasuna',
            options=["Hidruroak", "Oxidoak", "Hidruroak + Oxidoak", "Gatz Bitarrak",
                     "Hidruroak + Oxidoak + Gatz Bitarrak", "Hidroxidoak",
                     "Hidruroak + Oxidoak + Gatz Bitarrak + Hidroxidoak",
                     "Oxoazidoak", "Hidruroak + Oxidoak + Gatz Bitarrak + Hidroxidoak + Oxoazidoak",
                     "Gatz Hirutarrak", "Oxoazidoak",
                     "Hidruroak + Oxidoak + Gatz Bitarrak + Hidroxidoak + Oxoazidoak + Gatz Hirutarrak"])
    n = st.select_slider(
            'Aukeratu galdera kopurua',
            options=[4, 6, 8, 10, 12, 14, 16, 18, 20])
    aukera = st.radio(
            "Erabaki nomenklatura tradizionala erabili nahi duzun ala ez",
            ('Tradizionalarekin', 'Tradizionalik gabe'))
    #aukera_ordenatuta = st.radio(
     #   "Konposatuak modu ordenatuan nahi dituzu edo nahastuta",
      #  ('Ordenatuta', 'Nahastuta'))
with container2:
   st.markdown("<h3 style='text-align: center;"
              " color: black;'>OHARRAK</h3>",
               unsafe_allow_html=True)
   st.markdown("<div style='text-align: center; "
               "color: black;'>1.- Aplikazioak ez du *kobre* hitza onartzen, bakarrik *kupre*</div>",
               unsafe_allow_html=True)
   st.markdown("<div style='text-align: center; color: black;'>2."
                "- Konposaturen bat nomenklatura jakin batean izendatzen ez bada  *Ez da izendatzen* testua idatzi</div>",
                unsafe_allow_html=True)
   st.markdown("<div style='text-align: center; color: black;'>3."
               "- Froga berri bat egin nahi duzunean aurreko emaitzak borratu beharko dituzu erantzun laukietatik</div>",
               unsafe_allow_html=True)


col1, col2, col3= st.columns([3,1,3])
with col1:
   st.header("Galderak")
with col3:
   st.header("Erantzunak")

#----ERANTZUNAK ONDO DAUDEN IKUSTEKO FUNTZIOAK--------
def check_answer(user_formulazioa, matrizea):
    n=len(user_formulazioa)
    nota=0
    for i in range(n):
        if user_formulazioa[i] == matrizea[0][i]:
            with col3:
                st.markdown(f"**{i + 1 + n}.-**  **{matrizea[1][i]}** ")
                st.success("Erantzun zuzena!")
            nota=nota+1
        else:
            with col3:
                st.markdown(f"**{i + 1 + n}.-**  **{matrizea[1][i]}** ")
                st.error(f"Ez, {i+1+n}. galderaren erantzun zuzena hurrengoa da:")
                st.markdown(f" Formula:  {matrizea[0][i]} ")
                st.markdown(f" Birpasatzeko bideoa:  {matrizea[7][i]} ")
    return nota
def check_answer_no_trad(user_formulazioa, matrizea):
    n=len(user_formulazioa)
    nota=0
    for i in range(n):
        if user_formulazioa[i] == matrizea[0][i]:
            with col3:
                st.markdown(f"**{i + 1 + n}.-**  **{matrizea[1][i]}** ")
                st.success("Erantzun zuzena!")
            nota=nota+1
        else:
            with col3:
                st.markdown(f"**{i + 1 + n}.-**  **{matrizea[1][i]}** ")
                st.error(f"Ez, {i+1+n}. galderaren erantzun zuzena hurrengoa da:")
                st.markdown(f" Formula:  {matrizea[0][i]} ")
                st.markdown(f" Birpasatzeko bideoa:  {matrizea[7][i]} ")
    return nota

def check_answer_1(tradizionala_bek, stock_bek, sistematiko_bek, matrizea):
    n=len(tradizionala_bek)
    nota=0
    for i in range (n):
        if tradizionala_bek[i].lower()==matrizea[3][i].lower() or tradizionala_bek[i].lower()==matrizea[3][i].lower()[:-1]:
            if stock_bek[i].lower() == matrizea[4][i].lower() or stock_bek[i].lower()==matrizea[4][i].lower()[:-1]:
                if "(mon)" in matrizea[5][i].lower():
                    string=matrizea[5][i].lower()
                    berria =string.replace("(mon)", "")
                    berria1=string.replace("(", "")
                    berria1=berria1.replace(")","")
                    #print(berria)
                    #print(berria1)
                    if sistematiko_bek[i].lower() == berria.lower() or sistematiko_bek[i].lower()==berria.lower()[:-1]\
                            or sistematiko_bek[i].lower() == berria1.lower() or sistematiko_bek[i].lower()==berria1.lower()[:-1]:
                        with col3:
                            st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                            st.success("Erantzun zuzena!")
                        nota = nota + 1
                    else:
                        with col3:
                            st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                            st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                            st.markdown(f" Tradizionala:  {matrizea[3][i]} ")
                            st.markdown(f" Stock:  {matrizea[4][i]} ")
                            st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                            st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")

                elif "(mono)" in matrizea[5][i].lower():
                    string=matrizea[5][i].lower()
                    berria =string.replace("(mono)", "")
                    berria1=string.replace("(", "")
                    berria1=berria1.replace(")","")
                    #print(berria)
                    #print(berria1)
                    if sistematiko_bek[i].lower() == berria.lower() or sistematiko_bek[i].lower()==berria.lower()[:-1]\
                            or sistematiko_bek[i].lower() == berria1.lower() or sistematiko_bek[i].lower()==berria1.lower()[:-1]:
                        with col3:
                            st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                            st.success("Erantzun zuzena!")
                        nota = nota + 1
                    else:
                        with col3:
                            st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                            st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                            st.markdown(f" Tradizionala:  {matrizea[3][i]} ")
                            st.markdown(f" Stock:  {matrizea[4][i]} ")
                            st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                            st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
                else:
                    if sistematiko_bek[i].lower() == berria.lower() or sistematiko_bek[i].lower()==berria.lower()[:-1]\
                            or sistematiko_bek[i].lower() == berria1.lower() or sistematiko_bek[i].lower()==berria1.lower()[:-1]:
                        with col3:
                            st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                            st.success("Erantzun zuzena!")
                        nota = nota + 1
                    else:
                        with col3:
                            st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                            st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                            st.markdown(f" Tradizionala:  {matrizea[3][i]} ")
                            st.markdown(f" Stock:  {matrizea[4][i]} ")
                            st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                            st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
            else:
                with col3:
                    st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                    st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                    st.markdown(f" Tradizionala:  {matrizea[3][i]} ")
                    st.markdown(f" Stock:  {matrizea[4][i]} ")
                    st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                    st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
        else:
            with col3:
                st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                st.markdown(f" Tradizionala:  {matrizea[3][i]} ")
                st.markdown(f" Stock:  {matrizea[4][i]} ")
                st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")

    return nota
def check_answer_1_no_tradizionala(stock_bek, sistematiko_bek, matrizea):
    n=len(stock_bek)
    nota=0
    for i in range (n):
        if stock_bek[i].lower() == matrizea[4][i].lower() or stock_bek[i].lower()==matrizea[4][i].lower()[:-1]:
            if "(mon)" in matrizea[5][i].lower():
                string = matrizea[5][i].lower()
                berria = string.replace("(mon)", "")
                berria1 = string.replace("(", "")
                berria1 = berria1.replace(")", "")
                #print(berria)
                #print(berria1)
                ###
                if sistematiko_bek[i].lower() == berria.lower() or sistematiko_bek[i].lower() == berria.lower()[:-1] \
                        or sistematiko_bek[i].lower() == berria1.lower() or sistematiko_bek[
                    i].lower() == berria1.lower()[:-1]:
                    with col3:
                        st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                        st.success("Erantzun zuzena!")
                    nota = nota + 1
                else:
                    with col3:
                        st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                        st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                        st.markdown(f" Stock:  {matrizea[4][i]} ")
                        st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                        st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
                        #print("2")
            elif "(mono)" in matrizea[5][i].lower():
                string = matrizea[5][i].lower()
                berria = string.replace("(mono)", "")
                berria1 = string.replace("(", "")
                berria1 = berria1.replace(")", "")
                #print(berria)
                #print(berria1)
                ####
                if sistematiko_bek[i].lower() == berria.lower() or sistematiko_bek[i].lower() == berria.lower()[:-1] \
                        or sistematiko_bek[i].lower() == berria1.lower() or sistematiko_bek[
                    i].lower() == berria1.lower()[:-1]:
                    with col3:
                        st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                        st.success("Erantzun zuzena!")
                    nota = nota + 1
                else:
                    with col3:
                        st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                        st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                        st.markdown(f" Stock:  {matrizea[4][i]} ")
                        st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                        st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
                        #print("2")
            else:
                if sistematiko_bek[i].lower() == matrizea[5][i].lower() or sistematiko_bek[i].lower()==matrizea[5][i].lower()[:-1]:
                    with col3:
                        st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                        st.success("Erantzun zuzena!")
                    nota = nota + 1
                else:
                    with col3:
                        st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                        st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                        st.markdown(f" Stock:  {matrizea[4][i]} ")
                        st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                        st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
                        #print("2")
        else:
            with col3:
                st.markdown(f"**{i + 1}.-**  **{matrizea[2][i]}** ")
                st.error(f"Ez, {i + 1}. galderaren erantzun zuzenak hurrengoak dira:")
                st.markdown(f" Stock:  {matrizea[4][i]} ")
                st.markdown(f" Sistematikoa:  {matrizea[5][i]} ")
                st.markdown(f" Birpasatzeko bideoa:  {matrizea[6][i]} ")
                #print("3")
                #print(stock_bek[i].lower(), matrizea[4][i].lower())
                #print(sistematiko_bek[i].lower(),  matrizea[5][i].lower())
    return nota



def zailtasuna(mota):
    if mota=="Hidruroak":
        maila=1
    elif mota=="Oxidoak":
        maila=2
    elif mota=="Hidruroak + Oxidoak":
        maila=3
    elif mota=="Gatz Bitarrak":
        maila=4
    elif mota=="Hidruroak + Oxidoak + Gatz Bitarrak":
        maila=5
    elif mota=="Hidroxidoak":
        maila=6
    elif mota=="Hidruroak + Oxidoak + Gatz Bitarrak + Hidroxidoak":
        maila=7
    elif mota=="Oxoazidoak":
        maila=8
    elif mota=="Hidruroak + Oxidoak + Gatz Bitarrak + Hidroxidoak + Oxoazidoak":
        maila=9
    elif mota=="Gatz Hirutarrak":
        maila=10
    elif mota=="Hidruroak + Oxidoak + Gatz Bitarrak + Hidroxidoak + Oxoazidoak + Gatz Hirutarrak":
        maila=11
    return maila
#FUNTZIO NAGUSIA---------------------------------
def main(n,maila):
    matrizea1 = bs.formulak_sortu(n, maila)
    matrizea1=np.array(matrizea1)
    user_answers_trad = []
    user_answers_stock = []
    user_answers_sist = []
    user_answers_form = []
    puntuak = 0
    #Galderak agerraraziko ditugu lehenego zutabean
    for i in range(n): #Hemen formulaktik izenera
        with col1:
            st.markdown(f"**{i + 1}.-**  **{matrizea1[2][i]}** ")
            # Tradizionala
            user_answer_trad = st.text_input(f"Tradizionala:", key=f'answer_tr_{i}')
            user_answers_trad.append(user_answer_trad)
            # Stock
            user_answer_stock = st.text_input(f"Stock:", key=f'answer_st_{i}')
            user_answers_stock.append(user_answer_stock)
            # Sistematikoa
            user_answer_sist = st.text_input(f"Sistematiko:", key=f'answer_sis_{i}')
            user_answers_sist.append(user_answer_sist)
    for j in range(n): #Hemen izenetik formulara
        with col1:
            st.markdown(f"**{j + 1 + n}.-**  **{matrizea1[1][j]}** ")
            user_answer_form = st.text_input(f"Formula:", key=f'answer_form_{j + n}')
            user_answers_form.append(user_answer_form)
    if st.button("Ariketak zuzendu", key="frogatu"):
            puntuak = check_answer_1(user_answers_trad, user_answers_stock, user_answers_sist, matrizea1)
            puntuak = puntuak + check_answer(user_answers_form, matrizea1)
            st.header(f"Nota: {puntuak}/{2 * n}")
    #with container2:
    #    if st.button("Ariketak zuzendu", key="frogatu1"):
     #       puntuak = check_answer_1(user_answers_trad, user_answers_stock, user_answers_sist, matrizea1)
      #      puntuak = puntuak + check_answer(user_answers_form, matrizea1)
       #     st.header(f"Nota: {puntuak}/{2 * n}")

def main_no_tradizionala(n,maila):
    matrizea1 = bs.formulak_sortu_no_trad(n, maila)
    matrizea1 = np.array(matrizea1)
    user_answers_stock = []
    user_answers_sist = []
    user_answers_form = []
    puntuak = 0
    #Galderak agerraraziko ditugu lehenego zutabean
    for i in range(n): #Hemen formulaktik izenera
        with col1:
            st.markdown(f"**{i + 1}.-**  **{matrizea1[2][i]}** ")
            # Stock
            user_answer_stock = st.text_input(f"Stock:", key=f'answer_st_{i}')
            user_answers_stock.append(user_answer_stock)
            # Sistematikoa
            user_answer_sist = st.text_input(f"Sistematiko:", key=f'answer_sis_{i}')
            user_answers_sist.append(user_answer_sist)
    for j in range(n): #Hemen izenetik formulara
        with col1:
            st.markdown(f"**{j + 1 + n}.-**  **{matrizea1[1][j]}** ")
            user_answer_form = st.text_input(f"Formula:", key=f'answer_form_{j + n}')
            user_answers_form.append(user_answer_form)
    if st.button("Ariketak zuzendu", key="frogatu"):
            puntuak = check_answer_1_no_tradizionala(user_answers_stock, user_answers_sist, matrizea1)
            puntuak = puntuak + check_answer_no_trad(user_answers_form, matrizea1)
            st.header(f"Nota: {puntuak}/{2 * n}")
    #with container2:
     #   if st.button("Ariketak zuzendu", key="frogatu1"):
      #      puntuak = check_answer_1_no_tradizionala(user_answers_stock, user_answers_sist, matrizea1)
       #     puntuak = puntuak + check_answer_no_trad(user_answers_form, matrizea1)
        #    st.header(f"Nota: {puntuak}/{2 * n}")







if __name__ == '__main__':
    n = int(n / 2)
    if aukera=="Tradizionalarekin":
        main(n, zailtasuna(ariketa_mota))
    if aukera=="Tradizionalik gabe":
        main_no_tradizionala(n, zailtasuna(ariketa_mota))






