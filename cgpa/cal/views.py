from django.shortcuts import render

# Create your views here.
def calcula(request):
 
    return render(request, 'cal/inpu.html',)

def add(request):
    namval = request.GET["name"]
    rollval = request.GET["roll"]
    regval = request.GET["reg"]
    passyval = request.GET["passyear"]
    sessval = request.GET["session"]
    deptval = request.GET["department"]
    insval = request.GET["institute"]


    val1 = float(request.GET["one"])
    val2 = float(request.GET["two"])  
    val3 = float(request.GET["three"])  
    val4 = float(request.GET["four"])
    val5 = float(request.GET["five"])  
    val6 = float(request.GET["six"]) 
    val7 = float(request.GET["seven"])  
    val8 = float(request.GET["eight"]) 

    f1=((val1/100)*(5))
    f2=((val2/100)*(5))
    f3=((val3/100)*(5))
    f4=((val4/100)*(10))
    f5=((val5/100)*(15))
    f6=((val6/100)*(20))
    f7=((val7/100)*(25))
    f8=((val8/100)*(15))
    res = round(f1+f2+f3+f4+f5+f6+f7+f8, 2)
    return render(request, 'cal/res.html', {'result': res, 'name': namval,
     'roll': rollval, 'reg': regval, 'pass': passyval, 'dept': deptval, 'ses': sessval, 'ins': insval,
     'val1':val1, 'val2':val2, 'val3':val3, 'val4':val4, 'val5':val5, 'val6':val6, 'val7':val7, 'val8':val8, })

