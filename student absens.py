import datetime
class College():
    def __init__(self,name,today):
        self.name=name
        self.today=today
    def absent(self,):
        today=datetime.date.today()
        ab=today.year-self.today
    if today != datetime.date(today.year,self.name,self.today):
        absent-=1
    return absent
