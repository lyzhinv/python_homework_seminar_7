from menu import Menu
import function as fn 

if __name__ == "__main__":
    menuitems = [
        ("1", "Вывод автобусов", fn.print_bus),
        ("2", "Добавить автобус", fn.add_bus),
        ("3", "Вывод водителей", fn.print_driver),
        ("4", "Добавить водителей", fn.add_driver),
        ("5", "Вывод маршрутов", fn.print_route),
        ("6", "Добавить маршрут", fn.add_route),
        ("7", "Выход", lambda: exit())]

    menu = Menu(menuitems)
    menu.run('→ ')