# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)

report = f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute"
print(report)
player = "Hans van Breukelen"

first_name_look = player.find(" ")
print(first_name_look)
first_name = player[: first_name_look]
print(first_name)

last_name = player[first_name_look+1::]
print(last_name)
last_name_len = len(last_name)
print(last_name_len)
name_short = f"{player[0]}. {last_name}"
print(name_short)
pre_chant = (first_name + "! ") * len(first_name)
chant = pre_chant[:-1]
print(len(chant))
print(chant)
good_chant = chant[-1] != " "
print(good_chant)
