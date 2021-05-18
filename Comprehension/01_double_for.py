
def main():
    team_1 = {"Jane": 20, "John": 30}
    team_2 = {"Mary": 40, "Louis": 30}
    teams = (team_1, team_2)
    print(teams)

    combo = {name: score for team in teams for name, score in team.items()}

    combo_2 = {}
    for team in teams:
        for name, score in team.items():
            combo_2.update({name: score})

    print(combo)
    print(combo_2)


if __name__ == "__main__":
    main()
