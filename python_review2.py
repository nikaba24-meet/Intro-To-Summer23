def create_youtube_video(title,discription):
	youtube_video = {"title": title,"discription": discription, "likes": 0, "dislikes": 0, "comments": {"username": ""}}
	return youtube_video
	
def likes(youtube_video):
	if likes in youtube_video:
		youtube_video["likes"] += 1
		print(youtube_video["likes"])
	return youtube_video

def dislikes(youtube_video):
	if dislikes in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtube_video,username,comment_text):
	youtube_video["comments"]["username"] = comment_text
	youtube_video["username"] = username
	return youtube_video

new_youtube_video = create_youtube_video("hi", "hello")
likes_for_video = likes(new_youtube_video)
dislikes_for_video = dislikes(new_youtube_video)
comments_of_video = add_comment(new_youtube_video,MissMuffin,hellllloooo)
print(comments_of_video)
print(likes_for_video)
print(dislikes_for_video)