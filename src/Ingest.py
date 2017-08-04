activity =[
{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"}
]
print(activity)
# I pass dictionary dat to modify list activity

#Problem question as described
#Ingest(e, D)
#Given event e, update data D

#Solution
#I pass event key and modify data "activity" with data "dat" as below
#Example1
#Updated last_name to "Chandra" from "Smith" and adr_state to "CA" from "AK"
#dat = {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Chandra", "adr_city": "Middletown", "adr_state": "CA"}

#Example2
#Updated camera_make" updated from "Cannon" to "New Canon" and "camera_model" updated from "EOS 80D" to "EOS 80DD"
#
dat ={"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "New Canon", "camera_model": "EOS 80DD"}

def Ingest(e, D):
    for act in range(len(activity)):
        if (activity[act]["key"] ==e and activity[act]["type"] ==D["type"] and activity[act]["verb"] ==D["verb"]):
              activity[act] = D.copy()
    print(activity)
Ingest("d8ede43b1d9f",dat)
