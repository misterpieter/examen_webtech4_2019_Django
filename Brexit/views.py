from django.http import HttpResponse, HttpResponseRedirect
import datetime
# 29 March 2019 at 11 pm UK time.
# Create your views here.
def index(request):
    td = datetime.datetime(2019, 3, 29,23,0,0) - datetime.datetime.now()
    time = td.total_seconds()
    # hours = seconds // 3600
    # minutes = (seconds % 3600) // 60
    # seconds = seconds % 60

    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    return HttpResponse("REMAINING: {0} days - {1}h {2}m {3}s".format(day, hour,minutes,seconds))