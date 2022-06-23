

class TXTWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, details: dict):
        with open(self.filename, 'a') as file:
            result = f'{details["car_id"]},{details["car_details_url"]}\n'
            file.write(result)