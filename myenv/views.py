from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json 

from .models import SummaryData,SchoolData
# from .seriallizers import SchoolDataSerializer
# Create your views here.

def index (request):
    if 'term' in request.GET:
        qs = SchoolData.objects.filter(school_name__istartswith=request.GET.get('term')).only("school_name")
        school_name = []
        for s in qs:
            school_name.append(s.school_name)
        return JsonResponse(school_name,safe=False)
    if 'searchSchoolName' in request.GET:
        school_data = SchoolData.objects.filter(school_name__iexact=request.GET['searchSchoolName']).only('summary_school_id__total_student')

        if len(school_data) == 0 :
            message = "requested school was not found in database"
            return  JsonResponse({'status':'false','message':message}, status=500)
        if len(school_data) > 1:
            message = "Found more than one school, Check database"
            return  JsonResponse({'status':'false','message':message}, status=500)
        
        school_data = school_data.first()
        summary_data = school_data.summary_school_id.all().first()
        schoolJson_list = []
        point = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [school_data.lng, school_data.lat]
            },
            "properties": {
                "schoolID": school_data.school_id,
                "name": school_data.school_name,
                "size": summary_data.size,
                "lowest_level" :  summary_data.lowest_level,
                "highest_level" : summary_data.highest_level,
                "total_student" : summary_data.total_student
            }
        }
        schoolJson_list.append(point)
        resp ={
            'count' : "None", # จะเป็น None เสมอ ถ้าผู้ใช้งานกด search ชื่อโรงเรียน
            'schoolJson_list' : schoolJson_list
        }
        return JsonResponse(resp, safe = False)
    return render(request, 'index.html')

def getProvinceFromDB(request):
    req = request.GET['sector']
    fSchoolData = SchoolData.objects.filter(sector__exact=req).values_list('province',flat=True).distinct()
    provinces_dict = dict(zip(fSchoolData,fSchoolData))
    return JsonResponse(provinces_dict)

def filterPoi(request):
    req_sector = request.GET['sector']
    req_province = request.GET['province']
    req_size = request.GET['size']
    req_startSlice = int(request.GET['startPageItem'])
    req_pageLenght = int(request.GET['pageLenght'])
    req_count = request.GET['req_count'].lower()  # true or false
    #-------------Check query condition-----------------------
    q_list =[]
    if req_sector != 'ทุกภาค':
        q_sector = Q(school__sector = req_sector)
        q_list.append(q_sector)
        
    if req_size !='ทุกขนาด':
        q_size = Q(size = req_size)
        q_list.append(q_size) 

    if req_province != 'ทุกจังหวัด':
        q_province = Q(school__province = req_province)
        q_list.append(q_province)
    
    if len(q_list) == 0:
         q_req = Q(school__isnull = False)
    else:
        q_req = Q()
        for q in q_list:
            q_req = q_req & q
    #-------------End query condition-----------------------
    # Query to DB
    if(req_count == 'true'):
        count_fSchoolData = SummaryData.objects.select_related('school').filter(q_req).order_by('-total_student').only('size','school')
        count = count_fSchoolData.count()
    else:
        count = "None" 

    fSchoolData = SummaryData.objects.select_related('school').filter(q_req).order_by('-total_student').only('size','school')[req_startSlice:req_startSlice+req_pageLenght]
    #-----------------Make GeoJson list--------------------------
    schoolJson_list = []
    for s in fSchoolData:       
        point = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [s.school.lng, s.school.lat]
            },
            "properties": {
                "schoolID": s.school.school_id,
                "name": s.school.school_name,
                "size": s.size,
                "lowest_level" :  s.lowest_level,
                "highest_level" : s.highest_level,
                "total_student" : s.total_student
            }
        }
        schoolJson_list.append(point)
    #-----------------End GeoJson list--------------------------
    resp ={
        'count' : count,
        'schoolJson_list' : schoolJson_list
    }
    return JsonResponse(resp, safe = False)

def detailPage(request):
    if 'school_id' not in request.GET:
        return render(request, 'detailPage.html')
    
    focus_schoolID = request.GET['school_id'].split(",")
    if len(focus_schoolID[0]) != 10:  #เช็คว่าข้อมูลที่ส่งมาเป็นรหัสโรงเรียน 10 หลักหรือไม่
        print("something wrong")
        return render(request, 'detailPage.html')
    
    SchoolData = SummaryData.objects.select_related('school').order_by('-total_student').filter(school_id__in=focus_schoolID)
    # SchoolData = SummaryData.objects.select_related('school').order_by('-total_student')[100:200]
    schoolJson_list = []
    data_keys = []
    for s in SchoolData:
        school = {
            "id" : s.school.school_id,
            "name" : s.school.school_name,
            "size" : s.size,
            "lowest_level" : s.lowest_level,
            "highest_level" : s.highest_level,
            "total_k_field" : s.total_k_field,
            "total_p_field" : s.total_p_field,
            "total_s_lower" : s.total_s_lower,
            "total_s_upper" : s.total_s_upper,
            "total_cert_field" : s.total_cert_field,
            "total_student" : s.total_student
        }
        schoolJson_list.append(school)
    for k in schoolJson_list[0].keys():
        data_keys.append(k)
    return render(request, 'detailPage.html',{'schoolJson_list':schoolJson_list, "data_keys":data_keys})