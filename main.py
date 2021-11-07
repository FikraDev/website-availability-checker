from datetime import datetime
import requests, schedule, time

def checkSite():
    sites = ['https://www.goprodigy.com', 'https://www.cnn.com', 'https://www.icaj.org', 'https://www.pabenjamin.com/', 'https://www.homeandthingsja.com/']

    for site in sites:
        r = requests.get(site)
    
        if r.status_code != 200:
            print('Site Down***', r.url, r.status_code)
            logfile = open("logfile.txt", 'a')
            logfile.write('{} - {} is Down***. Error Code {} \n'.format(datetime.now(), r.url, r.status_code))
            logfile.close()
        else:
            print('Site is up', r.url)
    print()
    print()
    
schedule.every(5).seconds.do(checkSite)

while True:
    schedule.run_pending()
    time.sleep(1)






# r = requests.get('https://xkcd.com/353/')





