import csv


this_level = 1

lives = 5
player_lives = 5


blue_ghosts_num = 2
red_ghosts_num = 1
green_ghosts_num = 0
orange_ghosts_num = 0
apples_rate = 0


default_level = object()
def load_from_file(file='stats.csv', level=default_level):
    global blue_ghosts_num, red_ghosts_num, green_ghosts_num, orange_ghosts_num, this_level

    if level is default_level:
        level = this_level

    this_level = level
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        row_count = sum(1 for row in csv_reader)
        csvfile.seek(0)
        level = min(level + 1, row_count)

        for i in range(level):
            row = next(csv_reader)

        blue_ghosts_num = int(row[0])
        red_ghosts_num = int(row[1])
        green_ghosts_num = int(row[2])
        orange_ghosts_num = int(row[3])
