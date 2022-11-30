def slow_sort(arrival, departure):
    for i in range(len(arrival)):
        for j in range(len(arrival)):
            if arrival[i] <= arrival[j]:
                low_arriv = arrival[j]
                high_arriv = arrival[i]
                arrival[j] = high_arriv
                arrival[i] = low_arriv
                low_depart = departure[j]
                high_depart = departure[i]
                departure[j] = high_depart
                departure[i] = low_depart
    return (arrival, departure)


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    (arrival_sorted, departure_sorted) = slow_sort(arrival, departure)

    max_required = 0
    current_required = 0
    i = 0
    j = 1
    
    print(max_required)                
    return max_required

arrival = [900,  940, 950,  1100, 1500, 1800, 800]
departure = [910, 1200, 1120, 1130, 1900, 2000, 810]

print(slow_sort(arrival, departure))
