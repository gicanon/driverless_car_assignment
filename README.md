# driverless_car_assignment

The Driverless Car Assignment is an object-oriented program that relates to the characteristics of a driverless car. Four scenarios are included:

1. Registration of an account for the driverless car
2. Route planning
3. Dealing with a traffic light
4. Detecting obstacles

## Description & Approach

My approach to the development of the driverless car

Developing all these scenarios was not as easy as expected. However, with the help of the UML diagrams and the sketch of the driverless car (link is attached), I had a basis for development. During my development, I had to change the classes, methods and relationships to push my ideas forward. Designing the UML class diagram and other diagrams will be an outstanding achievement without changing the classes and methods in the development phase.

My biggest challenge was the development of the first scenario. It is an object-oriented program in which users can register an account and log in with the registered account name and password. After entering the correct information, the user can start the journey, update their profile, delete their account or log out of their account. All these functions are accessible without the code being interrupted through the `while true` loop. Because the methods are interdependent, the code has reached a higher level of complexity. Therefore, the code had to be executed and tested many times until the desired functions were achieved. The unit tests also had to be changed in the correct test order because of the dependencies.

The second scenario was developed using a state transition diagram. The user can search for his destination and calculate the route to start the navigation and, finally, the journey with the driverless car. Then, it can be connected to the registration programme as the user has to enter his destination to start the journey. Also, if the user wants to update their destination, the current destination will be deleted, and a new destination will be added. The last destination remains on the list if the journey is completed. Thanks to the UML state transition diagram, I could develop the scenario without difficulties. However, the particular task was to store the destination in a stack data structure (last in, first out). 

Dealing with a traffic light scenario was also easy to develop using the UML sequence diagram. The focus of this program was the interaction with the camera, database and control computer. Also, the particular task was calculating whether the car had to brake at the yellow traffic light or drive on. In the real scenario, the driverless car automatically supplies the class parameters. For the scenario development, however, I had to enter them manually. 

The last scenario was the detection of obstacles. For this scenario, I created an activity diagram focusing on saving and deleting data when the vehicle detects objects. Since all sensors are activated, the detection of the obstacles is different, but the same obstacle data will be stored in the database. Nevertheless, the more objects the car stores, the more complex the programme becomes. Hence I decided to create a scenario where the main task is executed.

## A Design Proposal of Software to Support Operation of a Driverless Car

Here you can find the design proposal with the UML diagrams for the development:

https://github.com/gicanon/driverless_car_assignment/blob/029d30cbb969dff4dc9d2c8f82e1bd7fa28f47e2/A%20Design%20Proposal%20of%20Software%20to%20Support%20Operation%20of%20a%20Driverless%20Car.pdf


## Getting Started

### Dependencies

This python project does not have any external libraries. However, starting this program will only require a Python 3 version.

### Installing

The latest version of python can be installed on the website: https://www.python.org/downloads/.

### Executing program

Executing this python project requires only running the file on the python platform. A welcome prompt will lead the user through this project until they quit the contact book by command. Then, the user needs to rerun the file to repeat the project.

## Help

Every function contains helper information. The command "help(function_name)" will display the function's information.

## Authors

Gianluca Cannone - https://github.com/gicanon

## License

Copyright (c) [2022] [Gianluca Cannone]

Permission is hereby granted, free of charge, to any person obtaining a copy of the project without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, and to permit persons to whom the project is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of this project.

THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROJECT OR THE USE OR OTHER DEALINGS IN THE PROJECT.