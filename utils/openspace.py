import random
import pandas as pd
from .table import Table

class Openspace:
    def __init__(self,number_of_tables:int, seats_per_table:int=4): #Each table has 4 seats
        self.number_of_tables=number_of_tables
        self.tables=[Table(seats_per_table) for i in range(number_of_tables)] #table is a list, and has attibute of 4 seats

    def organize(self,names:list[str]) -> None:  #randomly assign names to tables
        random.shuffle(names)  #all name are arranged randomly

        for name in names:
            assigned=False #remark if this person does not find a table
            for table in self.tables: 
                if table.has_free_spot(): #assign a seat to this person as long as this table has a empty seat
                    table.assign_seat(name)
                    assigned=True
                    break
            if not assigned: #If someone has no seat and table, print their name and remark no seat and table
                    print(f"No seat for {name}. No more table.")
                    
    
    def display(self) -> None:
        for i,table in enumerate(self.tables,1):  #enumerate function gives numbers/index to tables from 1 and get each element too
            occupants = []   
            for seat in table.seats: # get person's name who already has a table and a seat, save those name into occupants list
                if seat.occupant:
                    occupants.append(seat.occupant)
                else:
                    occupants.append("Empty")
            print(f"Table{i}:{occupants}") #print all table numbers and occupant of this table

    def store(self,filename:str) ->None:
        data=[] #save all imformation of tables and occupants as a excel file
        for table_num,table in enumerate(self.tables,1):
            for seat_num, seat in enumerate(table.seats,1):
                occupant= seat.occupant if seat.occupant else ""
                data.append({
                    "Table":table_num,
                    "Seat_num":seat_num,
                    "Occupant":occupant
                })
        df=pd.DataFrame(data)   #import pandas for saving it to excel
        df.to_excel(filename,index=False)
        print(f"Already save these data to {filename}")