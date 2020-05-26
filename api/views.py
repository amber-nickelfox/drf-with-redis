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
        for key in redis_instance.keys("*"):
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
            "msg": "{} successfully set {}"
        }
        return Response(response, 201)
