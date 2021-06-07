from django.shortcuts import render
from .serializers import Get
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import tweepy

def find_tag(hash, tweetnumber, api):
    ans = []
    tweets = tweepy.Cursor(api.search, hash).items(tweetnumber)
    for tweet in tweets:
        ans.append(tweet.id)
    return ans

def post_comment(comment, id, api):
    try:
        api.update_status(status = comment, in_reply_to_status_id = id , auto_populate_reply_metadata=True)
        print("successfully commented on", id)
    except:
        print("Error in", id)

def total_res(hash, tweetnumber, comment, api):
    res = find_tag(hash, tweetnumber, api)
    for i in res:
        post_comment(comment, i, api)

def main(key, keys, acc, accs, has, number, comment):
    api_key = key
    api_secreat_key = keys
    access_token = acc
    access_token_secreat = accs

    auth = tweepy.OAuthHandler(api_key, api_secreat_key)
    auth.set_access_token(access_token, access_token_secreat)

    api = tweepy.API(auth)

    total_res(has, number, comment, api)
    


@csrf_exempt
def dataGet(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        jsondata = json.dumps({'msg':'done'})

        main(
            pythondata['api_key'], 
            pythondata['api_secreat_key'],
            pythondata['access_token'],
            pythondata['access_token_secreat'],
            pythondata['hashtag'],
            pythondata['numbers'],
            pythondata['comment']
        )


        return HttpResponse(jsondata, content_type = 'application/json')