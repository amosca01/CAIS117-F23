## 
## Ab Mosca
## 10.25.2023
##
## Sample solution for Simple NLP
## Predicts who wrote a song based on
## lyrics input by the user
 
def get_lyrics(file_path):
  '''
  input: string
  output: list
  does: reads lines in input textfile into a list
        where each item is a word
  '''
  with open(file_path) as file:
    artist_lyrics = file.read().replace('\n',' ').split(" ")
    
  return artist_lyrics

def makeDict(lyrics):
  '''
  input: list
  output: word count dictionary
  does: takes song lyrics in input list
        and creates a word cound dictionary
  '''
  dict = {}
  
  for word in lyrics:
    # if word already seen, increase count
    if word in dict:
      dict[word] += 1
    else: # add to dictionary
      dict[word] = 1

  return dict

def predict(a1, d1, a2, d2, lyr):
  '''
  input: string, dictionary, string, dictionary, string
  output: string
  does: uses dictionaries to predict which artist 
        wrote lyric 
  '''
  lyr = lyr.split(" ")
  a1_count = 0 
  a2_count = 0

  # loop through words to get total count
  for word in lyr:
    if word in d1:
      a1_count += d1[word]
    if word in d2:
      a2_count += d2[word]

  # check higher count
  if a1_count > a2_count:
    return a1
  else:
    return a2

def main():

  # gather input
  artist1 = input("Artist 1: ")
  artist1_file = input("Artist 1 lyric file: ")

  artist2 = input("Artist 2: ")
  artist2_file = input("Artist 2 lyric file: ")
  
  artist1_lyrics = get_lyrics(artist1_file)
  artist2_lyrics = get_lyrics(artist2_file)

  # make dictionaries
  artist1_dict = makeDict(artist1_lyrics)
  artist2_dict = makeDict(artist2_lyrics)

  # get lyric to predict
  lyric = input("Input lyric (NO punctuation) to predict: ")
  lyric = lyric.lower()
  guess = predict(artist1, artist1_dict, 
                  artist2, artist2_dict, 
                  lyric)
  print(guess, "probably wrote that song!")

if __name__ == "__main__":
  main()