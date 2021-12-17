from django.db.models import Q
from .models import *
from .forms import *

strip_words= ["an","a","on","in","from","for",'by',"not",'of','then',"to","with","the","that"]




def getprodFiltered(major, place, tag,request):
    # words=prepare_txt(search_text)
    internships=Internships.objects.all()
    result={}
    result["internships"]=[]
    internshipsfiltered=[]


    # for word in words:
    internshipsfiltered = internships.filter(Q(title__icontains =major) | Q(description__icontains=tag) | Q(location__icontains=place) )
    
    
    arrayfiltered=[]
    for intshipfilt in internshipsfiltered:
        objectint={
            "id":intshipfilt.id,
            "title":intshipfilt.title,
            "level":intshipfilt.level,
            "image":intshipfilt.image.url,
            "description":intshipfilt.description,
            "exist":False
        }
        arrayfiltered.append(objectint)
        if request.user.is_authenticated:
            if WishInternship.objects.filter(user=request.user,internship=intshipfilt):
                objectint["exist"]=True

   
    # result['internships']=internshipsfiltered
    result['internships']=arrayfiltered

   

    
    
   
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