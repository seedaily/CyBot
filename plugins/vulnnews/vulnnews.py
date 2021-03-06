# !vulnnews is used for querying Google News for CVE Vulnerability

import requests
import xml.etree.ElementTree as ET
from errbot import BotPlugin, botcmd, arg_botcmd

class vulnnews(BotPlugin):

    @botcmd # flags a command
    def vulnnews(self, msg, args):
        urlip = "https://news.google.com/news/rss/search/section/q/CVE%20vulnerability/CVE%20vulnerability?hl=en&gl=US&ned=us"

        try:
            website = requests.get(urlip)

            #read html code
            html = website.text.encode('utf-8')

            root = ET.fromstring(html)

            count = 1
            answer = "Your news:"

            for item in root.iter('item'):
                title = item.find('title').text
                link = item.find('link').text
                answer += "\r\n"
                answer += str(count) + ") " + title
                answer += "\r\n"
                answer += link
                count += 1

            return(answer)

        except:
            return("Could not retrieve page")
            exit()

