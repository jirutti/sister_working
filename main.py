from fastapi import FastAPI
from typing import Optional
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get('/company/{vatId}')
async def root(vatId: str):
    try:
        api_url = 'https://vsreg.rd.go.th/VATINFOWSWeb/jsp/VATInfoWSServlet'
        json = {
            "operation": "searchByTin",
            "goto_page": "",
            "tin": "on",
            "txtTin": vatId,
            "branotxt": ""
        }
        response = requests.post(api_url, data=json)
        soup = BeautifulSoup(response.text, 'html.parser')
        find_word = soup.find_all("td", { "align": "left", "width": 167 })
        print(find_word)
        value = str(find_word[0]).split('<td "="" align="left" width="167"><b><font color="#0000FF" size="2">')
        value = str(value[1]).split('</font></b></td>')[0]
        value = str(value).split("\r")[0]
        print(value)
        return { "company": value }
    except Exception as err:
        print(err)