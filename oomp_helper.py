import copy
import glob
import os
from pathlib import Path

import oomlout_roboclick

##C:\gh\oomlout_oomp_version_5\prompts
PROMPT_ROOT = Path(__file__).resolve().parent / "prompts"
IMAGE_GENERATE_PROMPT = "Generate the image take all the time you need"


class _SafePromptDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"


def get_prompt_directories(prompt_root=PROMPT_ROOT):
    prompt_root = Path(prompt_root)
    if not prompt_root.exists():
        return []

    prompt_folders = []
    for child in sorted(prompt_root.iterdir(), key=lambda item: item.name.lower()):
        if not child.is_dir():
            continue
        if next(child.glob("working_*.md"), None) is None:
            continue
        prompt_folders.append(child.name)
    return prompt_folders


def _resolve_prompt_image_detail(part, image_detail=""):
    detail = str(image_detail or part.get("name_space", "")).strip()
    return detail


def _prompt_action_name(count, prompt_folder):
    prompt_name = Path(prompt_folder).name
    return f"step_{count}_create_{prompt_name}"


def _prompt_file_name(prompt_folder):
    prompt_name = Path(prompt_folder).name
    return f"initial_generated_{prompt_name}.png"


def _load_prompt_directory(prompt_folder, prompt_values=None):
    prompt_values = prompt_values or {}
    prompt_directory = Path(prompt_folder)
    if not prompt_directory.is_absolute():
        prompt_directory = PROMPT_ROOT / prompt_directory

    prompts = []
    for i in range(1, 50):
        prompt_file = prompt_directory / f"working_{i}.md"
        if not prompt_file.exists():
            break

        prompt_text = prompt_file.read_text(encoding="utf-8")
        prompt_text = prompt_text.format_map(_SafePromptDict(prompt_values))
        prompts.append({"text": prompt_text, "delay": "120"})

    if not prompts:
        raise FileNotFoundError(f"No prompt files found in {prompt_directory}")

    return prompts


def add_image_from_prompt_directory(
    part,
    count,
    prompt_folder,
    file_name,
    action_name,
    mode_ai_wait="slow",
    prompt_values=None,
    generate_prompt=IMAGE_GENERATE_PROMPT,
):
    prompt_data = copy.deepcopy(part)
    if prompt_values:
        prompt_data.update(prompt_values)

    prompts = _load_prompt_directory(prompt_folder, prompt_data)
    prompts.append(
        {
            "file_name_image": file_name,
            "text": generate_prompt,
            "delay": "120",
        }
    )

    part2 = copy.deepcopy(part)
    return oomlout_roboclick.ai_query_from_prompts(
        part=part,
        part2=part2,
        prompts=prompts,
        mode_ai_wait=mode_ai_wait,
        count=count,
        action_name=action_name,
    )


def _add_default_prompt_image(part, count, prompt_folder, mode_ai_wait="slow", image_detail=""):
    return add_image_from_prompt_directory(
        part=part,
        action_name=_prompt_action_name(count, prompt_folder),
        count=count,
        prompt_folder=prompt_folder,
        file_name=_prompt_file_name(prompt_folder),
        mode_ai_wait=mode_ai_wait,
        prompt_values={"image_detail": _resolve_prompt_image_detail(part, image_detail)},
    )


def add_image_birthday_banner_frame_vector(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_birthday_banner_frame_vector",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image_birthday_clipart_vector_pack(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_birthday_clipart_vector_pack",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image_birthday_icon_badge_vector(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_birthday_icon_badge_vector",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image_birthday_pattern_repeat_vector(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_birthday_pattern_repeat_vector",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image_enamel_pin_design(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_enamel_pin_design",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image_laser_cut_logo_full(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_laser_cut_logo_full",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image_sticker_design_vinyl(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_sticker_design_vinyl",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_all_default_prompt_images(
    part,
    count,
    mode_ai_wait="slow",
    image_detail="",
    prompt_folders=None,
):
    prompt_folders = prompt_folders or get_prompt_directories()
    for prompt_folder in prompt_folders:
        count = _add_default_prompt_image(
            part=part,
            count=count,
            prompt_folder=prompt_folder,
            mode_ai_wait=mode_ai_wait,
            image_detail=image_detail,
        )
    return count


def add_all_prompt_directories(part, count, mode_ai_wait="slow", image_detail="", prompt_folders=None):
    return add_all_default_prompt_images(
        part=part,
        count=count,
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
        prompt_folders=prompt_folders,
    )


def add_icon(part, count, mode_ai_wait="slow", icon_detail=""):
    action_name = f"step_{count}_create_icon"
    detail = f'{part.get("name_space", "")} {icon_detail}'.strip()
    image_detail = f"an image of {detail}"

    return add_image_from_prompt_directory(
        part=part,
        action_name=action_name,
        count=count,
        prompt_folder="image_laser_cut_logo_full",
        file_name="initial_generated_icon.png",
        mode_ai_wait=mode_ai_wait,
        prompt_values={"image_detail": image_detail},
    )


def add_image_chibi(part, count, mode_ai_wait="slow", chibi_detail=""):
    action_name = f"step_{count}_create_image_chibi"
    detail = f'{part.get("name_space", "")} {chibi_detail}'.strip()
    image_detail = f"a fun chibi CGI inspired picture of {detail}"

    return add_image_from_prompt_directory(
        part=part,
        action_name=action_name,
        count=count,
        prompt_folder="image_chibi_cgi_fun",
        file_name="initial_generated_chibi.png",
        mode_ai_wait=mode_ai_wait,
        prompt_values={"image_detail": image_detail},
    )


def add_image_chibi_cgi_fun(part, count, mode_ai_wait="slow", image_detail=""):
    return _add_default_prompt_image(
        part=part,
        count=count,
        prompt_folder="image_chibi_cgi_fun",
        mode_ai_wait=mode_ai_wait,
        image_detail=image_detail,
    )


def add_image(part, folder_project, files_to_trace, mode_ai_wait, count):
    words = part.get("words", [])
    prompts = []
    prompts.append(
        {
            "folder_name": f"roboclick\\{folder_project}\\prompt_three_dimension_letter_two_line_1",
            "delay": "120",
        }
    )

    for i, word in enumerate(words):
        prompts.append({"text": f'Awesome fill in the json template with "{word}"'})
        file_name = f"initial_generated_{i + 1}.png"
        prompts.append(
            {
                "file_name_image": file_name,
                "text": "Generate the image take all the time you need",
                "delay": "120",
            }
        )
        files_to_trace.append(file_name)

    part2 = copy.deepcopy(part)
    return oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)


def add_prompt_image(part, folder_project, prompt_folder, file_name, files_to_trace, mode_ai_wait, count):
    prompts = []
    prompts.append({"folder_name": f"roboclick\\{folder_project}\\{prompt_folder}", "delay": "120"})
    prompts.append(
        {
            "file_name_image": file_name,
            "text": "Generate the image take all the time you need",
            "delay": "120",
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
    prompts.append({"folder_name": f"roboclick\\{folder_project}\\prompt_image_background_1", "delay": "120"})
    file_name = "image_cover_background.png"
    prompts.append(
        {
            "file_name_image": file_name,
            "text": "Generate the image take all the time you need",
            "delay": "120",
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
    #template_root_defaults.append({"template_folder": "source_file\\template_jinja\\template_jinja_postcard_oomlout_101_6_mm_152_4_mm", "output_filename": "postcard_oomp.svg"})
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
        file_test = output_filename.replace(".svg", ".pdf")

        actions = []

        action={}
        action["command"] = "text_jinja_template"
        action["file_template"] = template_file
        action["file_output"] = file_output
        action["dict_data"] = copy.deepcopy(part)
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
