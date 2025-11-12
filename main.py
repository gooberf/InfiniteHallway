import functions.choices as choose
import floors.floor_one as f1

bad_time_starter = choose.two_options("Want to have a bad time?", "yes", "no", "chose yes", "chose no")

if bad_time_starter == "yes":
    pass

inventory = f1.floor_one()
