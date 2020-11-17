# visibility-service-getVisibilityIntervals

This is a simple implementation of the getVisibilityIntervals(ra, dec, start, end) function utilized in the visibility-service project https://github.com/emiliosalazardonate/visibility-service by Emilio Salazar to calculate Object Visibility in compliance with the Object Visibility Simple Access Protocol (ObjVisSAP).

This implementation should be valid for any ground-based facility. The tuneable parameters (latitude,longitude, object elevation limit, twillight limit) are easily recognized within the code.

Requirements: 
The PyEphem astronomy library https://rhodesmill.org/pyephem/

Usage:

Modify views.py from the visibility-service project: 

a) To import this function: from visibility.viscalc import VisCalc

b) Call the function within getVisibilityIntervals():

  def getVisibilityIntervals(ra, dec, start, end): 
  
     results = VisCalc(ra, dec, start, end)
     
     return results
      
viscalc.py should be placed in the same directory as views.py 
