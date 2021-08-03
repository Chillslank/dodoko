import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dodoko.settings')

import django
django.setup()
from game.models import Category, Page


def populate():
    ACT_pages = [
        {'title': 'Grand Theft Auto V', 'url':'https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/', 'views':128, 'likes':0, 'describe':"When a young street hustler, a retired bank robber and a terrifying psychopath find themselves entangled with some of the most frightening and deranged elements of the criminal underworld, the U.S. government and the entertainment industry, they must pull off a series of dangerous heists to survive in a ruthless city in which they can trust nobody, least of all each other."},
        {'title': 'CounterStrike Global Offensive', 'url':'https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/', 'views':195, 'likes':0, 'describe':"'Counter-Strike took the gaming industry by surprise when the unlikely MOD became the most played online PC action game in the world almost immediately after its release in August 1999,' said Doug Lombardi at Valve. 'For the past 12 years, it has continued to be one of the most-played games in the world, headline competitive gaming tournaments and selling over 25 million units worldwide across the franchise. CS: GO promises to expand on CS' award-winning gameplay and deliver it to gamers on the PC as well as the next gen consoles and the Mac.'"},
        {'title': 'Apex Legends', 'url':'https://store.steampowered.com/app/1172470/Apex_Legends/', 'views':199, 'likes':0, 'describe':"Apex Legends is the award-winning, free-to-play Hero shooter from Respawn Entertainment. Master an ever-growing roster of legendary characters with powerful abilities and experience strategic squad play and innovative gameplay in the next evolution of Hero Shooter and Battle Royale."},
        {'title': 'PUBG BATTLEGROUNDS', 'url':'https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/', 'views':23, 'likes':12, 'describe':'PUBG: BATTLEGROUNDS is a battle royale shooter that pits 100 players against each other in a struggle for survival. Gather supplies and outwit your opponents to become the last person standing.'},
        {'title': 'Warframe', 'url':'https://store.steampowered.com/app/230410/Warframe/', 'views':1234, 'likes':2342, 'describe':'Warframe is a cooperative free-to-play third person online action game set in an evolving sci-fi world.'},
        {'title': 'Dead by Daylight', 'url':'https://store.steampowered.com/app/381210/Dead_by_Daylight/', 'views':321, 'likes':232, 'describe':'Dead by Daylight is a multiplayer (4vs1) horror game where one player takes on the role of the savage Killer, and the other four players play as Survivors, trying to escape the Killer and avoid being caught and killed.'},
        {'title': 'Destiny 2', 'url':'https://store.steampowered.com/app/1085660/Destiny_2/', 'views':635, 'likes':214, 'describe':'Destiny 2 is an action MMO with a single evolving world that you and your friends can join anytime, anywhere, absolutely free.'},
    ]

    ARPG_pages = [
        {'title': 'The Ascent', 'url':'https://store.steampowered.com/app/979690/The_Ascent/', 'views':200, 'likes':320, 'describe':"The Ascent is a solo and co-op Action-shooter RPG set in a cyberpunk world. The mega corporation that owns you and everyone, The Ascent Group, has just collapsed. Can you survive without it?"}, 
        {'title': 'The Outer Worlds', 'url':'https://store.steampowered.com/app/578650/The_Outer_Worlds/', 'views':128, 'likes':0, 'describe':"https://store.steampowered.com/app/578650/The_Outer_Worlds/"},
        {'title': 'Mass Effect Legendary Edition', 'url':'https://store.steampowered.com/app/1328670/Mass_Effect_Legendary_Edition/', 'views':198, 'likes':0, 'describe':"The Mass Effect™ Legendary Edition includes single-player base content and over 40 DLC from the highly acclaimed Mass Effect, Mass Effect 2, and Mass Effect 3 games, including promo weapons, armors, and packs — remastered and optimized for 4K Ultra HD."},
        {'title': 'Path of Exile', 'url':'https://store.steampowered.com/app/238960/Path_of_Exile/', 'views':89, 'likes':32, 'describe':'You are an Exile, struggling to survive on the dark continent of Wraeclast, as you fight to earn power that will allow you to exact your revenge against those who wronged you. Created by hardcore gamers, Path of Exile is an online Action RPG set in a dark fantasy world.'},
        {'title': 'Lost Ark', 'url':'https://store.steampowered.com/app/1599340/Lost_Ark/', 'views':735, 'likes':345, 'describe':'Embark on an odyssey for the Lost Ark in a vast, vibrant world: explore new lands, seek out lost treasures, and test yourself in thrilling action combat in this action-packed free-to-play RPG.'},
        {'title': "Deaths Door", 'url':'https://store.steampowered.com/app/894020/Deaths_Door/', 'views':62, 'likes':43, 'describe':"Reaping souls of the dead and punching a clock might get monotonous but it's honest work for a Crow. The job gets lively when your assigned soul is stolen and you must track down a desperate thief to a realm untouched by death - where creatures grow far past their expiry."},
        {'title': 'Swords of Legends Online', 'url':'https://store.steampowered.com/app/1418100/Swords_of_Legends_Online/', 'views':623, 'likes':623, 'describe':'Swords of Legends Online is an action MMORPG set in a breathtaking fantasy world with sophisticated combat mechanics and a unique storyline based on Chinese mythology.'},
        {'title': 'Monster Hunter: World', 'url':'https://store.steampowered.com/app/582010/Monster_Hunter_World/', 'views':722, 'likes':734, 'describe':'Welcome to a new world! In Monster Hunter: World, the latest installment in the series, you can enjoy the ultimate hunting experience, using everything at your disposal to hunt monsters in a new world teeming with surprises and excitement.'},
    ]

    AVG_pages = [
        {'title': 'Valheim', 'url':'https://store.steampowered.com/app/892970/Valheim/', 'views':128, 'likes':0, 'describe':"A brutal exploration and survival game for 1-10 players, set in a procedurally-generated purgatory inspired by viking culture. Battle, build, and conquer your way to a saga worthy of Odin’s patronage!"},
        {'title': "Dont Starve Together", 'url':'https://store.steampowered.com/app/322330/Dont_Starve_Together/', 'views':197, 'likes':0, 'describe':"Fight, Farm, Build and Explore Together in the standalone multiplayer expansion to the uncompromising wilderness survival game, Don't Starve."} ,
        {'title': 'The Elder Scrolls V: Skyrim Special Edition', 'url':'https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/', 'views':745, 'likes':64, 'describe':'Winner of more than 200 Game of the Year Awards, Skyrim Special Edition brings the epic fantasy to life in stunning detail. The Special Edition includes the critically acclaimed game and add-ons with all-new features like remastered art and effects, volumetric god rays, dynamic depth of field, screen-space'},
        {'title': 'Sea of Thieves', 'url':'https://store.steampowered.com/app/1172620/Sea_of_Thieves/', 'views':4256, 'likes':742, 'describe':'Sea of Thieves offers the essential pirate experience, from sailing and fighting to exploring and looting – everything you need to live the pirate life and become a legend in your own right. With no set roles, you have complete freedom to approach the world, and other players, however you choose.'},
        {'title': 'Terraria', 'url':'https://store.steampowered.com/app/105600/Terraria/', 'views':456, 'likes':456, 'describe':'Dig, fight, explore, build! Nothing is impossible in this action-packed adventure game. Four Pack also available!'},
        {'title': 'Red Dead Redemption 2', 'url':'https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/', 'views':451, 'likes':713, 'describe':'Winner of over 175 Game of the Year Awards and recipient of over 250 perfect scores, RDR2 is the epic tale of outlaw Arthur Morgan and the infamous Van der Linde gang, on the run across America at the dawn of the modern age. Also includes access to the shared living world of Red Dead Online.'},
        {'title': 'FINAL FANTASY XIV Online', 'url':'https://store.steampowered.com/app/39210/FINAL_FANTASY_XIV_Online/', 'views':4617, 'likes':546, 'describe':'Take part in an epic and ever-changing FINAL FANTASY as you adventure and explore with friends from around the world.'},
    ]

    RTS_pages = [
        {'title': 'Dota 2', 'url':'https://store.steampowered.com/app/570/Dota_2/', 'views':4121, 'likes':4235, 'describe':"Every day, millions of players worldwide enter battle as one of over a hundred Dota heroes. And no matter if it's their 10th hour of play or 1,000th, there's always something new to discover. With regular updates that ensure a constant evolution of gameplay, features, and heroes, Dota 2 has taken on a life of its own."},
        {'title': "WARHAMMER II", 'url':'https://store.steampowered.com/app/594570/Total_War_WARHAMMER_II/', 'views':531, 'likes':715, 'describe': "Strategy gaming perfected. A breath-taking campaign of exploration, expansion and conquest across a fantasy world. Turn-based civilisation management and real-time epic strategy battles with thousands of troops and monsters at your command."},
        {'title': "Company of Heroes 2", 'url':'https://store.steampowered.com/app/231430/Company_of_Heroes_2/', 'views':4572, 'likes':562, 'describe': "Experience the ultimate WWII RTS platform with COH2 and its standalone expansions. This package includes the base game, which you can then upgrade by purchasing The Western Front Armies, Ardennes Assault and/or The British Forces. More info in the 'About This Game' section below."},
        {'title': "They Are Billions", 'url':'https://store.steampowered.com/app/644930/They_Are_Billions/', 'views':571, 'likes':8156, 'describe': "They Are Billions is a Steampunk strategy game set on a post-apocalyptic planet. Build and defend colonies to survive against the billions of the infected that seek to annihilate the few remaining living humans. Can humanity survive after the zombie apocalypse?"},
        {'title': "Men of War", 'url':'https://store.steampowered.com/app/244450/Men_of_War_Assault_Squad_2/', 'views':456, 'likes':714, 'describe': "Men of War: Assault Squad 2 features new single player style skirmish modes that take players from extreme tank combat to deadly sniper stealth missions. Commanders can now faceoff against opponents on various new multiplayer 1v1 – 8v8 maps"},
    ]
    FPS_pages = [
        {'title': "Tom Clancy's Rainbow Six", 'url':'https://store.steampowered.com/app/359550/Tom_Clancys_Rainbow_Six_Siege/', 'views':17, 'likes':178, 'describe': "Tom Clancy's Rainbow Six Siege is the latest installment of the acclaimed first-person shooter franchise developed by the renowned Ubisoft Montreal studio."},
        {'title': "Call of Duty", 'url':'https://store.steampowered.com/app/311210/Call_of_Duty_Black_Ops_III/', 'views':457, 'likes':456, 'describe': "Call of Duty: Black Ops III Zombies Chronicles Edition includes the full base game plus the Zombies Chronicles content expansion."},
        {'title': "Arma 3", 'url':'https://store.steampowered.com/app/107410/Arma_3/', 'views':1457, 'likes':745, 'describe': "Experience true combat gameplay in a massive military sandbox. Deploying a wide variety of single- and multiplayer content, over 20 vehicles and 40 weapons, and limitless opportunities for content creation, this is the PC’s premier military game. Authentic, diverse, open - Arma 3 sends you to war."},
        {'title': "Team Fortress 2", 'url':'https://store.steampowered.com/app/440/Team_Fortress_2/', 'views':347, 'likes':345, 'describe': "Nine distinct classes provide a broad range of tactical abilities and personalities. Constantly updated with new game modes, maps, equipment and, most importantly, hats!"},
        {'title': "Borderlands 3", 'url':'https://store.steampowered.com/app/397540/Borderlands_3/', 'views':456, 'likes':235, 'describe': "The original shooter-looter returns, packing bazillions of guns and a mayhem-fueled adventure! Blast through new worlds and enemies as one of four new Vault Hunters."},
    ]
    RCG_pages = [
        {'title': "Assetto Corsa", 'url':'https://store.steampowered.com/app/244210/Assetto_Corsa/', 'views':412, 'likes':561, 'describe': "Assetto Corsa v1.16 introduces the new 'Laguna Seca' laser-scanned track, 7 new cars among which the eagerly awaited Alfa Romeo Giulia Quadrifoglio! Check the changelog for further info!"},
        {'title': "BeamNG drive", 'url':'https://store.steampowered.com/app/284160/BeamNGdrive/', 'views':903, 'likes':783, 'describe': "A dynamic soft-body physics vehicle simulator capable of doing just about anything."},
        {'title': "CarX Drift Racing Online", 'url':'https://store.steampowered.com/app/635260/CarX_Drift_Racing_Online/', 'views':63, 'likes':52, 'describe': "CarX Drift Racing Online is your chance to immerse yourself in the real world of drifting. Get together with friends, tune your car and burn some tires!"},
        {'title': "Forza Horizon 4", 'url':'https://store.steampowered.com/app/1293830/Forza_Horizon_4/', 'views':235, 'likes':2114, 'describe': "Dynamic seasons change everything at the world’s greatest automotive festival. Go it alone or team up with others to explore beautiful and historic Britain in a shared open world."},
        {'title': "Wreckfest", 'url':'https://store.steampowered.com/app/228380/Wreckfest/', 'views':124, 'likes':51, 'describe': "Wreckfest is a demolition derby themed racing game with soft-body damage modeling, sophisticated driving dynamics and in-depth vehicle upgrading, featuring both demolition derbies and more traditional track races. It’s all about fun, breakneck racing and over-the-top crashes."},
    ]
    CAG_pages = [
        {'title': "Slay the Spire", 'url':'https://store.steampowered.com/app/646570/Slay_the_Spire/', 'views':321, 'likes':324, 'describe': "We fused card games and roguelikes together to make the best single player deckbuilder we could. Craft a unique deck, encounter bizarre creatures, discover relics of immense power, and Slay the Spire!"},
        {'title': "Tabletop Simulator", 'url':'https://store.steampowered.com/app/286160/Tabletop_Simulator/', 'views':90, 'likes':241, 'describe': "Tabletop Simulator is the only simulator where you can let your aggression out by flipping the table! There are no rules to follow: just you, a physics sandbox, and your friends. Make your own online board games or play the thousands of community created mods. Unlimited gaming possibilities!"},
        {'title': "KARDS The WWII Card Game", 'url':'https://store.steampowered.com/app/544810/KARDS__The_WWII_Card_Game/', 'views':63, 'likes':12, 'describe': "KARDS, The World War II Card Game, combines traditional CCG gameplay with innovative mechanics inspired by classic strategy games and real battlefield tactics. Take command and challenge other players in grand-scale warfare on the ground, air, or seas."},
        {'title': "Monster Train", 'url':'https://store.steampowered.com/app/1102190/Monster_Train/', 'views':67, 'likes':634, 'describe': "Monster Train is a strategic roguelike deck building game with a twist. Set on a train to hell, you’ll use tactical decision making to defend multiple vertical battlegrounds. With real time competitive multiplayer and endless replayability, Monster Train is always on time."},
    ]
    SLG_pages = [
        {'title': "CounterStrike: Global Offensive", 'url':'https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/', 'views':4236, 'likes':3223, 'describe': "Counter-Strike: Global Offensive (CS: GO) expands upon the team-based action gameplay that it pioneered when it was launched 19 years ago. CS: GO features new maps, characters, weapons, and game modes, and delivers updated versions of the classic CS content (de_dust2, etc.)."},
        {'title': "Dota 2", 'url':'https://store.steampowered.com/app/570/Dota_2/', 'views':623, 'likes':46, 'describe': "Every day, millions of players worldwide enter battle as one of over a hundred Dota heroes. And no matter if it's their 10th hour of play or 1,000th, there's always something new to discover. With regular updates that ensure a constant evolution of gameplay, features, and heroes, Dota 2 has taken on a life of its own."},
        {'title': "Sid Meier's Civilization", 'url':'https://store.steampowered.com/app/8930/Sid_Meiers_Civilization_V/', 'views':62, 'likes':346, 'describe': "Create, discover, and download new player-created maps, scenarios, interfaces, and more!"},
        {'title': "Paladins", 'url':'https://store.steampowered.com/app/444090/Paladins/', 'views':523, 'likes':123, 'describe': "Join 25+ million players in Paladins, the free-to-play fantasy team-based shooter sensation. Wield guns and magic as a legendary Champion of the Realm, customizing your core set of abilities to play exactly how you want to play."},
        {'title': "Plants vs. Zombies", 'url':'https://store.steampowered.com/app/3590/Plants_vs_Zombies_GOTY_Edition/', 'views':562, 'likes':56, 'describe': "Zombies are invading your home, and the only defense is your arsenal of plants! Armed with an alien nursery-worth of zombie-zapping plants like peashooters and cherry bombs, you'll need to think fast and plant faster to stop dozens of types of zombies dead in their tracks."},
    ]

    cats = {'ACT': {'pages': ACT_pages, 'views':12248, 'likes':6434},
            'ARPG': {'pages': ARPG_pages, 'views':64124, 'likes':2132},
            'AVG': {'pages': AVG_pages, 'views':35322, 'likes':1326},
            'FPS': {'pages': FPS_pages, 'views':24231, 'likes':23412 },
            'RCG': {'pages': RCG_pages, 'views':3412, 'likes': 4122},
            'RTS':{'pages': RTS_pages, 'views':19229, 'likes':34122},
            'CAG':{'pages': CAG_pages, 'views':23224, 'likes':9887},
            'SLG':{'pages': SLG_pages, 'views':12902, 'likes':3223}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'],p['likes'],p['describe'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0, likes=0, describe=''):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.likes = likes
    p.describe = describe
    p.save()
    return p 

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Game population script...')
    populate()