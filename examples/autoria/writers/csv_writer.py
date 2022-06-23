import csv


class CSVWriter:
    def __init__(self, filename: str):
        self.filename = filename
        self._write_headers = True

    def write(self, details: dict):

        headers = [
            'Car Id',
            'Car Details URL',
        ]
        fields = [
            details['car_id'],
            details['car_details_url'],
        ]

        with open(self.filename, 'a') as f:
            writer = csv.writer(f)

            if self._write_headers:
                writer.writerow(headers)
                self._write_headers = False

            writer.writerow(fields)
