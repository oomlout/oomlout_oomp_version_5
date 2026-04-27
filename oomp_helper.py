import copy
import glob
import os

import oomlout_roboclick


def add_icon(part, count, mode_ai_wait="slow", icon_detail=""):
    action_type = "ai"
    action_name = f"step_{count}_create_icon"
    file_test = "initial_generated_icon.png"

    detail = (
        f'{part.get("name_space", "")} {icon_detail}'
    )
    image_detail = f"an image of {detail}"

    actions = []

    action = {}
    action["command"] = "ai_skill_image_laser_cut_logo_full"
    action["file_destination"] = file_test
    action["image_detail"] = image_detail
    action["mode_ai_wait"] = mode_ai_wait
    actions.append(copy.deepcopy(action))

    action = {}
    action["command"] = "close_tab"
    actions.append(copy.deepcopy(action))



    oomlout_roboclick.add_action(
        part=part,
        action_type=action_type,
        action_name=action_name,
        actions=actions,
        file_test=file_test,
    )


def add_image(part, folder_project, files_to_trace, mode_ai_wait, count):
    words = part.get("words", [])
    prompts = []
    prompts.append(
        {
            "folder_name": f"roboclick\\{folder_project}\\prompt_three_dimension_letter_two_line_1",
            "delay": "60",
        }
    )

    for i, word in enumerate(words):
        prompts.append({"text": f'Awesome fill in the json template with "{word}"'})
        file_name = f"initial_generated_{i + 1}.png"
        prompts.append(
            {
                "file_name_image": file_name,
                "text": "Generate the image take all the time you need",
                "delay": "60",
            }
        )
        files_to_trace.append(file_name)

    part2 = copy.deepcopy(part)
    return oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)


def add_prompt_image(part, folder_project, prompt_folder, file_name, files_to_trace, mode_ai_wait, count):
    prompts = []
    prompts.append({"folder_name": f"roboclick\\{folder_project}\\{prompt_folder}", "delay": "60"})
    prompts.append(
        {
            "file_name_image": file_name,
            "text": "Generate the image take all the time you need",
            "delay": "60",
        }
    )
    files_to_trace.append(file_name)
    part2 = copy.deepcopy(part)
    return oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)


def add_value_images(part, folder_project, files_to_trace, mode_ai_wait, count):
    for i in range(1, 4):
        value = part.get(f"value_{i}", "")
        if value != "":
            count = add_prompt_image(
                part=part,
                folder_project=folder_project,
                prompt_folder=f"prompt_image_main_{i}",
                file_name=f"image_value_{i}.png",
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )
    return count


def add_cover_background(part, folder_project, files_to_trace, mode_ai_wait, count):
    part2 = copy.deepcopy(part)
    part2["background_theme"] = (
        f'A Bribe Bank with these rewards: {part.get("value_1", "")}, '
        f'{part.get("value_2", "")}, and {part.get("value_3", "")}'
    )
    prompts = []
    prompts.append({"folder_name": f"roboclick\\{folder_project}\\prompt_image_background_1", "delay": "60"})
    file_name = "image_cover_background.png"
    prompts.append(
        {
            "file_name_image": file_name,
            "text": "Generate the image take all the time you need",
            "delay": "60",
        }
    )
    files_to_trace.append(file_name)
    return oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)


def trace_files(part, files_to_trace, mode_ai_wait, count):
    for file_to_trace in files_to_trace:
        part2 = copy.deepcopy(part)
        part2["file_source"] = file_to_trace
        part2["folder_name"] = "roboclick\\action_corel_trace_1"
        if "inside_border" in file_to_trace or "logo_back" in file_to_trace:
            part2["number_of_colors"] = 2
        if "cover_background" not in file_to_trace:
            part2["remove_background_color_from_entire_image"] = True
        part2["mode_ai_wait"] = mode_ai_wait
        part2["file_test"] = "tag"
        count = oomlout_roboclick.ai_action_from_folder(part=part, part2=part2)
    return count


def make_card(part, folder_project, count):
    part2 = copy.deepcopy(part)
    part2["folder_name"] = f"roboclick\\{folder_project}\\action_corel_card_make"
    return oomlout_roboclick.ai_action_from_folder(part=part, part2=part2)


def add_research(part, folder_project, mode_ai_wait, count):
    prompts = []
    prompts.append({"folder_name": f"roboclick\\{folder_project}\\research_day_of_the_year", "delay": "120"})
    file_destination_yaml = "research.yaml"
    action_name = "research_day_of_the_year"
    part2 = copy.deepcopy(part)
    part2["new_item_name"] = "date_type"
    part2["remove_top_level"] = "data"
    return oomlout_roboclick.ai_query_from_prompts(
        part=part,
        part2=part2,
        prompts=prompts,
        mode_ai_wait=mode_ai_wait,
        count=count,
        file_destination_yaml=file_destination_yaml,
        action_name=action_name,
    )


def add_jinja_template(part, templates, mode_ai_wait="slow", count=0, convert_to_pdf=False, convert_to_png=False):
    template_root_defaults = []
    template_root_defaults.append({"template_folder": "source_file\\template_jinja\\template_jinja_label_oomlout_76_2_mm_50_8_mm", "output_filename": "label_oomp.svg"})

    templates_2 = []
    for template in templates:
        template_folder = template.get("template_folder", "")
        if template_folder == "default":
            templates_2.extend(template_root_defaults)
        else:
            templates_2.append(template)
    templates = templates_2

    for template in templates:
        template_folder = template.get("template_folder", "")
        template_folder = template_folder.replace("/", os.sep).replace("\\", os.sep)        
        template_file_base = template.get("template_file", "working.svg.j2")
        template_file = os.path.join(template_folder, template_file_base)

        

        output_filename = template.get("output_filename", "")
        

        directory = part.get("directory", oomlout_roboclick.get_directory(part))
        os.makedirs(directory, exist_ok=True)
        file_output = os.path.join(output_filename)

        action_type = "ai"
        action_name = f"step_{count}_jinja_template_{output_filename}"
        file_test = output_filename

        actions = []

        action={}
        action["command"] = "jinja_template"
        action["file_template"] = template_file
        action["file_output"] = file_output
        action["dict_data"] = part
        action["search_and_replace"] = template.get("search_and_replace", [])
        action["convert_to_pdf"] = convert_to_pdf
        action["convert_to_png"] = convert_to_png
        actions.append(action)

        oomlout_roboclick.add_action(
            part=part,
            action_type=action_type,
            action_name=action_name,
            actions=actions,
            file_test=file_test,
        )
        count += 1

    return count
