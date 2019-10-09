#!/usr/bin/env python3

"""
Add the API key from NASA's website
Change the save_path on the "main" function to specify where the image will be stored
"""
import requests 
import json 
import shutil
import os 
import ctypes
import platform
import datetime 
import random


API_KEY = ''

#desired_day =  str(datetime.datetime.today().strftime('%Y-%m-%d'))
link = lambda date: r'https://api.nasa.gov/planetary/apod?date='+date+'&api_key=' + API_KEY

def get_random_Date():
    start_dt = datetime.date.today().replace(day=1, month=1).toordinal()
    end_dt = datetime.date.today().toordinal()
    random_day = datetime.date.fromordinal(random.randint(start_dt, end_dt))
    return str(random_day.strftime('%Y-%m-%d'))

def get_response(date = None):
    desired_day = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    if date is not None:
        desired_day = date

    get_link = link(desired_day)
    r = requests.get(get_link)    # get the information for the current day image

    if r.status_code == 200:

        return r.json()
    else:
        return None


def get_img(path):
    
    json_response = get_response()
    if json_response is not None:     # request went without problems
        try:
            response = requests.get(json_response['hdurl'], stream = True)  # download hd image
            save_image(path,response)
        except KeyError:
            if json_response['media_type'] == 'video':
                random_Date = get_random_Date()
                random_request = get_response(random_Date)
                max_iter = 2
                cnt = 0
                while random_request is None or 'hdurl' not in random_request and cnt < max_iter:
                    random_Date = get_random_Date()
                    random_request = get_response(random_Date)
                    cnt += 1
                response = requests.get(random_request['hdurl'], stream = True)  # download hd image

                save_image(path,response)
    else:
        return -1

def save_image(path,response):
    with open(path, 'wb') as out_file:                    # write to file 
        shutil.copyfileobj(response.raw, out_file)

def main():
    """
    Downloads the current photo of the day from NASA's photo of the day website. If the "photo of the day" is not
    an image, then it shall use a random date. When a new image is downloaded, the old one is deleted.
    
    Works for windows and Linux.
    
    How to use:
        Add your API key to the API_KEY varible;
        Change save_path to the path to the folder in which the image will be stored.
    """
    save_path = ''

    if get_img(save_path) == -1:
        return -1
    system = platform.system()
    if system == 'Windows': 
        ctypes.windll.user32.SystemParametersInfoW(20, 0, save_path , 0)

    elif system == "Linux":
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+  save_path)

main()
