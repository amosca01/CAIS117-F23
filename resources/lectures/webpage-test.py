import webbrowser
from time import sleep

def main():

    title = input("Song title: ")
    artist = input("Artist: ")
    url = input("YouTube video: ")
    duration = input("Video duration (MM:SS): ")

    print("Now playing", title, "by", artist)
    
    webbrowser.open(url)
    
    time = duration.split(":")
    total_seconds = int(time[0])*60+int(time[1])
    
    sleep(total_seconds)
    print("Song is over!")
       
main()
