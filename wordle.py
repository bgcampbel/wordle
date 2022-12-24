import json
from parse import *

# Specify the file path to the JSON data file
file_path = 'messages.json'

# Parse JSON file for games, players, and scores
with open(file_path, 'r') as json_file:

  scores = {}  # Results for every game
  total_scores = {}  # Number of games won per player

  try:
    # Convert contents of JSON file into dictionary
    data = json.load(json_file)

    # Examine each entry in data
    for msg in data['messages']:
      
      # Only consider messages with a text payload
      if not 'text' in msg:
        continue

      # Parse text for a Wordle score
      result = search('Wordle {:d} {:d}/', msg['text'])

      # Only consider Worlde scores
      if result is None:
        continue
      
      # Record stats
      game_num = result[0]
      score = result[1]
      email = msg['creator']['email']
      total_scores[email] = 0

      # Ensure entry for this game
      if not game_num in scores:
        scores[game_num] = {}
      
      # Record game results
      scores[game_num][email] = score

  except json.JSONDecodeError:
    print('json parsing error')

print(scores)

# Run through each game
for game_num in scores:
  game = scores[game_num]
  winning_score = 7

  # Find winning score
  for email in game:
    
    if game[email] < winning_score:
      winning_score = game[email]

  # Find winners for game
  for email in game:

    if game[email] == winning_score:
      # TODO Mark Winner
      total_scores[email] += 1

print(total_scores)