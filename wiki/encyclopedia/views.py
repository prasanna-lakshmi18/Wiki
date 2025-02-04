from django.shortcuts import render
from markdown import Markdown
# Create your views here.
from . import util
import random

def index(request):             
    # To display the home Page
    return render(request,'encyclopedia/index.html',{
        "entries":util.list_entries()
    })
def md_html(entry):
    # TO convert the markdown content in to htnl content
    markdowner=Markdown()
    #TO get the required entry if present
    content=util.get_entry(entry)
    if content is not None :
        #If the required entry in present in list of entries
        return markdowner.convert(content)
    else:
        #If the required entry is not present in the list of entries
        return None

def entry_page(request,title):
    #To display the contents of the requred entry
    entry_content=md_html(title)
    if entry_content == None:
        #ERROR if the required entry is not present in the list_entries
        return render(request,'encyclopedia/error.html',{
            'message':"This Page does not Exist :("
        })
    else:
        #Display the contents if the page is an element od the list_entries
        return render(request, 'encyclopedia/entry.html',{
            'title': title,
            'entry_content': entry_content
        })
def Search_bar(request):
    #To give the results and suggestions for the search query
    elements=util.list_entries()
    #To store the list_entries that has a query as sub-string
    results=[]
    if request.method == 'POST':
        #Loads the query
        search=request.POST['q']
        #Load the contents of the entry
        entry_content=md_html(search)
        if entry_content is not None:
            #Query and it's content
            return render(request,'encyclopedia/entry.html',{
                'title': search,
                'entry_content': entry_content
            })
        else:
            if entry_content == None:
                #If the query is not in list_entries  add the entries that has query as sub-string 
                for item in elements:
                    if search.lower() in item.lower():
                        results.append(item)
                if len(results):
                    #Display suggestions from the results
                    return render(request,'encyclopedia/search_bar.html',{
                        "entries":results
                    }) 
                else:
                    #If results is NONE, display Error Page
                    return render(request,'encyclopedia/error.html',{
                      'message':"This Page does not Exist :("
                    })


def new_page(request):
    #To create a new Page that are stored in list_entries
    if request.method == 'GET':
        #Enter the title and content of the new_page
        return render(request,'encyclopedia/new.html')
    else:
        #Load the title and contents of the new_page
        title=request.POST['title']
        content=request.POST['content']
        titleExist=util.get_entry(title)
        if titleExist is not None:
            # if the entry is already present,display error message
            return render(request,'encyclopedia/error.html',{
                'message': 'Page already existed'
            })
        else:
            #Save the new_entry if not present in list_entries
            util.save_entry(title,content)
            entry_content=md_html(title)
            return render(request, 'encyclopedia/entry.html',{
            'title': title,
            'entry_content': entry_content})


def edit_page(request):
    #Edit the entries
    title=request.POST['entry_title']
    content=util.get_entry(title)
    return render(request,'encyclopedia/edit.html',{
        'title': title,
        'content': content
    })

def  save_edit(request):
    #Save the edits of the entry
    edit=request.POST['entry_title']
    content=request.POST['content']
    util.save_entry(edit,content)
    return render(request,'encyclopedia/entry.html',{
                'title': edit,
                'entry_content': md_html(edit)
            })

def random_page(request):
    #To display the random pages that are elements of list_entries
    elements=util.list_entries()
    title=random.choice(elements)
    content=md_html(title)
    return render(request,'encyclopedia/random.html',{
        'title': title,
        'content':content
    })