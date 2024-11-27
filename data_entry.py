from datetime import datetime

date_format = "%d-%m-%Y"

def get_date(prompt:str, allow_default=False)->str:
    date_str:str = input(prompt)

    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt,allow_default)
    


def get_amount()->float:
    try:
        amount: float = float(input("Enter the amount: "))
        if amount <=0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    

def get_category():
    raise NotImplementedError

def get_description():
    raise NotImplementedError