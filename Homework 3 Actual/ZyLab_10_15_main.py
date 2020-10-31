# Saqib Siddiqui
# PSID: 1495537

class Team:
    def __init__(self,teamname = 'none',team_wins = 0,team_losses = 0):
        self.teamname = teamname
        self.team_wins = team_wins
        self.team_losses = team_losses

    def teamname2(self,teamname):
        self.teamname = teamname

    def team_wins2(self,team_wins):
        self.team_wins = team_wins

    def team_losses2(self,team_losses):
        self.team_losses = team_losses

    def get_win_percentage(self):
        final_percent = self.team_wins/(self.team_wins + self.team_losses)
        return final_percent

if __name__ == '__main__' :
    sports = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    sports.teamname2(team_name)
    sports.team_wins2(team_wins)
    sports.team_losses2(team_losses)

    getpercentage = sports.get_win_percentage()


    if getpercentage >= 0.5:
        print('Congratulations, Team',team_name,'has a winning average!')

    else:
        print('Team', team_name, 'has a losing average.')






