import random
import pandas as pd
from table import Table

class Openspace:
    def __init__(self,numbers_of_tables:int, seats_of_table:int=4): #Each table has 4 seats
        self.number_of_tables=numbers_of_tables
        self.tables=[Table(seats_of_table) for i in range(numbers_of_tables)]

    def organize(self,names:list[str]) -> None:  #randomly assign names to tables
        random.shuffle(names)
        for name in names:
            assigned=False #remark if this person find a seat
            for table in self.tables: 
                if table.has_free_spot(): #assign a seat to a name as long as this table has a empty seat
                    table.assign_seat(name)
                    break
            if not assigned:
                print("No more table.")
    
    def display(self) -> None:
        for i,table in enumerate(self.tables.1):  #give numbers to tables from 1 and get each element too
            occupants = []
            for seat in table.seats:
                if seat.occupant:
                    occupants.append(seat.occupant)
                else:
                    occupants.append("Empty")
            print(f"Table{i}:{occupants}") #print all tables and occupants state

    def store(self,filename:str) ->None:
        data=[] #save all imformation of tables and occupants as a excel file
        for i,table in enumerate(self.tables,1):
            for seat_num,seat in enumerate(table.seats,1):
                occupant= seat.occupant if seat.occupant else ""
                data.append({
                    "Table":i,
                    "Seat_num":seat_num,
                    "Occupant":occupant
                })
        df=pd.DataFrame(data)   #import pandas for saving it to excel
        df.to_excel(filename,index=False)
        print(f"Already save these data to {filename}")