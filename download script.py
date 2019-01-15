from pytube import YouTube
int startIndex = 0 
int endIndex = 0 

def when_complete:
	endIndex ++ 
	print("The end Index is " + endIndex )
	return 

def when_start :
	startIndex ++ 
	print("The start index is " + startIndex )
	return 

def download(link) : 
	yt = YouTube(link)
	yt.register_on_complete_callback(when_complete)
	yt.register_on_progress_callback(when_start)
	yt.streams.get_by_itag(18).download()
	return 


def parsingNotepad():
	file = open("links.txt" , "r")
	for line in file:
		download(line)


parsingNotepad()


