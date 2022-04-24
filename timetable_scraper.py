import requests
import datetime
import re
from bs4 import BeautifulSoup


class timetable():
    def __init__(self):
        self.created = datetime.datetime.now()
        self.updated = None
        self.tt = []
        self.url = "http://www.phys.nsu.ru/bfa/raspisanie/"
    
    def update(self):
        req = requests.get("https://table.nsu.ru/room/БА")
        soup = BeautifulSoup(req.text, "html.parser")
        table = soup.find(class_ = "time-table")
        tds = table.findAll("td")
        tds = [td for i, td in enumerate(tds) if i%7 != 0]
        data = []
        week_data = []
        for time, td in enumerate(tds):
            cells = td.findAll('div', class_ = "cell")
            cell_data = []
            for cell in cells:
                subject = cell.find(class_ = "subject").text
                subject = re.sub(r"[^а-яА-Я.] +","",subject)
                if subject == "Контрольные раб.":
                    continue
                tutor = cell.find(class_ = "tutor").text
                tutor = re.sub(r"[^а-яА-Я.] +","",tutor)
                week = cell.find(class_ = "week")
                if week is not None:
                    week = week.text
                    week = re.sub(r"[^а-яА-Я.]","",week)
                cell_data.append({"subject": subject, "tutor": tutor, "week": week})
            week_data.append(cell_data)
            if time % 6 == 5:
                data.append(week_data)
                week_data = []
        for i in data:
            print(i)
            print()


t = timetable()
t.update()