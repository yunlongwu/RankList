from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.
from client.models import Client
import json
from django.core import serializers


def create_client(request):
    """
    创建客户端（测试用）
    """
    client_id = request.GET.get("client_id")
    data = {
        "state": True,
        "message": "上传成功"
    }
    try:
        client_id = str(client_id)
    except:
        data = {
            "state": False,
            "message": "上传失败"
        }
        return HttpResponse(json.dumps(data))
    item = Client()
    item.client_id = client_id
    item.save()
    return HttpResponse(json.dumps(data))


def update_point(request):
    """
    上传客户端数据
    """
    client_id = request.GET.get("client_id")
    point = request.GET.get("point")
    data = {
        "state": True,
        "message": "上传成功"
    }
    if not client_id or not point:
        data = {
            "state": False,
            "message": "上传失败,上传信息不完整"
        }
        return HttpResponse(json.dumps(data))
    client_item = Client.objects.filter(client_id=client_id).first()
    if not client_item:
        data = {
            "state": False,
            "message": "上传失败,未获取到客户端信息"
        }
        return HttpResponse(json.dumps(data))
    try:
        point = int(point)
    except:
        data = {
            "state": False,
            "message": "上传失败,分数类型错误"
        }
        return HttpResponse(json.dumps(data))

    if not (point > 1 and point < 10000000):
        data = {
            "state": False,
            "message": "上传失败,分数范围错误"
        }
        return HttpResponse(json.dumps(data))
    client_item.points = point
    client_item.save()
    return HttpResponse(json.dumps(data))


def query_rank_list(request):
    """
    查询分数列表
    """
    client_id = request.GET.get("client_id")
    start_id = request.GET.get("start_id")
    end_id = request.GET.get("end_id")

    item = Client.objects.values("points", "client_id").filter(client_id=client_id).first()
    if not item:
        data = {
            "state": False,
            "message": "获取用户信息失败"
        }
        return HttpResponse(json.dumps(data))
    try:
        start_id = int(start_id)
        end_id = int(end_id)
    except:
        data = {
            "state": False,
            "message": "排名位置有误"
        }
        return HttpResponse(json.dumps(data))

    query = Client.objects.filter().all()
    this_seat = Client.objects.filter(points__gt=item["points"]).count()
    item["seat"] = this_seat + 1

    qs_json = serializers.serialize('json', query[start_id - 1:end_id])
    data = {
        "state": True,
        "message": "查询成功",
        "data": qs_json,
        "this_seat": item
    }
    return HttpResponse(json.dumps(data))
