import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

if __name__ == '__main__':

    filenames = [f'./files/file {number}.txt' for number in range(1, 5)]

    start = datetime.datetime.now()

    for name in filenames:
        read_info(name)

    end = datetime.datetime.now()
    print(f'Линейный вызов - {end - start}')

    start = datetime.datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.datetime.now()
    print(f'Многопроцессный - {end - start}')
