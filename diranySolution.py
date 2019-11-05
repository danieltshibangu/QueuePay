class Queue:
    def __init__( self ):
        self.items = []
        
    def is_empty( self ):
        return self.items == []
    
    def enqueue( self, item ):
        self.items.insert( 0, item )
        
    def dequeue( self ):
        return self.items.pop()
    
    def size( self ):
        return len( self.items )

#-------------------------------------------------------------

#this program is to demo the use of classes
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        self.bonus = 0

    def getPay(self):
        return self.pay

    def setPay(self,pay):
        self.pay=pay

    # setter method for bonus
    def setBonus( self, amount ):            
        self.bonus = amount
        
    # getter method for bonus
    def getBonus( self ):
        return self.bonus
        
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
       

    def __str__(self):
       return '\nEmployee name: '+ self.fullName() +\
              '\nEmployee pay: ' + str(self.pay) +\
              '\nEmployee bonus: ' + str( format(self.bonus, '.2f') )

#-----------------------------------------------------------------------

# this is the main function
def main():

    # keep a bonus total and pay rate
    payRate = 0.2
    totalBonus = 0 

    # create queue to employees
    employeeQ = Queue()

    # open the dirany text file
    dirany_file = open( '/Users/danieltshibangu/Desktop/dirany.txt', 'r' )

    # read the first line of file
    lineData = dirany_file.readline()

    # translate it into employee objects
    while lineData != "":
        data_attr = lineData.split()

        # create an employee obj with 3 parameters
        # 1st is first name, 2nd is last name
        # 3rd is the pay
        employee = Employee( data_attr[0], data_attr[1], data_attr[2] )

        # calculate the bonus as pay times the pay rate 
        employee.setBonus( float( data_attr[2] ) * payRate )

        # add to the total bonus
        totalBonus += employee.getBonus() 

        # enqueue to the list
        employeeQ.enqueue( employee )

        # add 1 to employee and cut rate by 1
        payRate -= 0.01

        # read the next line
        lineData = dirany_file.readline()

    # close the file
    dirany_file.close()

    # print the number of employees and the total bonus
    print( "The total number of employees:", employeeQ.size() )
    print( "The total bonus amount:", format( totalBonus, '.2f' ) )

    # displays each item in the queue
    print( "\nDisplays all the objects in the queue:" ) 
    for item in range( employeeQ.size() ):
        print( employeeQ.dequeue() )

if __name__ == "__main__":
    main()

