# CS61002: Algorithms and Programming 1 
# Name: Lokeshwar Reddy Kasarla
# Date: 06/08/2016
# Project01.py



##### Template for Project. ######

from urllib2 import urlopen
import json
import urllib
import stdio
import sys


class Tour(object):
    def __init__(self, *cities):
        #assigning the string array parameters to the list variables  
        self.cities = list(cities)
        
        #setting the distance traveled to nothing
        self.travel = None
        
        #setting the number of locations visited to nothing
        self.no_of_locations = None
        
        #getting length of cities list to find number of cities to visit
        if len(self.cities) > 1:
            #setting no of locations to visit and calling distance function
            self.no_of_locations = len(self.cities)
            self.travel = self.distance()
        else:
            #if no arguments or 1 argument is given, setting locations to one and distance to zero
            self.no_of_locations = 1
            self.travel = 0.0
    
    #driving distance function which accepts the optional mode
    def distance(self, mode="driving"):
        #if no of locations to visit is greater than one
        
        if(self.no_of_locations >1 ):
        #temporary variable to store the distance traveled from one city to other in cities
            temp_calc = 0.0
            #for each city in cities, repeating the loop
            for counter in range(len(self.cities)-1):
                # dictonary for storing the json parameters
                json_parameters = {}
                #setting the keys and values of json-parameters
                json_parameters['origins'] = self.cities[counter] 
                json_parameters['destinations'] = self.cities[counter+1]
                json_parameters['mode'] = mode
                json_parameters['sensor'] = False
                
                #setting google maps api url
                gApiUrl = "http://maps.googleapis.com/maps/api/distancematrix/json?"
                
                #appending the json parameters to google url and making final url
                
                resultUrl = gApiUrl +  urllib.urlencode(json_parameters)
                
                #getting the response from the url created
                web_response = urlopen(resultUrl)
                #converting the response to json 
                json_response = str(web_response.read())
                
                #closing the web connection
                web_response.close()
                
                #loading the json data to result dictonary
                result = json.loads(json_response)
                #getting the driving time from the obtained dictonary
                driving_time = result['rows'][0]['elements'][0]['distance']['value']
                
                #adding driving time of this trip to temporary driving time
                temp_calc = temp_calc+driving_time
            
            #assigning temporary driving time to total driving time
            driving_time = temp_calc
            
            #exception handling to check the time is no zero and no negative!
            try:
                if driving_time<0:
                    raise ValueError("Distance is not a number!")
                
            #raising the appropriate exception and handling it
            except Exception ,arg:
                driving_time =None
                stdio.writeln("Error in retrieving data from Google Maps API : "+str(arg))
                #ending the program if an exception is caught
                sys.exit(0)
                
        else:
            #if locations equal is less than or equal to one then set driving time to zero
            driving_time =0.0
        
        #returning the driving time
        return driving_time

    #add method to add an city at end of tour
    def __add__(self, viaLocation):
        if type(viaLocation) != Tour:
            raise TypeError("Supports only Tour type object!")
        #adding the item to tour and updating the tour
        updated_tour = tuple(self.cities+viaLocation.cities)
        #returning the new tour
        return Tour(*updated_tour)
    
    #function to give the visited cities by separating them with semi-collan
    def __str__(self):
        return '; '.join(self.cities)
    
    #returning the string of cities visited
    def __repr__(self):
        return str(self)

    #multiplying the tour
    def __mul__(self, repetition):
        #raising an exception if repetitions supplied is not an integer
        if type(repetition) != int:
            raise TypeError("Number of repetition must be a Integer Value")
        
        #raising an exception if repetitions supplied is less than zero
        if repetition < 0:
            raise ValueError("Expecting a Positive Integer only!")
        #else setting the tour to new tour with repetitions
        previous_Tour = Tour()
        while repetition:
            #adding old to repetitions tour 
            previous_Tour = previous_Tour + self
            repetition = repetition - 1
        
        #returning the new tour
        return previous_Tour

    #multiplying without checking any exceptions
    def __rmul__(self, repetition):
        return self * repetition

    #comparing the two tours to be greater or not
    def __gt__(self, anotherTour):
        if self.travel > anotherTour.travel:
            return True
        else:
            return False
    #comparing the two tours to be lesser or not
    def __lt__(self,anotherTour):
        if self.travel < anotherTour.travel:
            return True
        else:
            return False
    #comparing the two tours to be equal or not
    def __eq__(self, anotherTour):
        if self.cities == anotherTour.cities:
            return True
        else:
            return False

#main method to use Tour class
def    main():
    #Creating three tour objects with various number of objects
    obj_tour1    =    Tour("Houston,TX", "Cleveland, OH",    "New Jersy, NJ")
    obj_tour2    =    Tour("Kent,OH")
    obj_tour3    =    Tour("Chicago,MI",    "Miami, FL")
    #obtain the cities in tours
    print("Cities in various tours are as follows \n obj_tour1:    {}\nobj_tour2:{}\nobj_tour3:{}".format(obj_tour1,obj_tour2,obj_tour3))
    
    #distance method test
    print("t1    distances:    \ndriving-{}    km;    \nbiking-{}    km;    \nwalking-{}    km;\n".format(round(obj_tour1.distance()/1000.0),    round(obj_tour2.distance('bicycling')/1000.0),round(obj_tour1.distance('walking')/1000.0)))
    print("Using    driving    distances    from    here    on.")
    
    #add method test
    obj_tour4    =    obj_tour1    +    obj_tour2
    
    #__str__ method test
    print("The cities of obj_tour4: ",    obj_tour4.__str__())
    
    #__repr__ method test
    print("The cities of obj_tour3: ",    obj_tour3.__str__())
    
    #distance test
    print("The distance of obj_tour1 in walking mode: ",    obj_tour4.distance("walking"),"meters")
    print("The t4    driving    distance:",    round(obj_tour4.distance()/1000.0),"km")
    
    #__eq__ test for Tours equality
    print("obj_tour4    ==    obj_tour1    +    obj_tour2:",    obj_tour4    ==    obj_tour1    +    obj_tour2)
    
    #Tours comparision Greater than test
    print ("Is obj_tour1 > obj_tour2 ?: ", obj_tour1>obj_tour2)
    
    #tours comparision less than test
    print ("Is obj_tour1 < obj_tour2 ?: ", obj_tour1<obj_tour2)
    
    
    #multiplying the tours
    print("tour repetitions test obj_tour4:",obj_tour4.__mul__(3))
    
    #multiplying the tours
    print("tour repetitions test obj_tour3:",obj_tour3.__rmul__(2))
    
    
    
main()
stdio.writeln("End of Project, End of Summer Semester")
stdio.writeln("Thanks for your support all the time! - Lokeshwar Reddy Kasarla")