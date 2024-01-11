from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    """The Home Page"""
    return render(request,'learnLogs/index.html')
@login_required
def topics(request):
    """Show all Topics"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learnLogs/topics.html',context)
@login_required
def topic(request,topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id = topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learnLogs/topic.html',context)
@login_required
def del_topic(request,topic_id):

    topic = Topic.objects.get(id = topic_id)
    if topic.owner != request.user:
        raise Http404
    topic.delete()
    return redirect('learnLogs:topics')
@login_required
def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        #No data is submitted
        form = TopicForm()
    else:
        #post the data;process
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learnLogs:topics')

    context = {'form':form}
    return render(request,'learnLogs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    """Add a entry for a particular topic"""
    topic = Topic.objects.get(id = topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #create a blank form
        form = EntryForm()

    else:
        # post data
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learnLogs:topic',topic_id=topic_id)
        
    context = {'topic':topic,'form':form}
    return render(request,'learnLogs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """edit existing entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)

    else:
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learnLogs:topic',topic_id = topic.id)

    context = {'entry':entry,'topic': topic,'form':form}
    return render(request,'learnLogs/edit_entry.html',context)
@login_required
def del_entry(request,entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    entry.delete()
    return redirect('learnLogs:topic',topic_id = topic.id)































    
