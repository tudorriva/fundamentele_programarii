from modelle.Identifizierbar import Identifizierbar
from functools import reduce
from datetime import datetime,timedelta

class Bestellung(Identifizierbar):
    def __init__(self,id,kundenID,gerichteIDs,getrankeIDs,gesamtkosten=None):
        super().__init__(id)
        self.kundenID = kundenID
        self.gerichteIDs = gerichteIDs
        self.getrankeIDs = getrankeIDs
        self.gesamtkosten = gesamtkosten

    def calculateCosts(self,drinkRepo,foodRepo):
        objects = self.getRechnung(drinkRepo,foodRepo)

        costs = [object.preis for object in objects]

        self.gesamtkosten = reduce(lambda x,y:int(x)+int(y),costs)


    def getRechnung(self,drinkRepo,foodRepo):
        drinks = drinkRepo.load()
        food = foodRepo.load()

        objects = drinks + food
        ids_to_search = self.gerichteIDs + self.getrankeIDs
        found_objects = []
        for id in ids_to_search:
            for object in objects:
                if object.id == id:
                    found_objects.append(object)
                    break

        return found_objects


    def getDates(self,drinkRepo,foodRepo):
        objects = self.getRechnung(drinkRepo,foodRepo)
        times = []
        
        for object in objects:
            if hasattr(object,'zubereitungszeit'):
                times.append(int(object.zubereitungszeit))

        current_time = datetime.now()
        if len(times) == 0:
            return current_time,current_time
        final_time = max(times)
        hours_to_add = final_time // 60
        minutes_to_add = final_time % 60

        time_delta = timedelta(hours=hours_to_add,minutes=minutes_to_add)

        final_time = current_time + time_delta

        return current_time,final_time

    def showRechnung(self,drinkRepo,foodRepo):
        objects = self.getRechnung(drinkRepo,foodRepo)
        dates = self.getDates(drinkRepo,foodRepo)

        print(f'client ID: {self.kundenID}')
        print(f'ordered: {dates[0]}         finalised: {dates[1]}')
        for object in objects:
            print(f'Name: {object.name}  -  Portionsgrosse: {object.portionsgrosse}  -  {object.preis}$')
        print(f'Total: {self.gesamtkosten}')
