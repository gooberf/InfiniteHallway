import functions.choices as choose
import floors.floor_one as f1
import functions.invHelper.invHelper as invHelper

bad_time_starter = choose.two_options("Want to have a bad time?", "yes", "no", "chose yes", "chose no")

if bad_time_starter == "yes":
    invHelper.invHelper()
else:
    pass

inventory = f1.floor_one()
