
from django.conf.urls import url
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.csrf import csrf_exempt 
from . import views
import myapp.views
from myapp import views
#from django.views.generic import TemplateView
urlpatterns = [
 #       url(r'^path/to/url', TemplateView.as_view(template_name='index.html')),
        url(r'^hell',views.hello, name='hello'),
#       url(r'^otp/', views.hell, name='hell'),
        url(r'^test/(?P<store_id>\d+)/',views.test),
        #url(r'^send1/(?P<store_id>\d+)/',views.detaill),                      #GET api example with parameter
#       url(r'^pt/$',views.det),                                 #post api example
        url(r'^sendmessage.py/(?P<store_id>\d+)/(?P<message>.+)/',views.detaill),     #GET api example with  two parameter
        url(r'^sendi/(?P<store_id>\d+)/',views.detaill3),
        url(r'^user/', views.test, name='test'),
       # url(r'^expense/(?p<user_data>\d+)/',views.expenseparticipent),
        url(r'^api/(?P<mob_number>\d+)',views.API2),
        url(r'^fcmapi/(?P<tokenid>.+)',views.FCMAPI),
       # url(r'^fcmdata/(?P<tokenid>.+)',views.FCMAPI),
        url(r'^fcmid1/(?P<message_title>.+)/(?P<message_body>.+)/', views.FCMDATA1, name='FCMDATA1'),
        url(r'^fcmid/(?P<userNumber>.+)/(?P<orderID>.+)/(?P<merchantName>.+)/(?P<merchantNumber>.+)/(?P<userName>.+)/(?P<itemsList>.+)/(?P<netPrice>.+)/(?P<itemPrice>.+)/(?P<orderNo>.+)/(?P<status>.+)/(?P<available>.+)/(?P<amountItems>.+)/(?P<confreeStatus>.+)/(?P<ETA>.+)/(?P<category>.+)/(?P<date>.+)/(?P<merchantFcm>.+)/', views.FCMDATA, name='FCMDATA'),
        url(r'^fcmapi2/(?P<data>.+)/(?P<fcmid>.+)/(?P<order_id>.+)/',views.fcmapi2),
        
#        url(r'^postapi/(?P<id>\d+)/', views.save_data),

        url(r'^api_call', views.api_call, name='api_call'),
        url(r'^api3/(?P<object>.+)/(?P<id>.+)/',views.API3),
        url(r'^api4/(?P<id>.+)/(?P<object_id>.+)/',views.API4),
        url(r'^api5/(?P<user_no>.+)/(?P<user_no1>.+)/',views.API5),
        url(r'^api6/(?P<id>.+)/(?P<expense_version>.+)/(?P<object>.+)/',views.API6),
       # url(r'^api7/(?P<object>.+)/(?P<syncedstring>.+)/',views.API7),
        url(r'^api7/(?P<id>.+)/(?P<expense_version>.+)/(?P<object>.+)/(?P<syncedstring>.+)/',views.API7),
        url(r'^api8/(?P<murchant_number>.+)/',views.API8),
        url(r'^api9/(?P<user_name>.+)/',views.API9),
        url(r'^api10/(?P<user_name>.+)/(?P<referalcount>.+)/(?P<treferalcount>.+)/',views.API10),
        url(r'^api11/(?P<user_number>.+)/(?P<order_id>.+)/',views.API11),
        url(r'^waletapi', views.waletApi, name='waletApi'),
          
] 
