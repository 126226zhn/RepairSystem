from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *


# # 省数据
# def area(request):
#     provinces=Provinces.objects.all()
#     for province in provinces:
#         provinceid=province.provinceid
#         citys=Cities.objects.filter(provinceid=provinceid)
#         print(citys)
#         for city in citys:
#             cityid=city.cityid
#             areas=Areas.objects.filter(cityid=cityid)
#         return render(request, 'area.html',locals())


from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def index(request):
    return render(request,'area.html')

def pro(request):
    prolist=AreaInfo.objects.filter(parent__areainfo__isnull=True)
    print('***',prolist)
    list=[]
    for item in prolist:
        list.append([item.id,item.title])
    return JsonResponse({'data':list})

def city(request,id):
    citylist=AreaInfo.objects.filter(parent_id=id)
    print('###',citylist)
    list=[]
    for item in citylist:
       # [{}, {}, {}...]
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data':list})

def create(request):
    if request.method=="POST":
        pro=request.POST.get("province")
        city=request.POST.get('city')
        area=request.POST.get('area')
        print('===========',pro,city,area)
        address=pro+city+area
        print(address)
        return HttpResponse('iii')


#将 repairform excel表格导入
def excel_upload(request):
    if request.method == "GET":
        return render(request,'input.html')
    if request.method == "POST":
        f = request.FILES['my_file','']
        type_excel = f.name.split('.')[1]
        if type_excel in ['xlsx','xls']:
        # if 'xls' == type_excel:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read(),formatting_info=True)  # 关键点在于这里
            table = wb.sheets()[0]
            nrows = table.nrows  # 行数
            # ncole = table.ncols  # 列数
            try:
                with transaction.atomic(): #控制数据库事物交易
                    for i in range(1, nrows):
                        # if 4 == i:
                        #     i/0
                        rowValues = table.row_values(i)  # 一行的数据
                        user = models.UserModel.objects.get(international_code=rowValues[0])
                        models.RepairFormModel.objects.create(user=user, sale_price=rowValues[1],sale_min_count = rowValues[2])
            except Exception as e:
                return JsonResponse({'msg':'出现错误....'})
            return JsonResponse({'msg':'ok'})
        return JsonResponse({'msg':'上传文件格式不是xls'})
 
    return JsonResponse({'msg':'不是post请求'})