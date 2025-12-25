data = """Ronaldo,AlNassr,12,4
Messi,InterMiami,10,8
Suarez,InterMiami,8,5
Neymar,AlHilal,10,20
Bad,Data,Entry,Here
Benzema,AlIttihad,15,5
Modric,RealMadrid,2,10"""
with open('soccer_stats.txt', 'w') as f:
    f.write(data)

    
def process_league_stats(filename):
    process = {}
    mvp_list = []
    with open(filename, 'r') as f:
        
         
        for line in f:
            line = line.strip()
            parts = line.split(',')
            if len(parts) != 4:
                continue
            player_name, team_name, goals, assist = parts
            try:
                goals = int(goals)
                assist = int(assist)
            except ValueError:
                continue
            total_contribution = goals + assist

            if team_name not in process:
                process[team_name] = {'total_contribution': 0}
            process[team_name]['total_contribution'] += goals + assist
            if total_contribution > 15:
                mvp_list.append((player_name, total_contribution))
    return process, mvp_list
team_totals, mvp_list = process_league_stats('soccer_stats.txt')

# print(mvp_list)

def generate_season_summary(team_totals, mvp_list):
    
    with open("season_summary.txt", "w") as result:
        result.write('TEAM PERFORMANCE (Total Contributions)\n')
        result.write('-' * 38)
        for i in team_totals:
            result.write(f"\n{i}: {team_totals[i]['total_contribution']}")
        result.write("\n\nMVP CANDIDATES (> 15 contribs)\n")
        result.write('-' * 30)
        for name, total in mvp_list:
            result.write(f"\n{name}: ({total})")
    
generate_season_summary(team_totals, mvp_list)
with open("season_summary.txt", "r") as result:
    print(result.read())

