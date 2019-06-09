from bs4 import BeautifulSoup
from urllib import request
from openpyxl import Workbook
import urllib
import click

@click.command()
@click.argument('args',nargs=1)
def main(args):
    url='https://d1b10bmlvqabco.cloudfront.net/attach/inpg92dp42z2zo/hdff4poirlh7i6/io5hun2sdr21/mock_results.html'

    page = request.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")

    table=soup.find('table')
    rows = table.find_all('tr')

    book = Workbook()
    sheet = book.active

    i,j=0,0
    flag=0
    for tr in rows:
        cols=tr.findAll('td')
        flag=0
        i+=1
        j=1
        for k in cols:
            if flag==0:
                flag=1
                continue
            sheet.cell(row=i, column=j).value = str(k.string)
            j+=1


    book.save(args)

if __name__ == '__main__':
    main()
