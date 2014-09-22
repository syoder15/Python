'''

@author: Sam

File setting up the dictionary with the cities and their respective teams
'''



global teamDict 

teamDict= {
'boston': {'NBA': ("Celtics",), 'MLB': ("Red Sox",), 'Abbrev': "bos"},
"buffalo": {'NFL': ("Bills",), 'Abbrev': "buf"},
'brooklyn' : {'NBA': ("Nets",), 'Abbrev': "bkn"},
"new york": {'NBA': ("Knicks", ), 'NFL': ('Jets', 'Giants'), 'MLB': ("Yankees", "Mets"), 'Abbrev': "ny"},
"new england": {'NFL': ("Patriots",), 'Abbrev': "ne"},
"baltimore" : {'NFL': ("Ravens",), 'MLB': ("Orioles",), 'Abbrev': "bal"},
"cincinatti": {'NFL': ("Bengals",), 'MLB':("Reds", ), 'Abbrev': "cin"},
"philadelphia" : {'NBA': ("76ers",), 'MLB':("Phillies",), 'NFL': ("Eagles", ), 'Abbrev': "phi"},
"toronto" : {'NBA': ("Raptors",), 'MLB':("Blue Jays",), 'Abbrev': "tor"},
"chicago": {'NBA': ("Bulls",), 'MLB':("White Sox", "Cubs"), 'NFL': ("Bears",), 'Abbrev': "chi"},
"cleveland": {'NBA': ("Cavaliers",), 'MLB':("Indians", ), 'NFL' : ("Browns", ), 'Abbrev': "cle"},
"detroit": {'NBA': ("Pistons",), 'MLB':("Tigers", ), 'NFL':("Lions",), 'Abbrev': "det"},
"indiana": {'NBA': ("Pacers",), 'Abbrev': "ind"},
"indianapolis": {'NFL': ("Colts",), 'Abbrev': "ind"},
"pittsburgh": {'NBA': ("Steelers",), 'MLB':("Pirates", ), 'Abbrev': "pit"},
"jacksonville": {'NFL': ("Jaguars",), 'Abbrev': "jax"},
"tennessee": {'NFL': ("Titans",), 'Abbrev': "ten"},
"milwaukee": {'NBA': ("Bucks",), 'MLB':("Brewers", ), 'Abbrev': "mil"},
"atlanta": {'NBA': ("Hawks",), 'MLB':("Braves",), 'NFL':("Falcons",), 'Abbrev': "atl"},
"charlotte": {'NBA': ("Hornets",), 'Abbrev': "cha"},
"miami": {'NBA':("Heat",), 'MLB':("Marlins",), 'NFL':("Dolphins",), 'Abbrev': "mia"},
"orlando": {'NBA': ("Magic",), 'Abbrev': "orl"},
"washington": {'NBA': ("Wizards",), 'MLB':("Nationals",), 'NFL': ("Redskins", ), 'Abbrev': "wsh"},
"kansas city": {'NFL': ("Chiefs",), 'MLB':("Royals", ), 'Abbrev': "kc"},
"dallas": {'NBA': ("Mavericks",), 'NFL': ("Cowboys",), 'Abbrev': "dal"},
"oakland": {'NFL': ("Raiders",), 'MLB':("Athletics",), 'Abbrev': "oak"},
"san diego": {'NFL': ("Chargers",), 'MLB':("Padres",), 'Abbrev': "sd"},
"green bay": {'NFL': ("Packers",), 'Abbrev': "gb"},
"st. louis": {'NFL': ("Rams",), 'MLB':("Cardinals",), 'Abbrev': "stl"},
"st louis": {'NFL': ("Rams",), 'MLB':("Cardinals", ), 'Abbrev': "stl"},
"san francisco": {'NFL': ("49ers",), 'MLB':("Giants",), 'Abbrev': "sf"},
"seattle": {'NFL': ("Seahawks",), 'MLB':("Mariners",), 'Abbrev': "sea"},
"carolina": {'NFL': ("Panthers",), 'Abbrev': "car"},
"arizona": {'NFL': ("Cardinals",), 'MLB':("Diamondbacks",), 'Abbrev': "ari"},
"texas": {'MLB':("Rangers",), 'Abbrev': "tex"},
"tampa bay": {'NFL': ("Buccaneers",), 'MLB': ("Rays",), 'Abbrev': "tb"},
"houston": {'NBA': ("Rockets",), 'MLB':("Astros", ), 'NFL': ("Texans",), 'Abbrev': "hou"},
"memphis": {'NBA': ("Grizzlies",), 'Abbrev': "mem"},
"new orleans": {'NBA': ("Pelicans",), 'NFL':("Saints",), 'Abbrev': "no"},
"san antonio": {'NBA': ("Spurs",), 'Abbrev': "sa"},
"colorado": {'MLB':("Rockies",), 'Abbrev': "col"},
"denver": {'NBA': ("Nuggets",), 'NFL': ("Broncos",), 'Abbrev': "den"},
"minnesota": {'NBA': ("Timberwolves",), 'MLB':("Twins", ), 'NFL':("Vikings",), 'Abbrev': "min"},
"portland": {'NBA': ("Trailblazers",), 'Abbrev': "por"},
"oklahoma city": {'NBA': ("Thunder",), 'Abbrev': "okc"},
"utah": {'NBA': ("Jazz",), 'Abbrev': "utah"},
"golden state": {'NBA':("Warriors",), 'Abbrev': "gs"},
"los angeles": {'NBA': ("Clippers", "Lakers",), 'MLB':("Angels", "Dodgers"), 'Abbrev': "la"},
"phoenix": {'NBA': ("Suns",), 'Abbrev': "phx"},
"sacramento": {'NBA': ("Kings",), 'Abbrev': "sac"}
}