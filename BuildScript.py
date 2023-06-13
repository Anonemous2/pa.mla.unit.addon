# This script was written by Anonemous2 11/26/2020

# import os subprocess module
import os
# import json module
import json
from json.decoder import JSONDecodeError


def main():
    # starts by asking for correct directory to media PA
    # use default, then ask if the user wants to change it.
    media_dir = "C:/Program Files (x86)/Steam/steamapps/common/Planetary Annihilation Titans/media"
    print("Is the following directory correct? (y/n): " + media_dir)
    user_input = str(input())
    if (user_input.lower()) == "n":
        while user_input.lower() != "y":
            print("Enter new media directory: ")
            media_dir = str(input())
            media_dir = media_dir.replace('\\', '/')
            print("Is the following directory correct? (y/n): " + media_dir)
            user_input = str(input())
    # setup unit mod folder
    # find current directory
    home_dir = os.path.dirname(os.path.realpath(__file__))
    home_dir = home_dir.replace('\\', '/')
    print(home_dir)
    # create the units dir
    create_dir("/pa", home_dir)
    create_dir("/pa/units", home_dir)

    update_shadows(media_dir)


def create_dir(new_dir, home_dir):
    print("--Create Dir--")
    final_dir = home_dir + new_dir
    try:
        os.makedirs(final_dir)
    except OSError as error:
        print(error)

# this function makes changes to any units Second Wave edits; energy storages, galata, and flak.
def update_shadows(media_dir):
    # galata
    # find unit
    if os.path.exists(media_dir + "/pa_ex1/units/land/air_defense/air_defense.json"):
        update_path = media_dir + "/pa_ex1/units/land/air_defense/air_defense.json"
        print(update_path)
    elif os.path.exists(media_dir + "/pa/units/land/air_defense/air_defense.json"):
        update_path = media_dir + "/pa/units/land/air_defense/air_defense.json"
        print(update_path)
    else:
        print("EER1")
        update_path = ""
    # attempt to open air_defense, edit alt build
    with open(update_path, 'r') as file:
        file_data = json.load(file)
        # set build separation
    sep = 50
    file_data["alt_area_build_separation"] = sep
    file_data.pop("alt_area_build_pattern", None)
    # attempt to make the directories required
    try:
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/air_defense/")
    except OSError as error:
        print(error)
    # save file to pa_ex1
    with open(
        os.path.dirname(os.path.realpath(__file__))
        + "/pa_ex1/units/land/air_defense/air_defense.json",
        'w'
    ) as file:
        json.dump(file_data, file)

    # flak
    # find unit
    if os.path.exists(media_dir + "/pa_ex1/units/land/air_defense_adv/air_defense_adv.json"):
        update_path = media_dir + "/pa_ex1/units/land/air_defense_adv/air_defense_adv.json"
        print(update_path)
    elif os.path.exists(media_dir + "/pa/units/land/air_defense_adv/air_defense_adv.json"):
        update_path = media_dir + "/pa/units/land/air_defense_adv/air_defense_adv.json"
        print(update_path)
    else:
        print("EER1")
        update_path = ""
    # attempt to open air_defense_adv, edit alt build
    with open(update_path, 'r') as file:
        file_data = json.load(file)
    # set build separation
    sep = 30
    file_data["alt_area_build_separation"] = sep
    file_data.pop("alt_area_build_pattern", None)
    # attempt to make the directories required
    try:
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/air_defense_adv/")
    except OSError as error:
        print(error)
    # save file to pa_ex1
    with open(
        os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/air_defense_adv/air_defense_adv.json",
        'w'
    ) as file:
        json.dump(file_data, file)

    # gile
    # find unit weapon
    if os.path.exists(media_dir + "/pa_ex1/units/land/bot_sniper/bot_sniper_beam_tool_weapon.json"):
        update_path = media_dir + "/pa_ex1/units/land/bot_sniper/bot_sniper_beam_tool_weapon.json"
        print(update_path)
    elif os.path.exists(media_dir + "/pa/units/land/bot_sniper/bot_sniper_beam_tool_weapon.json"):
        update_path = media_dir + "/pa/units/land/bot_sniper/bot_sniper_beam_tool_weapon.json"
        print(update_path)
    else:
        print("EER1")
        update_path = ""
    # attempt to open bot_sniper_beam_tool_weapon, update anti_entity_targets
    with open(update_path, 'r') as file:
        file_data = json.load(file)
    # set anti missile weapon
    targets = '/pa/units/land/bot_tactical_missile/bot_tactical_missile_ammo.json', \
              '/pa/units/air/bomber_adv/bomber_adv_ammo.json', \
              '/pa/units/land/tactical_missile_launcher/tactical_missile_launcher_ammo.json', \
              '/pa/units/addon/naval_anti_orbital_ship/naval_anti_orbital_ammo.json', \
              '/pa/units/sea/missile_ship/missile_ship_ammo.json'
    file_data["anti_entity_targets"] = targets
    # attempt to make the directories required
    try:
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/bot_sniper/")
    except OSError as error:
        print(error)

    # save file to pa_ex1
    with open(
        os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/bot_sniper/bot_sniper_beam_tool_weapon.json",
        'w'
    ) as file:
        json.dump(file_data, file)

    # alt build for pgen

    # alt build for adv pgen

    # legion
    # we ask for the legion dir before starting
    print("please enter the dir for legion's server mod:")
    user_input = "n"
    while user_input.lower() != "y":
        print("Enter new media directory: ")
        media_dir = str(input())
        media_dir = media_dir.replace('\\', '/')
        print("Is the following directory correct? (y/n): " + media_dir)
        user_input = str(input())

    # omni storage
    # aa
    # adv aa
    # shield

main()

# end of program
print("---END---")