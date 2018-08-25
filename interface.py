#Python version 3.3.3
from Garage import *
from Queue import *

begin = """

 ==============================================================================
 ==============================================================================
 ====                  -------- LAUGHF CAR PARK --------                   ====
 ==============================================================================
 ==============================================================================

                             === INSTRUCTIONS ===


 > Enter to the Car Park                       > Exit from the Car Park

    1)Type 'Enter'                                1)Type 'Exit'
    2)Type <Vehicle Plate Number>                 2)Type <Vehicle Plate Number>

 > TO Exit from the programme
    1)Type 'Close'
 
"""
print(begin)

garage = Garage(10)
exList = Queue()
count = Queue()

while True:
    com = input('Enter the Command to continue : ')
    if com == 'Enter':
        lPlate = input('Enter the Plate Number : ')

        if garage.isExist(lPlate) == True:
            print('The vehicle is already in the car park !\n')
            #return
        else:
            if garage.isFull() == False:
                garage.entry(lPlate)
                print('The Plate Number ',lPlate,' has been entered successfully !\n')
                #return
            else:
                exList.enqueue(lPlate)
                print('Sorry ! Car Park is already full.\n','Please wait for a moment...\n')

    elif com == 'Exit':
        lPlate = input('Enter the Plate Number : ')
        
        if garage.garage.size() == 0:
            print("There isn't any vehicle in here !!!")
        elif garage.garage.size() > 0:
            if garage.isExist(lPlate) != True:
                garage.exits(lPlate)
                print('The Plate Number ',lPlate,' exits successfully from the Car Park !')
            if exList.isEmpty() != True:
                if exList.findItem(lPlate):
                    exList.removeItem(lPlate)
                    print('The Plate Number',lPlate,'vehicle exits from the waiting list')
                else:
                    print("There isn't any vehicle as ",lPlate)
            if garage.garage.size() == (garage.gSize - 1):
                print('There is a space for an one vehicle.')
                if exList.isEmpty() != True:
                    lPlate = exList.dequeue()
                    garage.entry(lPlate)
                    print('The Plate Number ',lPlate,' has been entered successfully !\n')
                else:
                    print("The waiting list is Empty\n")

    elif com == 'Close':
        print('Bye !!!\nThanks for comming')
        break

    else:
        print('Please Use Given Instructions !')

    

    
             

            

    
