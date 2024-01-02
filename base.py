import csv

class acc:
    input_file = ''
    def __init__(self, input_file):
        self.input_file = input_file

    def get_base_сsv(self):
        users = []
        with open(self.input_file, encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        return users

    def get_base_txt(self):
        f = open(self.input_file)
        users = [str(x) for x in f.readlines()]
        return users