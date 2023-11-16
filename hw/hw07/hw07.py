## Follow the instructions in the pdf on the course website
## Remember to add a header, comments, and to test your
##  code with the autograder to help debug it 


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