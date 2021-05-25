from random import randint
import copy

story = ("This one is for the {} with the {} system, top down, AC with the cooler system, When he come up in the {} he be {}, Got stacks on deck like he savin' up. And he {}, he {}, he might gotta deal. He pop {} and he got the right kind of build. He {}, he {}, he might sell {}. He always in the {}, but he never fly coach"
         )

# create a dictionary to look uo words by type

word_dict = {
    "adjective": ["dead", "hairless", "sadistic", "wild", "cocky", "internet worthy", "sick", "frozen", "frisky", "magical", "pea-brained", "medium ugly", "got the IQ of meek mill", "short sighted"],
    "noun": ["blood rage", "idot", "toaster", "legend", "death wish", "therapy", "kitty", "psychic", "hairy legs", "cottage pie", "hissy fit"],
    "being": ["hot girls", "city girls", "beach boys", "toy boys", "silly billys", "anime fans", "tea drinkers", "conspiracy theorists", "nut-cases"],
    "booming": ["dead", "loud-ass", "fire", "kinda whack", "broke", "meme worthy", "sexy", "broken", "frisky", "magical", "bad-ass"],
    "club": ["therapy", "kitty", "silent disco", "maccies D's", "glee club", "primark boxing day sale", "flat earth society", "soul society", "bando", ],
    "blazing-up": ["sicking up", "fighting babies", "farting up", "acting stupid", "twerking like miley", "auditioning for xfactor", "shaking that thang"],
    "bottles": ["therapy", "kitty", "psychic", "hairy legs", "cottage pie", "childrens balloons", "my hopes and dreams", "£5 bottles of Echo Falls"],
    "coke": ["toasters", "lelly kellys", "chicken nuggets", "souls", "cottage pie", "cookie dough"]
}


def get_word(type, local_dict):
    words = local_dict[type]
    # further understanding of count and index purpose
    count = len(words)-1
    index = randint(0, count)
    return local_dict[type].pop(index)


def create():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word("being", local_dict),
        get_word("booming", local_dict),
        get_word("club", local_dict),
        get_word("blazing-up", local_dict),
        get_word("adjective", local_dict),
        get_word("adjective", local_dict),
        get_word("bottles", local_dict),
        get_word("adjective", local_dict),
        get_word("noun", local_dict),
        get_word("coke", local_dict),
        get_word("noun", local_dict),
    )


print("LYRIC 1: ")
print(create())
print()
print("LYRIC 2: ")
print(create())
