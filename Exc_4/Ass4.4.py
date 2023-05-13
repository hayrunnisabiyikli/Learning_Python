def create_world_series_dicts(filename):
    team_wins = {}
    year_winners = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

        for year, line in enumerate(lines, 1903):
            winner = line.strip()

            # Skip the years when World Series was not played
            if year == 1904 or year == 1994:
                continue

            # Update the team wins dictionary
            team_wins[winner] = team_wins.get(winner, 0) + 1

            # Update the year winners dictionary
            year_winners[year] = winner

    return team_wins, year_winners

def main():
    input_file = 'WorldSeriesWinners.txt'
    team_wins, year_winners = create_world_series_dicts(input_file)

    while True:
        year = int(input("Enter a year between 1903 and 2009 (or enter 0 to quit): "))

        if year == 0:
            break

        if year < 1903 or year > 2009:
            print("Invalid year. Please try again.")
            continue

        winner = year_winners.get(year)

        if winner is None:
            print("No World Series was played in that year.")
        else:
            wins = team_wins.get(winner)
            print(f"The {winner} won the World Series in {year} and has won it {wins} times in total.")

if __name__ == '__main__':

    main()
