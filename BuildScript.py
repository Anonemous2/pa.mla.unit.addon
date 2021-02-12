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

    # start creating modified units
    # must create a list off all unit jsons first
    print("---Find---")
    # create a list of files
    found_files = []
    print("The following files have been found:")
    for root, dirs, files in os.walk(media_dir + "/pa/units"):
        for name in files:
            file = os.path.join(root, name)
            file = file.replace('\\', '/')
            # print(file)
            found_files.append(file)
    json_files = remove_other(found_files)
    update_build(json_files, media_dir)
    # use remove_other method
    found_files = []
    # use remove_dev_buildables
    remove_dev_buildables()
    for root, dirs, files in os.walk(media_dir + "/pa_ex1/units"):
        for name in files:
            file = os.path.join(root, name)
            file = file.replace('\\', '/')
            # print(file)
            found_files.append(file)
    # use remove_other method
    json_files = remove_other(found_files)
    update_build(json_files, media_dir)
    # use update_shadow method
    update_shadows(media_dir)


def update_build(json_files, media_dir):
    print("--Build Update--")
    # find current directory to save changes to it
    save_path = os.path.dirname(os.path.realpath(__file__))
    save_path = save_path.replace('\\', '/')
    total = len(json_files)
    index = 0
    while index < total:
        try:
            with open(json_files[index]) as file:
                file_data = json.load(file)
            # print(file_data)
            if "buildable_types" in file_data:
                print("Build json: " + json_files[index])
                # save buildtype info
                file_data_prebuild = json.dumps(file_data["buildable_types"])
                print(file_data_prebuild)

                # append build types
                # if they do exist, add brackets to append, and strip target_priorities
                data_to_append = file_data["buildable_types"]
                print("LLL4")
                updated_data = json.dumps(data_to_append)
                updated_data = "(" + updated_data[1:]
                updated_data = updated_data[:-1] + ") - Custom1 - Custom2 - Custom3 - Custom4"

                # update buildtypes
                print(updated_data)
                file_data["buildable_types"] = updated_data
                print(file_data)

                # save to new directory
                new_dir_save = json_files[index]
                new_dir_save = new_dir_save.replace(media_dir, "")
                file_name = new_dir_save[new_dir_save.rfind('/') + 1:]
                # attempt to create directories
                # loop through file until no more sub directories exist
                pulled_dir = ""
                dir_end_index = new_dir_save.find('/')
                while dir_end_index != -1:
                    new_dir = new_dir_save[:dir_end_index]
                    try:
                        os.mkdir(save_path + pulled_dir + new_dir)
                    except OSError as error:
                        print(error)
                    pulled_dir += new_dir + "/"
                    new_dir_save = new_dir_save[(dir_end_index + 1):]
                    dir_end_index = new_dir_save.find('/')
                final_dir = save_path + pulled_dir + file_name
                print(final_dir)
                with open(final_dir, "w+") as new_file:
                    json.dump(file_data, new_file)
                print(json.dumps(file_data))
            else:
                print("No buildable_types")
        except UnicodeDecodeError as error:
            print(error)
        except JSONDecodeError as error:
            print(error)
        index += 1


def remove_other(found_files):
    json_files = []

    for file in found_files:
        if file.find('.json') != -1:
            json_files.append(file)
    print("--Final--")
    # for item in json_files:
    # print(item)
    print(json_files)
    return json_files


def create_dir(new_dir, home_dir):
    print("--Create Dir--")
    final_dir = home_dir + new_dir
    try:
        os.mkdir(final_dir)
    except OSError as error:
        print(error)

# this function deletes the shadow for the avatar and avatar_factory, so they can still build everything
def remove_dev_buildables():
    remove_path = os.path.dirname(os.path.realpath(__file__))
    remove_path = remove_path.replace('\\', '/')
    # delete avatar from the updated jsons
    try:
        avatar = remove_path + "/pa/units/commanders/avatar/avatar.json"
        os.remove(avatar)
        os.rmdir(remove_path + "/pa/units/commanders/avatar")
    except OSError as error:
        print("EEE1")
        print(error)
    # delete avatar_factory from the updated jsons
    try:
        avatar = remove_path + "/pa/units/land/avatar_factory/avatar_factory.json"
        os.remove(avatar)
        os.rmdir(remove_path + "/pa/units/land/avatar_factory")
    except OSError as error:
        print("EEE1")
        print(error)


# this function makes changes to any units Second Wave edits; energy storages, galata, and flak.
def update_shadows(media_dir):
    # energy_storage
    # find unit
    if os.path.exists(media_dir + "/pa_ex1/units/land/energy_storage/energy_storage.json"):
        update_path = media_dir + "/pa_ex1/units/land/energy_storage/energy_storage.json"
        print(update_path)
    elif os.path.exists(media_dir + "/pa/units/land/energy_storage/energy_storage.json"):
        update_path = media_dir + "/pa/units/land/energy_storage/energy_storage.json"
        print(update_path)
    else:
        print("EER1")
        update_path = ""
    # attempt to open energy_storage, edit storage
    with open(update_path, 'r') as file:
        file_data = json.load(file)
    # open damage value, then divide it by 6
    storage = json.dumps(file_data["storage"]["energy"])
    storage = int(int(storage) * 5)
    file_data["storage"]["energy"] = storage
    # attempt to make the directories required
    try:
        os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/energy_storage")
    except OSError as error:
        print(error)

    # save file to pa_ex1
    with open(
        os.path.dirname(os.path.realpath(__file__))
        + "/pa_ex1/units/land/energy_storage/energy_storage.json", 'w'
    ) as file:
        json.dump(file_data, file)

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
        os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/air_defense/")
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
        os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/air_defense_adv/")
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
        os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/pa_ex1/units/land/bot_sniper/")
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