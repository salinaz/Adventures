print("welcome to your adventure. please input the capitalized phrases to prompt you further on your journey.")
deci1 = input("go LEFT or RIGHT?")
if deci1 == "LEFT":
    print("you end up in the mountains, on the wooded bank near a set of crystalline rapids.")
    deci2 = input("go FORAGE in the copse of trees or go FISHING in the waters?")
    if deci2 == "FISHING":
        print("you run into an angry bear and try to steal his lunch. he doesn't take lightly to this, so you get rekt by the bear and end up as a side dish of his lunch instead.")
    if deci2 == "FORAGE":
        print("you find some berries and fruit, eating your fill.")
        deci3 = input("take a NAP or continue to EXPLORE your surroundings?")
        if deci3 == "NAP":
            print("the day goes by, completely uneventful. you wake up during the night with the crescent moon shining overhead.")
            deci4 = input("go back to SLEEP or try to EXPLORE the area in the dark?")
            if deci4 == "SLEEP":
                    print("a giant owl swoops by to find a light breakfast for its owlets. congrats, you officially got turned into baby food.")
            if deci4 == "EXPLORE":
                    print("you narrowly avoid the giant owls soaring overhead and take refuge in a cave with some 'friendly' vampire bats that toootallly aren't trying to drink your blood.")
                    deci5 = input("find some wild GARLIC to (hopefully) stay safe or take a chance and TOUGH it out?")
                    if deci5 == "GARLIC":
                        print("your precautions pay off and you get a peaceful night's sleep among a caveload of batdung. that's probably a win?")
                        deci6 = input("VENTURE out during the day to find better accomodations or only head out to get some FOOD?")
                        if deci6 == "VENTURE":
                            print("you head out a bit too far into some exposed foothills and get airlifted by the giant eagles. you're never seen or heard from ever again.")
                        if deci6 == "FOOD":
                            print("you encroach on the territory of a nearby colony of grumpy cats. they don't seem as delightfully sardonic as their memed overlord and they chase you off after you sustain a lot of scratches.")
                            deci7 = input("try to CHARM the cats one more time or TEND to your wounds?")
                            if deci7 == "CHARM":
                                print("the cats aren't impressed and decide to destroy you with a superpowered cannon of adorable rage.")
                            if deci7 == "TEND":
                                print("you have no idea what you're doing when it comes to medical matters, so you end up dead anyway.")
                    if deci5 == "TOUGH":
                        print("the bats turn you into a human drink keg during one of their devious nightly bat frat parties. what a way to end.")
if deci1 == "RIGHT":
    print("you end up in a dark forest, with gnarled trees swathed in brambles and cobwebs.")
    deci10 = input("take the path on the RIGHT or continue FORWARD explore the wild?")
    if deci10 == "RIGHT":
        print("the path leads you around the forest and you end up being murdered by a tribe of brutal coconut warriors who don't like you and your trespassing.")
    if deci10 == "FORWARD":
        print("you go further and further into the wild until the wolves find you. they don't feel like being helpful today so they decided to eat you as a snack.")
