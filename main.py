import pandas as pd
import csv
from datetime import datetime
from pathlib import Path
from typing import Union
from data_entry import get_amount,get_category,get_date,get_description


class CSV:
    CSV_FILE: Union[str,Path] = 'finance_data.csv'
    COLUMNS: list[str] = ["date","amount","category","description"]

    @classmethod
    def initialize_csv(cls)->None:
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,*,date:str,amount:float,category:str,description:str)->None:
        new_entry: dict = {
            "date": date,
            "amount": amount,
            "category": category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

def add()->None:
    CSV.initialize_csv()
    date: str = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or hit 'enter' for today's date: ", 
        allow_default=True,
    )
    amount: float = get_amount()
    category: str = get_category()
    description: str = get_description()
    CSV.add_entry(date=date,amount=amount,category=category,description=description)
    

    


add()