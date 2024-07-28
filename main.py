from googleapiclient.discovery import build
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and video ID from environment variables
api_key = os.getenv('API_KEY')
video_id = os.getenv('VIDEO_ID')

youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id):
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()
    return response['items'][0]

def get_comments(video_id):
    comments = []

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        textFormat="plainText"
    )

    while request:
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comment_data = {
                'VideoID': video_id,
                'Channel': comment['authorDisplayName'],
                'NumOfCommentlikes': comment['likeCount'],
                'NumOfCommentDislikes': comment.get('dislikeCount', 0), # Dislikes are not available anymore
                'Comment': comment['textDisplay'],
                'CommentedUserID': comment['authorChannelUrl'],
                'Comment|repliedTime': comment['publishedAt'], 
            }

            if 'replies' in item:
                for reply in item['replies']['comments']:
                    reply_snippet = reply['snippet']
                    comment_data['NumOfReplies'] = len(item['replies']['comments'])
                    comment_data['RepliedUserID'] = reply_snippet['authorChannelUrl']
                    comment_data['Reply'] = reply_snippet['textDisplay']
                    comment_data['RepliesLikes'] = reply_snippet['likeCount']
                    comment_data['RepliesDislike'] = reply_snippet.get('dislikeCount', 0) # Dislikes are not available anymore
                    comment_data['ToWhomTheyReplied'] = comment['authorDisplayName']
                    comments.append(comment_data.copy())
            else:
                comment_data['NumOfReplies'] = 0
                comment_data['RepliedUserID'] = ''
                comment_data['Reply'] = ''
                comment_data['RepliesLikes'] = 0
                comment_data['RepliesDislike'] = 0
                comment_data['ToWhomTheyReplied'] = ''
                comments.append(comment_data.copy())

        request = youtube.commentThreads().list_next(request, response)

    return comments

video_details = get_video_details(video_id)
comments = get_comments(video_id)

# Get video upload time and date
video_upload_time = video_details['snippet']['publishedAt']

# Add video upload time to each comment
for comment in comments:
    comment['VideoUploadedtimeanddate'] = video_upload_time

filename = f"{video_id}.csv"
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['VideoID', 'Channel', 'NumOfCommentlikes', 'NumOfCommentDislikes', 'NumOfReplies', 'Comment', 'CommentedUserID', 'RepliedUserID', 'Reply', 'RepliesLikes', 'RepliesDislike', 'ToWhomTheyReplied', 'Comment|repliedTime', 'VideoUploadedtimeanddate'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for comment in comments:
        writer.writerow(comment)
