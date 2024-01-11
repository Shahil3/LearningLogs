from django.urls import path
from . import views

app_name = 'learnLogs'

urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    #Topic page
    path('topics/',views.topics,name='topics'),
    #details for single topic
    path('topics/<int:topic_id>/',views.topic,name = 'topic'),
    #page for adding new topic
    path('new_topic/',views.new_topic,name = 'new_topic'),
    #page for adding a new entry
    path('new_entry/<int:topic_id>/',views.new_entry,name = 'new_entry'),
    # page to save entry edits
    path('edit_entry/<int:entry_id>/',views.edit_entry,name = 'edit_entry'),
    #fun to del topic
    path('del_topic/<int:topic_id>/',views.del_topic,name = 'del_topic'),
    #fun to del entry
    path('del_entry/<int:entry_id>/',views.del_entry,name = 'del_entry'),
]
