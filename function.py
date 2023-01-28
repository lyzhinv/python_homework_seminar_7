
def print_bus():
    bus = read_data_from_file('bus.txt')
    print('|    Название|   Гос. номер|')
    print('-'*26)
    for name, number in bus:
        print('|     {:>7s}|    {:>9s}|'.format(name, number))
    print('')
    choose = int(input("""Для возврата в меню - 1 | Добавить автобус - 2
"""))
    if choose == 2:
        add_bus() 


def add_bus():
    with open('bus.txt', 'a+', encoding = 'utf8') as data:
        data.writelines('\n')
        data.writelines(input('Введите название автобуса: ') + ",")
        data.writelines(input('Гос. номер '))
        print('')
        print('Автобус добавлен!')
    choose = int(input("""Для возврата в меню - 1 | Добавить еще один автобус - 2 | Вывести обновленный список автобусов - 3
"""))
    if choose == 2:
        add_bus() 
    elif choose == 3:
        print_bus() 


def print_driver():
    drivers = read_data_from_file('driver.txt')
    print('|         Имя|     Фамилия|')
    print('-'*27)
    for firstname, lastname in drivers:
        print('|{:>12s}|{:>12s}|'.format(firstname, lastname))
    print('')
    choose = int(input("""Для возврата в меню - 1 | Добавить водителя - 2
"""))
    if choose == 2:
        add_driver()


def add_driver():
    with open('driver.txt', 'a+', encoding = 'utf8') as data:
        data.writelines('\n')
        data.writelines(input('Введите Имя: ') + ",")
        data.writelines(input('Введите Фамилию: ') )
        print('')
        print('Водитель добавлен!')
    choose = int(input("""Для возврата в меню - 1 | Добавить еще одного водителя - 2 | Вывести обновленный список водителей - 3
"""))
    if choose == 2:
        add_driver()
    elif choose == 3:
        print_driver() 


def print_route():        
    routes = read_data_from_file('route.txt')
    buses = read_data_from_file('bus.txt')
    drivers = read_data_from_file('driver.txt')
    print('|Маршрут|   №|    Водитель| Госномер|')
    print('-'*37)
    for r_name,r_number,r_bus,r_driver in routes:
        bus_number = get_item_by_id(r_bus,buses)
        driver_name = get_item_by_id(r_driver,drivers)
        print('|{:>7}|{:>4}|{:>12}|{:>9}|'.format(r_name, r_number, driver_name, bus_number))    
    print('')
    choose = int(input("""Для возврата в меню - 1 | Добавить маршрут - 2
"""))
    if choose == 2:
        add_route()
    

def add_route():
    with open('route.txt', 'a+', encoding = 'utf8') as data:
        data.writelines('\n')
        data.writelines(input('Введите ID маршрута: ') + ",")
        data.writelines(input('Введите номер маршрута: ') + ",")
        data.writelines(input('Введите ID автобуса: ') + ",")
        data.writelines(input('Введите ID водителя: '))
        print('')
        print('Маршурт добавлен!')
    choose = int(input("""Для возврата в меню - 1 | Добавить еще один маршрут - 2 | Вывести обновленный список маршрутов - 3
"""))
    if choose == 2:
        add_route()
    elif choose == 3:
        print_route() 


def read_data_from_file(file_name):
    rawdata_list = []
    with open(file_name, 'r', encoding = 'utf8') as datafile:
        for line in datafile:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list


def save_data_to_file(file_name, rawdata_list):
    with open(file_name, 'w', encoding = 'utf8') as datafile:
        for rawdata in rawdata_list:
            datafile.write(','.join(rawdata) + '\n')


def add_item_to_file(file_name, rawdata):
    with open(file_name, 'a', encoding = 'utf8') as datafile:
        datafile.write(','.join(rawdata) + '\n')


def get_item_by_id(id, records):
    for id_record, item_record in records:
        if id==id_record:
            return item_record
            break
    return None        
