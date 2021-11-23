class NegativeNumberError(Exception):
    pass


class OnlyIntError(Exception):
    pass


class OfficeEquipment:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f'{self.name} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, name, model, printer_type, paper_size, print_color):
        super().__init__(name, model)
        self.printer_type = printer_type
        self.paper_size = paper_size
        self.print_color = print_color


class Scanner(OfficeEquipment):
    def __init__(self, name, model, scanner_type, print_resolution, paper_size):
        super().__init__(name, model)
        self.scanner_type = scanner_type
        self.print_resolution = print_resolution
        self.paper_size = paper_size


class CopyMachine(OfficeEquipment):
    def __init__(self, name, model, print_speed, paper_size, print_color):
        super().__init__(name, model)
        self.print_speed = print_speed
        self.paper_size = paper_size
        self.print_color = print_color


class Warehouse:
    name = 'Склад оргтехники'

    def __init__(self):
        self.stored_in_warehouse = {}
        self.transfer_to_sales_dep = {}
        self.transfer_to_accounting_dep = {}

    def to_accept(self, key: OfficeEquipment, amount):
        try:
            if not isinstance(amount, int):
                raise OnlyIntError(f'Количество принтеров должно быть числом')
        except OnlyIntError as err:
            print(err)
        else:
            if key in self.stored_in_warehouse:
                self.stored_in_warehouse[key] += amount
            else:
                self.stored_in_warehouse[key] = amount
            print(f'Принято на склад: {key}, {amount} шт. (всего на складе - {self.stored_in_warehouse[key]} шт.)')

    def to_transfer(self, key: OfficeEquipment, amount, departament):
        if departament == 'отдел продаж':
            try:
                if self.stored_in_warehouse[key] < amount:
                    raise NegativeNumberError(f'Остаток позиции {key} на складе меньше необходимых {amount} шт.')
            except NegativeNumberError as err:
                print(err)
            else:
                self.stored_in_warehouse[key] -= amount
                if key in self.transfer_to_sales_dep:
                    self.transfer_to_sales_dep[key] += amount
                else:
                    self.transfer_to_sales_dep[key] = amount
                    print(f'Передано со склада: {key}, {amount} шт. в {departament}.')
            finally:
                print(f'Остаток позиции на складе - {self.stored_in_warehouse[key]} шт.')

        elif departament == 'отдел бухгалтерии':
            try:
                if self.stored_in_warehouse[key] < amount:
                    raise NegativeNumberError(f'Остаток позиции {key} на складе меньше необходимых {amount} шт.')
            except NegativeNumberError as err:
                print(err)
            else:
                self.stored_in_warehouse[key] -= amount
                if key in self.transfer_to_accounting_dep:
                    self.transfer_to_accounting_dep[key] += amount
                else:
                    self.transfer_to_accounting_dep[key] = amount
                print(f'Передано со склада: {key}, {amount} шт. в {departament}.')
            finally:
                print(f'Остаток позиции на складе - {self.stored_in_warehouse[key]} шт.')


printer_hp = Printer('HP LaserJet', 'M15', 'laser', 'A4', 'monochrome')
printer_epson = Printer('Epson', 'L121', 'jet', 'A4', 'multicolor')
scanner_canon = Scanner('Canon imageFORMULA', 'S-130', 'broaching', '600', 'A4')
copy_xerox = CopyMachine('Xerox WorkCentre', '5020', '20', 'A3', 'multicolor')
storage1 = Warehouse()

storage1.to_accept(printer_hp, 6)
storage1.to_accept(printer_hp, 2)
storage1.to_accept(printer_epson, 8)
storage1.to_accept(scanner_canon, 6)
storage1.to_accept(copy_xerox, '10')  # OnlyIntError
print('----------')
storage1.to_transfer(printer_epson, 5, 'отдел продаж')
storage1.to_transfer(printer_hp, 4, 'отдел бухгалтерии')
storage1.to_transfer(printer_hp, 6, 'отдел продаж')  # NegativeNumberError
