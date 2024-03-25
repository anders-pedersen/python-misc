# Import the datetime module
import datetime

#  Get the current date and return it in the format MM/DD/YYYY.
def get_current_date():
  log_currentdate = datetime.datetime.now().strftime("%m/%d/%Y")
  return log_currentdate

print(get_current_date())
