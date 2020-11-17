# target-visibility

This is a simple implementation of the getVisibilityIntervals(ra, dec, start, end) function for utilized in the visibility-service project https://github.com/emiliosalazardonate/visibility-service by Emilio Salazar to calculate Object Visibility in compliance with the Object Visibility Simple Access Protocol (ObjVisSAP).

This implementation is only valid for ground-based facilities.

Requirements: 
The PyEphem astronomy library https://rhodesmill.org/pyephem/

Usage:

Modify views.py from the visibility-service project 
a) To import this function: from visibility.viscalc import VisCalc
b) Call the function within getVisibilityIntervals():
class VisibilityCalculator:
    @staticmethod
    def getVisibilityIntervals(ra, dec, start, end):
        # These are mock data.
        # This is telescope-related. The values are [t_start (in MJD), t_stop (in MJD), t_visibility (in seconds) ].
        # Each observatory should provide with this values.

        #results = [[58986.01767361111, 58987.993101851855, 170677],
        #           [58988.01767361111, 58989.993101851855, 170637],
        #           [58990.01767361111, 58997.993101851855, 170647],
        #           [58992.01767361111, 59997.993101851855, 170647]]

        results = VisCalc(ra, dec, start, end)

        return results

