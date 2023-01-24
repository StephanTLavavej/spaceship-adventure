class Room:
    def __init__(self, room_name, room_description, room_exits):
        self.name = room_name
        self.description = room_description
        self.exits = room_exits


all_rooms = [
    Room(
        "Bridge",
        "This is where they FLY the SHIP. Well, it's where the crew presses the "
        "buttons that the captain orders them to. Button pressing is still cool! "
        "Crew members who have had enough coolness for one day can leave to the "
        "south in search of pizza and/or sleep.",
        {"south": "Bright Hallway"},
    ),
    Room(
        "Sickbay",
        "The autodoc is currently dormant, but could be called upon to repair any "
        "organic being. This room is the safest room on the ship. Danger awaits to "
        "the east. (Well, not directly east, it's just the hallway out there.)",
        {"east": "Bright Hallway"},
    ),
    Room(
        "Bright Hallway",
        "The lighting here is powerful and steady. You hear soothing beeps, "
        "buzzes, and warbles to the north. There are more doors to the east and "
        "west. The hallway continues south, although the lighting barely does.",
        {
            "north": "Bridge",
            "east": "Ready Room",
            "south": "Dark Hallway",
            "west": "Sickbay",
        },
    ),
    Room(
        "Ready Room",
        "The senior officers get ready in this room, whatever that means. You "
        "suspect that they play video games in here. The ship's cat, Admiral "
        "Whiskers, is curled up on the conference table. It would be nice to "
        "PET the KITTY. An automatic door is ready to serve you, to the west.",
        {"west": "Bright Hallway"},
    ),
    Room(
        "Crew Quarters",
        "Bunk beds fill this room, but nobody's here. There's a sliding door in "
        "the east wall.",
        {"east": "Dark Hallway"},
    ),
    Room(
        "Dark Hallway",
        "The lighting here is dim and flickering, but there's more intense light "
        "coming from the north. Your cyber-nose detects the scent of pizza to the "
        "east, grass to the south, and fresh laundry to the west. In the corner, "
        "there's a ladder leading down to pulsing red lights.",
        {
            "north": "Bright Hallway",
            "east": "Mess Hall",
            "south": "Airlock",
            "west": "Crew Quarters",
            "down": "Engineering",
        },
    ),
    Room(
        "Mess Hall",
        "It's pizza day, your favorite day of the week. Darkness and a complete "
        "lack of pizza await you to the west.",
        {"west": "Dark Hallway"},
    ),
    Room(
        "Engineering",
        "The warp core is as impressive as the day the ship was commissioned, but "
        "the flashing red lights seem ominous. You studied Core Maintenance back "
        "at the Academy - maybe you could FIX the REACTOR. In the corner, there's "
        "a ladder leading up to the rest of the ship, but why would you ever want "
        "to leave Engineering?",
        {"up": "Dark Hallway"},
    ),
    Room(
        "Airlock",
        "To the north, a heavy door could seal off the ship, but is currently "
        "open. To the south, the external door is badly damaged, and you can see "
        "sunlight through it.",
        {"north": "Dark Hallway", "south": "Cliff Edge"},
    ),
    Room(
        "Cliff Edge",
        "You stand on purple alien grass. Huge boulders prevent you from walking "
        "around the ship. The damaged airlock is to the north, while the cliff "
        "drops off steeply to the south. You avoided taking Rock Climbing back "
        "at the Academy for a reason!",
        {"north": "Airlock", "south": "Canyon Floor"},
    ),
    Room(
        "Canyon Floor",
        "You've tumbled off the cliff, to the bottom of the canyon. The autodoc "
        "in sickbay could patch you up, but alas, you're too injured to crawl back.",
        {},
    ),
]

playing_game = True
won_game = False
current_room_name = "Crew Quarters"
working_reactor = False


def current_room_description():
    for room in all_rooms:
        if room.name == current_room_name:
            return room.description

    assert False, "Couldn't find current_room_name in all_rooms!"


def current_room_exits():
    for room in all_rooms:
        if room.name == current_room_name:
            return room.exits

    assert False, "Couldn't find current_room_name in all_rooms!"


def take_turn():
    global current_room_name

    available_exits = current_room_exits()
    cardinal_directions = {"north", "east", "south", "west", "up", "down"}

    player_command = input("> ")

    if player_command == "help":
        print(
            "     help - Sponsored by Universal Reactors, making quality warp engines since 3347!"
        )
        print("     quit - Quit the game. (Saving is not yet implemented.)")
        print("     look - Before you leap.")
        print("    north - Never.")
        print("     east - Eat.")
        print("    south - Shredded.")
        print("     west - Wheat.")
        print("       up - Rockets go in this direction.")
        print("     down - Apples fall in this direction.")
        print("verb noun - There are three SECRET COMMANDS of this form.")
    elif player_command == "quit":
        print("Ok, but quitters never win.")
        global playing_game
        playing_game = False
    elif player_command == "look":
        print(current_room_name)
        print(current_room_description())
    elif player_command in available_exits:
        current_room_name = available_exits[player_command]
        print("You move " + player_command + " to: " + current_room_name)
    elif player_command in cardinal_directions:
        print("There's no exit in that direction.")
    elif player_command == "fix reactor":
        if current_room_name == "Engineering":
            print(
                "You've fixed the reactor! (Updated room descriptions are not yet implemented.)"
            )
            global working_reactor
            working_reactor = True
        else:
            print("There's no reactor here.")
    elif player_command == "pet kitty":
        if current_room_name == "Ready Room":
            print("Admiral Whiskers purrs contentedly as you scritch between her ears.")
        else:
            print("There's no kitty here. Aw.")
    elif player_command == "fly ship":
        if current_room_name == "Bridge":
            if working_reactor:
                print("With a delightful hum, the ship takes off and enters orbit!")
                global won_game
                won_game = True
                playing_game = False
            else:
                print("You press the buttons to make the ship go, but it won't go.")
                print("Maybe something's wrong with the reactor?")
        else:
            print("There's no flight control console here.")
    else:
        print("Unknown command.")

    print("")


def main():
    print("Welcome to Spaceship Adventure!")
    print("If you need assistance, type: help")
    print("")
    print("You wake up in: " + current_room_name)
    print("")

    while playing_game:
        take_turn()

    if won_game:
        print("Congratulations, you won Spaceship Adventure!")
        print("Thanks for playing!")
    else:
        print("Sorry, you lost Spaceship Adventure!")
        print("Better luck next time!")


main()

# Spoilers...
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#                     ┌──────┐
#                     │Bridge│
#                     └──┬───┘
#                        │
#       ┌───────┐ ┌──────┴───────┐ ┌──────────┐
#       │Sickbay├─┤Bright Hallway├─┤Ready Room│
#       └───────┘ └──────┬───────┘ └──────────┘
#                        │
# ┌─────────────┐  ┌─────┴──────┐  ┌─────────┐
# │Crew Quarters├──┤Dark Hallway├──┤Mess Hall│
# └─────────────┘  └─────┬──────┘  └─────────┘
#                        │     ▲
#                    ┌───┴───┐ └─┐
#                    │Airlock│   └─┐
#                    └───┬───┘     └─┐
#                        │           ▼
#                   ┌────┴─────┐    ┌───────────┐
#                   │Cliff Edge│    │Engineering│
#                   └────┬─────┘    └───────────┘
#                        │
#                  ┌─────┴──────┐
#                  │Canyon Floor│
#                  └────────────┘

# TODO:
# * Accept case-insensitive player commands (e.g. "NORTH")
# * Accept abbreviated player commands (e.g. "n" for "north", "l" for "look")
# * Update room descriptions when variables change
#   + For example, Engineering and Dark Hallway refer to flashing red lights,
#     and Engineering says that the reactor is broken. This should change after
#     the player fixes the reactor.
# * Add more puzzles
#   + Plot hole: The airlock is open/damaged but this doesn't prevent the ship
#     from taking off.
# * Global variables are problematic
#   + Use classes, or something? As programs grow, this becomes a bigger problem
# * Improve the data structure for all_rooms
#   + Currently it's a list of rooms, and we need a for-loop to search for
#     a given room name. A dictionary, mapping from name to room, would be
#     easier to use (and more efficient)
# * Improve how room connections are set up
#   + Currently, Room A needs to say that it has an exit east to Room B, and
#     then Room B needs to say that it has an exit west to Room A. Almost
#     all rooms have bidirectional connections (i.e. you can walk from A to B
#     and then back to A), so setting this up should be easier. However,
#     we should keep the ability to have one-way connections, e.g. the exit
#     from Cliff Edge to Canyon Floor
# * Could implement items
# * Could implement NPCs with dialogue
