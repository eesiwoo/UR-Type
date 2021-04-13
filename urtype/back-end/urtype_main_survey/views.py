from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from urtype_main_survey.models import Globals
from urtype_main_survey.models import Middle
from urtype_main_survey.models import National
from urtype_main_survey.models import Soho
from urtype_main_survey.models import Userinfo



def Index(request):
    datas = Globals.objects.all()
    return render(request, 'index.html')


def WhoAreYou(request):
    datas = Globals.objects.all()
    return render(request, 'whoAreYou.html')


def UserInfo(request):
    print('work')
    if request.method == 'POST' :
        Userinfo(
            user_age = request.POST.get('user_Age'),
            user_job = request.POST.get('user_Job')
            ).save()
        user_age = request.POST.get('user_Age')
        user_job = request.POST.get('user_Job')
        print('user_Age :',user_age)
        print('user_Job :',user_job)
    return render(request, 'survey.html')
  
            
def Result(request):
    if request.method == 'POST' :
        brand_Size = request.POST.get('brand_Size')
        brand_Genre = request.POST.get('brand_Genre')
        design_Point = request.POST.get('design_Point')
        design_Color = request.POST.get('design_Color')
        avg_Price = request.POST.get('avg_Price')
        
        # 브랜드 규모에 따라 테이블에서 값 불러오기
        if brand_Size == 'Globals' :
            datas, name = ReadGlobals(brand_Genre,design_Point, design_Color, avg_Price)
        if brand_Size == 'National' :
            datas, name = ReadNational(brand_Genre, design_Point, design_Color, avg_Price)
        if brand_Size == 'Middle' :
            datas, name = ReadMiddle(brand_Genre,design_Point, design_Color, avg_Price)
        if brand_Size == 'Soho' :
            datas, name = ReadSoho(brand_Genre, design_Point, design_Color, avg_Price)
        
        length = datas.count()   
        # 유저 정보 업데이트 (포스트로 넘어올 때만 업데이트)
        UserInfoUpdate(name)
        # 카카오톡 공유하기를 위한 데이터
        kakao_data = {'Size':brand_Size, 'Genre':brand_Genre, 'Point':design_Point, 'Color':design_Color, 'Price':avg_Price}
        
            
    return render(request, 'result.html',{'datas':datas, 'length':length, 'kakao_data':kakao_data})

def ShareResult(request):
    if request.method == 'GET' :
        brand_Size = request.GET.get('Size')
        brand_Genre = request.GET.get('Genre')
        design_Point = request.GET.get('Point')
        design_Color = request.GET.get('Color')
        avg_Price = request.GET.get('Price')
        
        # 브랜드 규모에 따라 테이블에서 값 불러오기
        if brand_Size == 'Globals' :
            datas, name = ReadGlobals(brand_Genre,design_Point, design_Color, avg_Price)
        if brand_Size == 'National' :
            datas, name = ReadNational(brand_Genre, design_Point, design_Color, avg_Price)
        if brand_Size == 'Middle' :
            datas, name = ReadMiddle(brand_Genre,design_Point, design_Color, avg_Price)
        if brand_Size == 'Soho' :
            datas, name = ReadSoho(brand_Genre, design_Point, design_Color, avg_Price)
        
        length = datas.count()
        # 카카오톡 공유하기를 위한 데이터
        kakao_data = {'Size':brand_Size, 'Genre':brand_Genre, 'Point':design_Point, 'Color':design_Color, 'Price':avg_Price}  
    
    return render(request, 'result.html',{'datas':datas, 'length':length, 'kakao_data':kakao_data})


def Feedback_form(request):
    return render(request, 'feedback.html')


def Send_Email(request):
    if request.method == 'POST' :
        title = request.POST.get('title')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(title, message, to=[email_from])
        email.send()
    return render(request, 'thanks.html')

# ORM 실행문

def ReadGlobals(genre, point, color, price):
    datas = Globals.objects.filter(
        brand_Genre = genre,
        design_Point = point,
        design_Color = color,
        avg_Price = price
        )
    name = datas.values_list('brand_Name',flat=True)
    name = list(name)
    
    return datas, name

def ReadMiddle(genre, point, color, price):
    datas = Middle.objects.filter(
        brand_Genre = genre,
        design_Point = point,
        design_Color = color,
        avg_Price = price
        )
    name = datas.values_list('brand_Name',flat=True)
    name = list(name)
    
    return datas, name

def ReadNational(genre, point, color, price):
    datas = National.objects.filter(
        brand_Genre = genre,
        design_Point = point,
        design_Color = color,
        avg_Price = price
        )
    name = datas.values_list('brand_Name',flat=True)
    name = list(name)
    
    return datas, name

def ReadSoho(genre, point, color, price):
    datas = Soho.objects.filter(
        brand_Genre = genre,
        design_Point = point,
        design_Color = color,
        avg_Price = price
        )
    name = datas.values_list('brand_Name',flat=True)
    name = str(name)
    
    return datas, name

def UserInfoUpdate(name):
    user_info = Userinfo.objects.last()
    user_info.brand_name = name
    user_info.save()
     
    