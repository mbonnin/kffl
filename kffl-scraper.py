#!python

from bs4 import BeautifulSoup
import urllib3
import sys
import os.path
import time

class Player:
    """A class representing a player"""  
    
    def __init__(self, cells):
        self.number = cells[0].string
        self.rank   = cells[1].string
        self.fa     = cells[10].string
        self.name   = cells[4].contents[0].string
     
    def on_roster(self):
        return bool(self.name in roster)

    def free_agent(self):
        return bool(len(self.fa) > 1)
    
def print_player_ranks(position_page):

    # fetch the page source from the url
    http = urllib3.PoolManager()
    response = http.request('GET', position_page)
    soup = BeautifulSoup(response.data, 'lxml')

    # get all the tags that have the '.stats' CSS class 
    players = soup.select('.stats')

    print
    
    for i, player in enumerate(players):

        p = Player(player.find_all('td'))
    
        # on_roster = ''
        # if p.name in roster or len(p.fa) > 1:
            # on_roster = '*'
            # print '{0:<4}{1:<15}{2:<6}{3:<23}'.format(p.number, p.rank, p.fa, p.name)

        if p.on_roster() or p.free_agent():
            print '{0:<4}{1:<15}{2:<6}{3:<23}'.format(p.number, p.rank, p.fa, p.name)            

            if i == 0:
                print '{0:-<42}'.format('')

if __name__ == "__main__":

    # set some encoding flags to enable output of weird characters
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # read the current roster file
    roster_file = open('calvinball-roster.txt', 'r')
    roster = []
    for line in roster_file:
        roster.append(line.rstrip())

    # read the modified time on the cache
    print time.ctime(os.path.getmtime('rb.html'))
        
    urls =[]
    urls.append('http://www.kffl.com/a.php/131312/fantasy-football/Fantasy-Football-Rankings--QB---Week-3v')
    urls.append('http://www.kffl.com/a.php/131307/fantasy-football/Fantasy-Football-Rankings--RB---Week-3---PPR')
    urls.append('http://www.kffl.com/a.php/131308/fantasy-football/Fantasy-Football-Rankings--WR---Week-3---PPR')
    urls.append('http://www.kffl.com/a.php/131309/fantasy-football/Fantasy-Football-Rankings--TE---Week-3---PPR')
    
    for url in urls:
        print_player_ranks(url)

