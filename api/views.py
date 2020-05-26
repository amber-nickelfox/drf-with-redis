import json
import redis
from django_redis_demo import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# connect to our Redis Instance
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
)


@api_view(['GET', 'POST'])
def manage_items(request, *args, **kwargs):
    """
    api view
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    if request.method == "GET":
        items = {}
        count = 0
        data = redis_instance.keys("*")[:-1]
        for key in data:
            print(key)
            items[key.decode("utf-8")] = redis_instance.get(key)
            count = count + 1
        response = {
            "count": count,
            "msg": "Found {} items".format(count),
            "items": items
        }
        return Response(response, status=status.HTTP_200_OK)

    elif request.method == "POST":
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        redis_instance.set(key, value)
        response = {
            "msg": "{} successfully set {}".format(key, value)
        }
        return Response(response, 201)


@api_view(['GET', 'PUT', 'DELETE'])
def manage_item(request, *args, **kwargs):
    if request.method == "GET":
        if kwargs['key']:
            value = redis_instance.get(kwargs['key'])
            if value:
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

    elif request.method == 'PUT':
        if kwargs['key']:
            request_data = json.loads(request.body)
            new_value = request_data['new_value']
            value = redis_instance.get(kwargs['key'])
            if value:
                redis_instance.set(kwargs['key'], new_value)
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': f"Successfully updated {kwargs['key']}"
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

    elif request.method == 'DELETE':
        if kwargs['key']:
            result = redis_instance.delete(kwargs['key'])
            if result == 1:
                response = {
                    'msg': f"{kwargs['key']} successfully deleted"
                }
                return Response(response, status=404)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)