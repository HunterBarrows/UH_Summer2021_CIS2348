# Hunter Barrows 1550107

# Final Project

# Import csv and datetime modules
import csv
from datetime import datetime


# create a class to def all functions needed to carry out the output files
class Invent_Out:

    def __init__(self, var):
        self.var = var

# This creates the Full list of inventory csv file (MUST HAVE "OUTPUT" FOLDER TO HAVE THIS FUNCTION WORK)

    def Invent_Full_List(self):
        with open('./output/FullInventory.csv', 'w') as file_output:
            vars = self.var
            reference = sorted(vars.keys(), key=lambda x: vars[x]['manu'])
            for var in reference:
                num_id = var
                manu = vars[var]['manu']
                type_product = vars[var]['type_product']
                date_of_service = vars[var]['date_of_service']
                item_damaged = vars[var]['item_damaged']
                price_item = vars[var]['price_item']
                file_output.write('{2},{0},{4},{3},{5},{1}\n'.format(manu, item_damaged, num_id, price_item, type_product, date_of_service))

# This creates the damaged inventory file and checks if the item are damaged (MUST HAVE "OUTPUT" FOLDER TO HAVE THIS FUNCTION WORK)

    def check_if_damaged(self):
        vars = self.var
        reference = sorted(vars.keys(), key=lambda x: vars[x]['price_item'], reverse=True)
        with open('./output/DamagedInventory.csv', 'w') as file_output:
            for var in reference:
                num_id = var
                manu = vars[var]['manu']
                type_product = vars[var]['type_product']
                date_of_service = vars[var]['date_of_service']
                item_damaged = vars[var]['item_damaged']
                price_item = vars[var]['price_item']
                if item_damaged:
                    file_output.write('{1},{0},{3},{2},{4}\n'.format(manu, num_id, price_item, type_product, date_of_service))

# This checks to see if the product are past the service date, if so outputs a file csv file called "PasrServiceDateInventory" (MUST HAVE "OUTPUT" FOLDER TO HAVE THIS FUNCTION WORK)

    def date_of_service_check(self):
        vars = self.var
        reference = sorted(vars.keys(), key=lambda x: datetime.strptime(vars[x]['date_of_service'], "%m/%d/%Y").date(), reverse=True)
        with open('./output/PastServiceDateInventory.csv', 'w') as file_output:
            for var in reference:
                num_id = var
                manu = vars[var]['manu']
                type_product = vars[var]['type_product']
                date_of_service = vars[var]['date_of_service']
                item_damaged = vars[var]['item_damaged']
                price_item = vars[var]['price_item']
                today_date = datetime.now().date()
                exp = datetime.strptime(date_of_service, "%m/%d/%Y").date()
                past_exp = exp < today_date
                if past_exp:
                    file_output.write('{2},{0},{4},{3},{5},{1}\n'.format(manu, item_damaged, num_id, price_item, type_product, date_of_service))

# This checks the inventory types and outputs the file name with the type of inventory for each type (MUST HAVE "OUTPUT" FOLDER TO HAVE THIS FUNCTION WORK)
    def invent_type(self):
        vars = self.var
        list_type = []
        reference = sorted(vars.keys())
        for var in vars:
            check_item = vars[var]['type_product']
            if check_item not in list_type:
                list_type.append(check_item)
        for info in list_type:
            file_name = info.capitalize() + 'Inventory.csv'
            with open('./output/'+file_name, 'w') as file_output:
                for var in reference:
                    num_id = var
                    manu = vars[var]['manu']
                    type_product = vars[var]['type_product']
                    date_of_service = vars[var]['date_of_service']
                    item_damaged = vars[var]['item_damaged']
                    price_item = vars[var]['price_item']
                    if info == type_product:
                        file_output.write('{2},{0},{3},{4},{1}\n'.format(manu, item_damaged, num_id, price_item, date_of_service))

# Main part of code that calls each function with the corresponding csv files

if __name__ == '__main__':
    vars = {}
    Input_files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for info in Input_files:
        with open(info, 'r') as csv_file:
            read = csv.reader(csv_file, delimiter=',')
            for row in read:
                id_num = row[0]
                if info == Input_files[0]:
                    vars[id_num] = {}
                    manu = row[1]
                    type_product = row[2]
                    item_damaged = row[3]
                    vars[id_num]['manu'] = manu.strip()
                    vars[id_num]['type_product'] = type_product.strip()
                    vars[id_num]['item_damaged'] = item_damaged
                elif info == Input_files[1]:
                    price_item = row[1]
                    vars[id_num]['price_item'] = price_item
                elif info == Input_files[2]:
                    date_of_service = row[1]
                    vars[id_num]['date_of_service'] = date_of_service
    inventory_information = Invent_Out(vars)
    inventory_information.Invent_Full_List()
    inventory_information.check_if_damaged()
    inventory_information.date_of_service_check()
    inventory_information.invent_type()
    referencing = []
    manu = []
    for var in vars:
        manu_check = vars[var]['manu']
        checked = vars[var]['type_product']
        if manu_check not in referencing:
            manu.append(manu_check)
        if checked not in referencing:
            referencing.append(checked)


# Gets input from user
    Inpt = None
    while Inpt != 'q':
        Inpt = input("\nEnter an item manufacturer and item type (ex: Apple phone) or enter 'q' to quit:\n")
        if Inpt == 'q':
            break
        else:
            manu_slct = None
            type_slct = None
            Inpt = Inpt.split()
            false_input = False
            for product in Inpt:
                if product in manu:
                    if manu_slct:
                        false_input = True
                    else:
                        manu_slct = product
                elif product in referencing:
                    if type_slct:
                        false_input = True
                    else:
                        type_slct = product
            if not manu_slct or not type_slct or false_input:
                print("No such item in inventory")
            else:
                reference = sorted(vars.keys(), key=lambda x: vars[x]['price_item'], reverse=True)
                item_exist = []
                simi_exist = {}

# gets today date and checks is product is past the date of service
                for var in reference:
                    if vars[var]['type_product'] == type_slct:
                        today_date = datetime.now().date()
                        date_of_service = vars[var]['date_of_service']
                        exp_service = datetime.strptime(date_of_service, "%m/%d/%Y").date()
                        past_date_of_service = exp_service < today_date
                        if vars[var]['manu'] == manu_slct:
                            if not past_date_of_service and not vars[var]['item_damaged']:
                                item_exist.append((var, vars[var]))
                        else:
                            if not past_date_of_service and not vars[var]['item_damaged']:
                                simi_exist[var] = vars[var]

# checks if item exist and outputs information for the product if it does otherwise stats "item does not exist"
                if item_exist:
                    var = item_exist[0]
                    num_id = var[0]
                    manu = var[1]['manu']
                    type_product = var[1]['type_product']
                    price_item = var[1]['price_item']
                    print("Your item is: {3}, {2}, {0}, {1}\n".format(type_product, price_item, manu, num_id))
                    if simi_exist:
                        same_price = price_item
                        close = None
                        close_price = None
                        for var in simi_exist:
                            if close_price == None:
                                close = simi_exist[var]
                                close_price = abs(int(same_price) - int(simi_exist[var]['price_item']))
                                num_id = var
                                manu = simi_exist[var]['manu']
                                type_product = simi_exist[var]['type_product']
                                price_item = simi_exist[var]['price_item']
                                continue
                            differnce = abs(int(same_price) - int(simi_exist[var]['price_item']))
                            if differnce < close_price:
                                close = var
                                close_price = differnce
                                num_id = var
                                manu = simi_exist[var]['manu']
                                type_product = simi_exist[var]['type_product']
                                price_item = simi_exist[var]['price_item']
                        print("You may, also, consider: {3}, {2}, {0}, {1}\n".format(type_product, price_item, manu, num_id))
                else:
                    print("No such item in inventory")