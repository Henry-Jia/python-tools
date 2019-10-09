import requests
import re
import sys
import argparse
import json

def profile_data(username):
    data = requests.get("https://instagram.com/{}".format(username))
    if data.status_code == 404:
        print("Specified username not found")
        sys.exit()
    json_data   = json.loads(re.findall(r'window._sharedData\s=\s(\{.*\});</script>', data.text)[0])
    data        = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
    followers_count = data['edge_followed_by']['count']
    follows_count   = data['edge_follow']['count']
    profile_pic = data['profile_pic_url']
    insta_id    = data['id']
    bio         = data['biography']
    total_posts = data['edge_owner_to_timeline_media']['count']
    posts = []
    for i in range(min(12,total_posts)):
        posts.append(data['edge_owner_to_timeline_media']['edges'][i]['node']['display_url'])
    profile = { 
        'instagram_id' : insta_id,
        'followers' : followers_count, 
        'follows' : follows_count,
        'profile_pic' : profile_pic,
        'bio' : bio,
        'total_posts' : total_posts,
        'latest_posts' : posts
         }
    open("{}.json".format(username), "w").write(str(json.dumps(profile)))
    print("Data written to {}.json".format(username))

def post_data(post_id):
    data = requests.get("https://instagram.com/p/{}".format(post_id))
    if data.status_code == 404:
        print("Specified post not found")
        sys.exit()
    json_data       = json.loads(re.findall(r'window._sharedData\s=\s(\{.*\});</script>', data.text)[0])
    data            = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    likes_count     = data['edge_media_preview_like']['count']
    comments_count  = data['edge_media_to_parent_comment']['count']
    caption         = data['edge_media_to_caption']['edges'][0]['node']['text']
    media_url       = data['display_resources'][2]['src']
    is_video        = data['is_video']
    if is_video:
        media_url = data['video_url']
    comments = []
    for i in range(min(10, comments_count)):
        comments.append(data['edge_media_to_parent_comment']['edges'][i]['node']['text'])
    post = {
        'likes' : likes_count,
        'comments_count' : comments_count,
        'caption' : caption,
        'media' : media_url,
        'is_video' : is_video,
        'latest_comments' : comments
        }
    open("{}.json".format(post_id), "w").write(str(json.dumps(post)))
    print("Data written to {}.json".format(post_id))

def main():
    usage = '''
    Example:

    Fetch Profile Data:
        python3 igdata.py -p google

    Fetch Post Data:
        python3 igdata.py -d BzRIu3_lsev
    '''
    parser = argparse.ArgumentParser(description="Instagram Scraper", epilog=usage, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-p", help="Instagram public profile", type=str)
    parser.add_argument("-d", help="Instagram public post", type=str)
    args = parser.parse_args()

    profile = args.p
    post    = args.d

    if profile:
        profile_data(profile)
    elif post:
        post_data(post)

main()