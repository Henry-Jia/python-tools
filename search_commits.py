import json
import time
import requests
import random
import re

def search_words(commit:dict):
    commiter = commit['committer'] # the author of hte commit
    message = commit['message'] # the commit message
    # Github commits will be ignored
    if commiter['name'] != 'GitHub' and any(re.match(i,message,re.IGNORECASE) for i in search_list):
        print(commiter['name'] + ' : ' + message)# show the committer's name and his/her message

if __name__ == '__main__':
    main_url = 'https://api.github.com/'
    language = 'javascript' #choose a language

    page = random.randint(1,100)# choose a random page
    quant = 10 # choose the quantity of commits that will be returned

    # tuple with the words that wil be searched
    search_list = (
        'add',
        'test'
    )

    repos = requests.get(f'{main_url}search/repositories?q=language:{language}&per_page={quant}&page={page}')
    if repos.status_code == 200:
        con = json.loads(repos.content)# content of the search
        l = 0
        for i in con['items']:
            l +=1# loading...
            repos_commits = requests.get(f"{main_url}repos/{i['full_name']}/commits") # make a request in each repositories returning only commits
            if repos_commits.status_code == 200:
                commits = json.loads(repos_commits.content)#content of the json response
                for commit in commits:
                    search_words(commit['commit']) # make the search in each commit 
                    #(I used a method because otherwise it would look something like : commit['commit']['message'] kinda ugly ;-; )
                print('.'*l)
            else:
                print(json.loads(repos_commits.content)['message'])
            time.sleep(2) # delay

    else:
        print(json.loads(repos.content)['message'])
