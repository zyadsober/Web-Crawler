#Python Search Engine
#import modules
import urllib2
from bs4 import BeautifulSoup
import mysql.connector
#connect to mysql database
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='search')
cursor = cnx.cursor()
#define variables
id = 1
response = 1
#get page sourcecode function
def getpage(page_url):
    try:
        stop = 0
        global response
        global nextlink
        request = urllib2.Request(page_url)
        #
        try:
            response = urllib2.urlopen(request)
            #contents = resp.read()
        except urllib2.HTTPError, error:
            contents = error.read()
        #
        #response = urllib2.urlopen(request)
        soup = BeautifulSoup(response)
        #handle the links
        for div in soup.findAll('div'):
            if div.has_key('onclick'):
                currentlink = div['onclick']
                #print currentlink
                if currentlink:
                    currentonclick = div['onclick'][0:22]
                    if(currentonclick == "window.location.href='"):
                       currentlink = nextlink + div['onclick'][23:-1]
                       print currentlink
                       add_site = ("INSERT INTO sites "
                          "(id, site, explored) "
                          "VALUES (%s, %s, %s)")
                       global id
                       
                       site_prop = (id, currentlink, 0)
                       cursor.execute(add_site, site_prop)
                       id = id + 1
        for a in soup.findAll('a'):
            if a.has_key('href'):
                currentlink = a['href']
                #print currentlink
                if currentlink:
                    currentfirstchar = a['href'][0]
                    currentfirstsevenchar = a['href'][0:7]
                    if currentfirstsevenchar == 'http://' or currentfirstsevenchar == 'https:/':
                        #cursor.execute("SELECT exists FROM sites WHERE site = '%s'" % (currentlink))
                        #print 'http'
                        print currentlink
                        #insert to database
                        add_site = ("INSERT INTO sites "
                           "(id, site, explored) "
                           "VALUES (%s, %s, %s)")
                        global id
                        
                        site_prop = (id, currentlink, 0)
                        cursor.execute(add_site, site_prop)
                        #getpage(currentlink)
                    elif currentfirstchar == '/':
                        if nextlink[-1] == '/':
                            curaddition = currentlink[1:]
                            currentlink = nextlink + curaddition
                        else:
                            currentlink = nextlink  + currentlink
                        add_site = ("INSERT INTO sites "
                           "(id, site, explored) "
                           "VALUES (%s, %s, %s)")
                        global id
                        
                        site_prop = (id, currentlink, 0)
                        cursor.execute(add_site, site_prop)
                        #print nextlink + curaddition
                        #print "Done"
                        #print '/'
                        print currentlink####
                    else:
                        pass
                        #print 'other'
                        #print currentlink####
                    id = id + 1

                       
    except:
        pass
    #updateexplored = ("UPDATE sites"
     #   "SET explored = 1"
      #  "WHERE site = %s")

    #print page_url
    sql = "UPDATE sites SET explored = 1 WHERE site = '%s'" % (page_url)
    cursor.execute (sql)
    #which_site = (page_url)
    #cursor.execute(updateexplored, which_site)
    
    query = ("SELECT site FROM sites "
         "WHERE explored = 0 ORDER BY  id ASC")
    cursor.execute(query)
    #global stop
    for (site) in cursor:
        if stop == 0:
            nextlink = site[0]
            stop = 1
    #print nextlink
    getpage(nextlink)
          #print("{}".format(site))
#call the function
print "Crawling the web..."
query = ("SELECT site FROM sites "
         "WHERE explored = 0 ORDER BY  id ASC")
cursor.execute(query)
stop = 0
for (site) in cursor:
    if stop == 0:
        nextlink = site[0]
        stop = 1
#print nextlink
getpage(nextlink)
#getpage('http://google.com')

cnx.commit()
cursor.close()
cnx.close()
