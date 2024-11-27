import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE: str = 'finance_data.csv'
    COLUMNS: list = ["date","amount","category","description"]

    @classmethod
    def initialize_csv(cls)->None:
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,date:str,amount:int,category:str,description:str)->None:
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

    


CSV.initialize_csv()
CSV.add_entry("20-07-2024",125.64,"income","Salary")