def VisCalc(ra, dec, start, end):

  import ephem

  DEBUG = False

  # PyEphem dates are encoded as the “Dublin Julian Day”, so we need to convert input dates which are given as MJD
  # Modified JD 0h November 17, 1858    JD − 2400000.5
  # Dublin JD   12h December 31, 1899   JD − 2415020 
  # MJD = DJD + 15019.5
  # start and end times are not exact here. A very conservative approach has been taken to ensure the whole
  # input period is covered. Can be improved
  date_start = ephem.Date(int(start) - 15019 - 3)
  date_end = ephem.Date(int(end) - 15019)
  date = date_start

  # Observatory location, latitude & longitude 
  observer = ephem.Observer()
  observer.lon = '-17:52:59.7'
  observer.lat = '28:45:26.2'

  # Define a PyEphem fixed object from the input coordinates
  # The exact object properties are not important here, only ra and dec
  obj = "star,f|M|F7,%s,%s,2000" % (float(ra)/15,dec)
  star = ephem.readdb(obj)

  # Define the list to contain all visibility intervals
  vis_list =[]

  # Loop over every day in the defined period
  while date < date_end:

    # We start incrementing the date for simplicity; The loop iteration can be skipped in several places
    # and would otherwise require an explicit date increment.
    date = ephem.date(date + 1)

    if DEBUG: print("Date: %s" % date)

    # Set the date at the observatory location
    observer.date = date

    # Calculate nautical twilligts. If the night should be defined as between astronomical twillights
    # set horizon to -18 (For sunset and sunrise, use horizon = 0)
    observer.horizon = '-12'
    start_night = observer.next_setting(ephem.Sun())
    observer.date = start_night
    end_night = observer.next_rising(ephem.Sun()) 
    observer.date = date

    # Calculate object visibility at the observatory location. 
    # TRICK: To define an airmass limit, change the observatory horizon.
    # Here we set the horizon to 30 degrees, which implies that the object visibility is limited to airmass = 2
    # If the object never rises above 30 degrees, skip to next day
    observer.horizon = '30'
    try:
      observer.date = end_night
      start_obj = observer.previous_rising(star)
    except ephem.NeverUpError:
      continue
    observer.date = start_obj
    end_obj = observer.next_setting(star)

    if DEBUG: print("Start Night: %s" % start_night)
    if DEBUG: print("End Night  : %s" % end_night)
    if DEBUG: print("Start Obj  : %s" % start_obj)
    if DEBUG: print("End Obj    : %s" % end_obj)

    # Here comes the tricky part. These two conditional statements determines (or should determine)
    # the visibility interval of the object given the limitations imposed from object rise/set time 
    # and sun set/rise times (respecting airmass limit and nautical twilligt).
    if (start_obj < start_night):
      start_obs = start_night
    elif (start_obj > start_night) and (start_obj < end_night):
      start_obs = start_obj
    else:
      continue

    if end_obj > end_night:
      end_obs = end_night
    elif end_obj < start_night:
      continue
    else:
      end_obs = end_obj

    # If we got so far, the object is visible in a certain period on this day. We add start time (MJD), end time (MJD) 
    # and corresponding interval (seconds) to the list to be returned from this function call.
    vis_list.append([start_obs+15019.5,end_obs+15019.5,int((end_obs-start_obs)*86400)])

    if DEBUG: print("Start Obs  : %s" % start_obs)
    if DEBUG: print("End Obs    : %s" % end_obs)

  return vis_list
