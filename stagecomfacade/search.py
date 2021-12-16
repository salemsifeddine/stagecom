from django.db.models import Q
from .models import *
from .forms import *

strip_words= ["an","a","on","in","from","for",'by',"not",'of','then',"to","with","the","that"]




def getprodFiltered(major, place, tag):
    # words=prepare_txt(search_text)
    internships=Internships.objects.all()
    result={}
    result["internships"]=[]
    internshipsfiltered=[]


    # for word in words:
    internshipsfiltered = internships.filter(Q(title__icontains =major) | Q(description__icontains=tag) | Q(location__icontains=place) )
    
    
    
    # try:
    #     slicenumber=int(val)
        
       
    #     seted=set(internshipsfiltered[:slicenumber])
    # except:

    # seted=set(internshipsfiltered)
   
    result['internships']=internshipsfiltered

    if len(result["internships"]) == len(set(internshipsfiltered)):
        result['all']="yes"
    else:
        result['all']="no"
    
    print(result)
    return result


def prepare_txt(search_text):
    words=search_text.split()
    
    for common in strip_words:
        if common in words:
            words.remove(common)
    return words[0:5]





# def suggestedProduct(request):
#     sugestedforUser=SearchItem.objects.all().filter(user=request.user)
#     products=Product.objects.all()
#     searchUser=[]
#     result={}
#     result["suggested"]=[]
#     productsfiltered=[]

#     for sgstd in sugestedforUser:
#         searchUser.append(sgstd)
    
   
    

#     for word in searchUser:
#         productsfiltered += products.filter(Q(name__icontains =word) | Q(description__icontains=word) | Q(sku__iexact=word) | Q(description__icontains=word) | Q(brand_name__icontains=word) | Q(meta_description__icontains=word) | Q(meta_keywords__icontains=word) )
    
#     seted=set(productsfiltered)

  
#     result['suggested']=seted

    
#     return result