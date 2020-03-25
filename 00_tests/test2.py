### DECLARATIONS
player_team = {}

for i in range(4):
    player_team[i] = []

### FUNCTIONS
def find_team(player_number, number_teams):
  team_number = player_number % number_teams
  return team_number

### CALLS
for i in range(1,101):
  team_number = find_team(i, 4)
  player_team[team_number].append(i)
 
print(player_team)

for i in range(4):
    print("Team {}: {}".format(i, player_team[i]))

    
