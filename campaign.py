

def create_campaign():
    """
    This function mix all the list of actions below returning a cool idea to gain attention to your brand.
    Is your work to evaluate it and realize if the campaign is aligned with thes imbolic valueo of your brand.
    You can also enlarge the list of action and help to develop the campaigns creator.
    """

    import random           
    [divide_actions(_tuple) for _tuple in actions]
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    action = verb, noun
    print (action)

actions = [("jump from 10th floor", "swimmingpool"),("stealt", "dog"), ("fight in the", "street"), ("break","art_expo"),
    ("walk with","exotic animal"), ("eat","rotten mushrooms"), ("f*ck at", "insta live"),
    ("build a", "obelisk of cupcakes"), ("break your own", "artwork"),("make show with a", "dwarf"),
    ("paper the city with", "ants"),("sing song with","homeless"),("kill","drugdealer"),
    ("auction a", "painting"), ("in the show give away", "sweets"),("release a song with", "2 possible endings"),
    ("give away", "acapellas"), ("upload a", "ridiculous video"),("crash","car"),("go to", "jail"),
    ("upload photos", "without clothes"),("have", "beef"),("go to the","hospital"),("suffer a","kidnapping"),
    ("make beef to","a entire city"),("overdoze of", "drugs"),("make jokes about","legal charges"),("be a model in a","parade"),
    ("video riding","unicycle"),("sell workshop to a", "supermarket"),("exchange beer to","antares"),("flyers in","cabins"),
    ("with golf club break","tv"),("video dressed as","student"),("convert institute in","giant videogame"),
    ("paper","university"),("encroach a","event"),("giant burguer in the ", "center of the city"),
    ("gender performance in the","train"),("paint logo in the face at/of","latin grammys"),
    ("sail with a","plastic boat"),("population using daily your","app"),
    ("make a song about", "death of the police"),("criticize a","parent"),("having problems with","celebrities"),
    ("get shot in","shooting"),("make them think you are","illuminati"),("make video with","high sexual content")]
verbs = []
nouns = []

def divide_actions(_tuple):
    """
    This function divide the tuple of verb/noun so create_campaign function can mix them
    """
    verbs.append(_tuple[0])
    nouns.append(_tuple[1]) 

create_campaign()

warfare_marketing = ["unexpected", "inmediatte action","impact in the mass media"
    "don't realease ads in saturated media", "uncommon places, público desprevenidoxs",
    "concentration in a channel", "don't divide forces in different strategies","analogic meme = resignify",
    "bewilderment","right poster in the right place","surprise effect","empathy","5 senses"]





