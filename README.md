# target-visibility

This is a simple implementation of the getVisibilityIntervals(ra, dec, start, end) function for utilized in the visibility-service project https://github.com/emiliosalazardonate/visibility-service by Emilio Salazar to calculate Object Visibility in compliance with the Object Visibility Simple Access Protocol (ObjVisSAP).

This implementation is only valid for ground-based facilities.

Requirements: 
The PyEphem astronomy library https://rhodesmill.org/pyephem/

Usage:

Modify views.py from the visibility-service project 

a) To import this function: from visibility.viscalc import VisCalc

b) Call the function within getVisibilityIntervals():

  def getVisibilityIntervals(ra, dec, start, end): 
  
     results = VisCalc(ra, dec, start, end)
     
     return results
      

