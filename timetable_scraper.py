import requests
import datetime
import re
from bs4 import BeautifulSoup


class timetable():
    def __init__(self):
        self.created = datetime.datetime.now()
        self.updated = None
        self.tt = None
        self.url = "http://www.phys.nsu.ru/bfa/raspisanie/"
    
    def update(self):
        try:
            req = requests.get("https://table.nsu.ru/room/БА")
            soup = BeautifulSoup(req.text, "html.parser")
            table = soup.find(class_ = "time-table")
            tds = table.findAll("td")
            tds = [td for i, td in enumerate(tds) if i % 7 != 0]
            data = []
            week_data = []
            for time, td in enumerate(tds):
                cells = td.findAll('div', class_ = "cell")
                cell_data = []
                for cell in cells:
                    subject = cell.find(class_ = "subject").text
                    subject = re.sub(r"[^а-яА-Я.0-9] +","",subject)
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
            self.update = datetime.datetime.now()
            self.tt = data
        except Exception as e:
            print(e)
    
    def get_current(self, time):
        start_time = ["09:00", "10:50", "12:40",
                        "14:30", "16:20", "18:10", "21:10"]
        now = datetime.datetime.now()
        # time = now.strftime('%H:%M')
        # tmp = now
        # for t in start_time:
        #     tmp_time = datetime.datetime.strptime(t, '%H:%M')
        #     tmp = tmp.replace(hour = tmp_time.hour, minute = tmp_time.minute)
        #     print((now - tmp))
        day = now.weekday()
        week = now.isocalendar()[1]
        if week is not None:
            week = "Нечетная" if week % 2 == 1 else "Четная"
            if week == self.tt[time][day][0]["week"]:
                lesson = self.tt[time][day][0]
            else:
                lesson = self.tt[time][day][1]
        else:
            lesson = self.tt[time][day]
        print(lesson)


t = timetable()
t.update()
t.get_current()