def is_it_summer_yet(threshold_temp,today,yesterday,the_day_before_yesterday): #this func. takes 4 parameters.

    threshold_temp = float(threshold_temp)      # this part converts the parameters of the func. into floats
    today = float(today)
    yesterday = float(yesterday)
    the_day_before_yesterday = float(the_day_before_yesterday)

    def check_at_least_2_out_of_3():  # this function checks if at least 2 out of 3 days are above.
                                      # it returns True if correct and False if incorrect.
        if (threshold_temp < today) and (threshold_temp < yesterday or threshold_temp < the_day_before_yesterday):
            return True
        elif (threshold_temp < yesterday) and (threshold_temp < today or threshold_temp < the_day_before_yesterday):
            return True
        elif (threshold_temp < the_day_before_yesterday) and (threshold_temp < yesterday or threshold_temp < today):
            return True
        else:
            return False
    check_at_least_2_out_of_3() # executes the checking function
