from django.contrib import admin
from django.db import models

# Register your models here.
#from .models import Merchantofferings
#from .models import Notifications
#from .models import Referral
#from .models import Waste
from .models import Runningexpenses
#from .models import Getpaidback
from .models import Expensedetails
from .models import Expenseparticipants
from .models import Updatelist

from .models import Fcm


#from .models import Groups
#from .models import Pw2W                       Updatelist
#from .models import Userorder
#from .models import Dynamicvalue
#from .models import Deviceid
#from .models import Contree
#from .models import Pbanktransfer
from .models import User
from .models import Userfinal


admin.site.register(Updatelist)

admin.site.register(Expenseparticipants)
#admin.site.register(st2)
#admin.site.register(Notifications)
#admin.site.register(Merchantofferings)
#admin.site.register(Referral)
#admin.site.register(Waste)
admin.site.register(Runningexpenses)
#admin.site.register(Getpaidback)
admin.site.register(Expensedetails)
#admin.site.register(Groups)
#admin.site.register(Pw2W)
#admin.site.register(Userorder)
#admin.site.register(Dynamicvalue)
#admin.site.register(Deviceid)
#admin.site.register(Contree)
#admin.site.register(Pbanktransfer)
admin.site.register(User)
admin.site.register(Userfinal)
admin.site.register(Fcm)




