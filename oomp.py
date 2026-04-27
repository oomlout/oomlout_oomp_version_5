
import oomp_bip39

import oom_git

import copy

parts = {}
parts_md5 = {}
parts_md5_5 = {}
parts_md5_6 = {}
parts_md5_6_alpha = {}
parts_md5_10 = {}
parts_short_code = {}




names_of_main_elements = []
for i in range(1, 16):
    names_of_main_elements.append(f"taxonomy_{i}")


def clone_data_files():
    repo_list = []
    repo_list.append("https://github.com/oomlout/oomlout_oomp_footprint_bot")
    repo_list.append("https://github.com/oomlout/oomlout_oomp_symbol_bot")
    repo_list.append("https://github.com/oomlout/oomlout_oomp_project_bot")

    #if tmp/ doesn't exist create it
    
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    for repo in repo_list:
        #clone repo using os.system to tmp/repo_name
        print(f"cloning {repo}")
        
        repo_name = repo.split('/')[-1] 
        directory = "tmp"     
        oom_git.clone(repo=repo, directory=directory)
        oom_git.pull(directory=directory)




def load_parts(**kwargs):
    global add_part_filter
    from_yaml = kwargs.get("from_yaml", True)
    from_pickle = kwargs.get("from_pickle", False)
    from_folders = kwargs.get("from_folders", False)
    filter = kwargs.get("filter", "")
    add_part_filter = filter
    if from_pickle:
        print ("loading parts from pickle")
        oomp_create_parts.load_parts_from_pickle(**kwargs)
        #load extra dicts
        load_extra_dicts()
    elif from_folders:
        directory = kwargs.get("directory", "parts")
        load_parts_from_folders(directory=directory)
    elif from_yaml:
        print ("loading parts from yaml")
        oomp_create_parts.load_parts_from_yaml(**kwargs)
    
    else:
        print ("loading parts from module")
        oomp_create_parts.load_parts(**kwargs)
    return parts

def load_parts_from_folders(**kwargs):
    global parts
    print("loading parts from folders")
    directory = kwargs.get("directory", "parts")
    #go through each folder in the parts directory
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            #look for working.yaml in the folder
            working_yaml_path = os.path.join(folder_path, "working.yaml")
            if os.path.isfile(working_yaml_path):
                import yaml
                with open(working_yaml_path, "r") as infile:
                    part = yaml.load(infile, Loader=yaml.FullLoader)
                    parts[part["id"]] = part
    parts = parts
    return parts

def load_extra_dicts():
    global parts_md5
    global parts_md5_5
    global parts_md5_6
    global parts_md5_6_alpha
    global parts_md5_10
    global parts_short_code
    for part in parts:
        part = part.lower()
        parts_md5[parts[part]["md5"]] = parts[part]
        parts_md5_5[parts[part]["md5_5"]] = parts[part]
        parts_md5_6[parts[part]["md5_6"]] = parts[part]
        parts_md5_6_alpha[parts[part]["md5_6_alpha"]] = parts[part]
        parts_md5_10[parts[part]["md5_10"]] = parts[part]
        parts_short_code[parts[part]["short_code"]] = parts[part]


def save_parts(**kwargs):
    oomp_create_parts.save_parts_to_yaml(**kwargs)
    oomp_create_parts.save_parts_to_pickle(**kwargs)

def save_parts_to_individual_yaml_files(**kwargs):
    oomp_create_parts.save_parts_to_individual_yaml_files(**kwargs)

def create_parts_readme_old():
    print("creating parts readme")
    #create a file called parts_readme.md that links to all the parts in the parts directory
    readme = ""
    readme += "# Parts\n"
    readme += "\n"
    for part in parts:
        readme += f"[{parts[part]['name']}](parts/{parts[part]['id']}/readme.md)\n"
    with open("readme_parts.md", "w") as outfile:
        outfile.write(readme)

    


def add_parts(parts,**kwargs):
    parts_full_list = []
    #expand the parts list into parts_processed, make this a list of permutations of the part using itertools
    import itertools

    # Initialize an empty dictionary for lists
    my_dict_lists = {}

    # Convert all the dictionary values to lists but only use the keys in names_of_main_elements
    
    for part in parts:

        #test if any elelment in the part is a list
        list_in_part = False
        # get all the dict values that aren't in names_of_main_elements 
        not_main_elements = {}
        for key, value in part.items():
            if key not in names_of_main_elements:
                not_main_elements[key] = (part[key])
        
        for key, value in part.items():
            if isinstance(value, list):
                list_in_part = True
        if True:
            part_full = {}
            part_full.update(part)  
            part_full.update(kwargs)  
            parts_full_list.append(part_full)
            #add_part(classification=part["classification"], type=part["type"], size=part["size"], color=part["color"], description_main=part["description_main"], description_extra=part["description_extra"], manufacturer=part["manufacturer"], part_number=part["part_number"], not_main_elements=not_main_elements, **kwargs)

    #go through each item in parts_full_list and run it through add_part but use threading on 6 cores
    import threading
    threads = []
    for part in parts_full_list:
        thread = threading.Thread(target=add_part, kwargs=part)
        threads.append(thread)
        thread.start()




add_part_filter = ""

cnt = 1

def add_part(**kwargs):
    global cnt
    global add_part_filter
    global parts
    make_files = kwargs.get("make_files", True)

    
    ## get id
    import copy
    add_part_filters = copy.deepcopy(add_part_filter)
    if not isinstance(add_part_filters, list):
        add_part_filters = [add_part_filters] 
    id = get_id(**kwargs)
    for add_part_filter in add_part_filters:
        if add_part_filter in id:
            
            
            
            ## add part to dict
            #print("    adding part " + id)
            

            #add formated taxonomy
            
            formats = ["upper","capital","first_letter","first_letter_upper"]
            for typ in names_of_main_elements:
                value_test = kwargs.get(typ, "")
                if value_test != "":
                    for format in formats:
                        kwargs[f"{typ}_{format}"] = kwargs[typ]
                        first_letter = ""
                        if kwargs[typ] != "":
                            first_letter = kwargs[typ][0]
                        if format == "upper":
                            kwargs[f"{typ}_{format}"] = kwargs[typ].upper()
                        if format == "capital":
                            
                            value = kwargs[typ].replace("_", " ").title()
                            value = value.replace(" X ", " x ")
                            value = value.replace("Mm", "mm")
                            for i in range(1,10):
                                for j in range(1,10):
                                    src_value = f"{i} {j}"
                                    dst_value = f"{i}.{j}"
                                    value = value.replace(src_value, dst_value)
                            kwargs[f"{typ}_{format}"] = value
                        if format == "first_letter":
                            kwargs[f"{typ}_{format}"] = first_letter
                        if format == "first_letter_upper":
                            kwargs[f"{typ}_{format}"] = first_letter.upper()


            #add id as a keyed item to kwargs
            kwargs["id"] = id
            clas = kwargs.get("classification","none")
            ###add_id_start
            id_no_class = id.replace(f"{clas}_","")        
            kwargs["id_no_class"] = id_no_class
            typ = kwargs.get("type","none")
            id_no_type = id_no_class.replace(f"{typ}_","")        
            kwargs["id_no_type"] = id_no_type
            siz = kwargs.get("size","none")
            id_no_size = id_no_type.replace(f"{siz}_","")
            kwargs["id_no_size"] = id_no_size

            kwargs["oomp_key"] = f'oomp_{id}'
            github_link = f"https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/{id}" 
            kwargs["link_github"] = github_link
            kwargs["link_main"] = github_link
            kwargs["link_redirect"] = github_link

            
            #add the directory
            kwargs["directory"] = f'parts/{id}'

            ## add_id_end

            ## add_name_start

            #add name, the name is the id with proper capitalization and _ replaced with ' '
            kwargs["name"] = id.replace("_", " ").title()
            name_no_class = id_no_class.replace("_", " ").title()
            kwargs["name_no_class"] = name_no_class
            name_no_type = id_no_type.replace("_", " ").title()
            kwargs["name_no_type"] = name_no_type
            name_no_size = id_no_size.replace("_", " ").title()
            kwargs["name_no_size"] = name_no_size


            # add_md5_start

            #add a md5 hash of the id as a keyed item to kwargs
            import hashlib
            kwargs["md5"] = hashlib.md5(id.encode()).hexdigest()
            #trim md5 to 6 and add it as md5_6
            kwargs["md5_5"] = kwargs["md5"][0:5]
            kwargs["md5_5_upper"] = kwargs["md5"][0:5].upper()
            #add to md5_5 dict
            parts_md5_5[kwargs["md5_5"]] = id
            md5_6 = kwargs["md5"][0:6]
            kwargs["md5_6"] = md5_6
            kwargs["md5_6_upper"] = kwargs["md5_6"].upper()

            md5_6_alpha = hex_to_base36(kwargs["md5_6"])
            kwargs["md5_6_alpha"] = md5_6_alpha
            kwargs["md5_6_alpha_upper"] = kwargs["md5_6_alpha"].upper()
            
            
            parts_md5_6[kwargs["md5_6"]] = id
            kwargs["md5_10"] = kwargs["md5"][0:10]
            kwargs["md5_10_upper"] = kwargs["md5_10"].upper()
            parts_md5_10[kwargs["md5_10"]] = id
            kwargs.update(oomp_bip39.get_bip39_variants(kwargs["md5"]))
            
            
            if make_files:
                ######### file stuff
                directory_parts = "parts"
                if make_files != True:
                    directory_parts = make_files

                ## make a directory in /parts for the part the name is its id
                import os
                folder = f"{directory_parts}/" + id
                if not os.path.exists(folder):
                    try:
                        os.makedirs(folder)
                    except Exception as e:
                        print(f"Error creating directory {folder}: {e}")
                        return
                
                import yaml
                import copy
                p2 = copy.deepcopy(kwargs)
                p2.pop("make_files", None)
                p2.pop("counter", None)

                with open(f"{directory_parts}/" + id + "/working.yaml", "w") as outfile:
                    yaml.dump(p2, outfile, indent=4)


            parts[id] = kwargs
        else:
            print("    skipping part " + id)
            pass
    cnt += 1
    if cnt % 100 == 0:
        print(f".", end="")
    return kwargs

def hex_to_base36(hex_value):
    # Convert the hex value to an integer
    decimal_value = int(hex_value, 16)

    # Encode the integer as base36
    base36_value = ''
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, 36)
        base36_digit = '0123456789abcdefghijklmnopqrstuvwxyz'[remainder]
        base36_value = base36_digit + base36_value

    return base36_value


def get_id(**kwargs):
    #concate all the elements in kwargs from names_of_main_elements with '_' and return the string if the element isn't '' include it
    id = ""
    #populate names_of_main_elements with taxonomy1-15
    for name in names_of_main_elements:
        value = kwargs.get(name, "")
        if value != "":
            id += kwargs[name] + "_"
    #remove the trailing '_'
    id = id[:-1]
    return id

