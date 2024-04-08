from django.shortcuts import render

# Create your views here.
def calculation(request):
    result=""
    if request.method=="POST":
        no1=int(request.POST.get('txtnum1'))
        no2=int(request.POST.get('txtnum2'))
        btn=request.POST.get('button')
        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        elif btn=="*":
            result=no1*no2
        elif btn=="/":
            result=no1/no2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:        
        return render(request,"Basics/Calculator.html",{'res':result})



#Largest & Smallest of numbers
def largest_smallest(request):
    result1=""
    result2=""
    if request.method=="POST":    
        no1=int(request.POST.get('no1'))
        no2=int(request.POST.get('no2'))
        no3=int(request.POST.get('no3'))
        btn=request.POST.get('btn')
        if btn=="Submit":
            if((no1>no2)&(no1>no3)):
                result1=no1
            elif(no2>no3):
                result1=no2
            else:
                result1=no3
            if((no1<no2)&(no1<no3)):
                result2=no1
            elif(no2<no3):
                result2=no2
            else:
                result2=no3   
            return render(request,"Basics/Largest_smallest.html",{'res1':result1,'res2':result2})
    else:
        return render(request,"Basics/Largest_smallest.html",{'res1':result1,'res2':result2})



#progm for finding total,percentage,mark
def mark(request):
    total=""
    percent=""
    grade=""
    if request.method=="POST":
        m1=int(request.POST.get('m1'))
        m2=int(request.POST.get('m2'))
        m3=int(request.POST.get('m3'))
        btn=request.POST.get('btn1')
        if btn=="submit":
            total=m1+m2+m3
            if total<=300:
                percent=(total/300)*100
            if percent >= 90:
                grade = 'A'
            elif 80 <= percent < 90:
                grade = 'B'
            elif 70 <= percent < 80:
                grade = 'C'
            elif 60 <= percent < 70:
                grade ='D'
            else:
                grade = 'F'
            return render(request,"Basics/Ranklist.html",{'res1':total,'res2':percent,'res3':grade})
    else:
        return render(request,"Basics/Ranklist.html",{'res1':total,'res2':percent,'res3':grade})  


# BasicsSalary
def Salary(request):
    # Initialize variables
    ta = ""
    da = ""
    hrc = ""
    lic = ""
    pf = ""
    deduction = ""
    net = ""
    fname = ""
    lname = ""
    gender = ""
    marriage = ""
    dpat = ""
    bs = ""

    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        marriage = request.POST.get('marriage')
        dpat = request.POST.get('dpat') 
        bs = int(request.POST.get('bs'))  
        btn = request.POST.get('submit')

        # Check if the submit button is clicked
        if btn == "submit":
            # Calculate salary components based on basic salary (bs)
            if bs >= 10000:
                ta = bs * 0.40
                da = bs * 0.35
                hrc = bs * 0.30
                lic = bs * 0.25
                pf = bs * 0.20
            elif bs >= 5000:  
                ta = bs * 0.35
                da = bs * 0.30
                hrc = bs * 0.25
                lic = bs * 0.20
                pf = bs * 0.15
            else:  
                ta = bs * 0.30
                da = bs * 0.25
                hrc = bs * 0.20
                lic = bs * 0.15
                pf = bs * 0.10

            # Calculate deduction and net salary
            deduction = lic + pf
            net = bs + ta + da + hrc - deduction

    # Render the template with data
    return render(request, "Basics/Salary.html", {
        'ta': ta, 'da': da, 'hrc': hrc, 'lic': lic, 'pf': pf,
        'deduction': deduction, 'net': net,
        'fname': fname, 'lname': lname, 'gender': gender,
        'marriage': marriage, 'dpat': dpat, 'bs': bs
    })



       