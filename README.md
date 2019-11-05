CSC 212 – Data Structures
Queues Assignment 



For this project, you are to modify the Employee class posted on Blackboard by adding a bonus field. The bonus field should be equal to zero when an Employee object is created. You need to add a setter and a getter method to the new bonus field.

The Dirany’s company saves all employee information in the dirany.txt file (attached). The file saves each employee’s information in a new line and all attributes are separated by tabs. For example, the first employee’s information on the first line in the dirany.txt file is as follows:
John	Smith	90000
John is the first name of the employee, Smith is the employee’s last name and 90000 is the employee’s annual salary.

Your program should read the dirany.txt file and create an Employee object for each employee in the file, then add the employees to a queue data structure in the same order you read them from the file. The Dirany’s company saves the employees records according to their longevity in the company.

You need to help the Dirany’s company, to calculate the bonus for each employee according to their longevity rule so the bonus of the first employee will be 20% of his/her salary and for each employee afterwards the percent of the bonus will be 1%less so the second employee will get 19% of his/her salary, the third employee will get 18% of his/her salary and so forth.

Your program should access the Employees’ objects in the queue, calculate the bonus field and set it for each Employee object and display the object status:  first name, last name, pay and bonus for each employee.

Also your program should calculate and display the number of the employees in the company and the total bonus that the company will pay for all its employees.

Make sure you break up your code into a set of well-defined functions. Each function should include a comment block that briefly describes it, its parameters and any return values. 
