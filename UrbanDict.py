# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:33:32 2020

@author: Lekuid
"""

import tkinter as tk
import requests

def output_format(listing):
    meaning = listing['list'][0]['definition']
    return meaning

#Getting the meaning from the UrbanDictionary website using their API

def web_request(word):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":word}
    
    headers = {
        'x-rapidapi-key': "97b529b4b4msh42484512d38b7dfp134312jsn372925ad40ca",
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    listing = response.json()
    returned['text'] = output_format(listing)
    print(output_format(listing))



#GUI program for the same
height = 720
width = 1280
root = tk.Tk()
root.title('UrbanDic')

base = tk.Canvas(root, height=height, width=width, bg='#36311F')
base.pack()

main_frame = tk.Frame(base, bg='#F2D0A4')
main_frame.place(relwidth=0.4, relheight=1)

word = tk.Entry(main_frame, bg='#ffeccc', font=40)
word.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.05)

submit = tk.Button(main_frame, text='Enlighten Me', bg='#A4303F', font=20, command=lambda: web_request(word.get()))
submit.place(relx=0.35, rely=0.11, relheight=0.03, relwidth=0.3)

returned = tk.Label(base, bg='#ffeccc', wraplengt=200)
returned.place(relx=0.413, rely=0.02, relheight=0.96, relwidth=0.57)


root.mainloop()