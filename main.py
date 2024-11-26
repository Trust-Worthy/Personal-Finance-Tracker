import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = 'finance_data.csv'

    @classmethod
    def initialize_csv(cls):
        try: