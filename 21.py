import requests as req
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
from random import randint
import pandas as pd

df = pd.read_csv("H:\AllPython\PythonProjects/arter.csv", delimiter=";")

arter_svenska = []
arter_latin = []

for index, row in df.iterrows():
    arter_svenska.append(row["Svenska"])
    arter_latin.append(row["Latin"])

def test_latin():
    for i in arter_latin:
        index = arter_latin.index(i)
        svar = str(input(f"Vad heter {arter_svenska[index]} på latin?: ").lower())
        while svar != str(arter_latin[index].lower()):    
            svar = str(input("Fel svar, pröva igen: ").lower())
        else:
            print("Korrekt!")
test_latin()





