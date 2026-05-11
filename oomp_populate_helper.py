import copy
import os

import yaml


def _normalize_oomp_id_segment(value):
    return str(value).strip().replace(" ", "_").replace(".", "_")


def build_oobb_entry(input_dict):
    oomp_id_item = build_oomp_id(input_dict)
    new_dict = copy.deepcopy(input_dict)
    oobb_details = {}
    # "" out all taxonomy 1-17
    for i in range(1, 18):
        new_dict[f"taxonomy_{i}"] = ""
    # redefine start with oobb
    count = 1
    new_dict[f"taxonomy_{count}"] = "oobb"
    count += 1
    name = input_dict.get("oobb_name", "")
    if name:
        new_dict[f"taxonomy_{count}"] = name
        oobb_details["oobb_name"] = name
        count += 1
    width = input_dict.get("width", 1)
    new_dict[f"taxonomy_{count}"] = f"{width}_width"
    oobb_details["width"] = width
    count += 1
    height = input_dict.get("height", 1)
    new_dict[f"taxonomy_{count}"] = f"{height}_height"
    oobb_details["height"] = height
    count += 1
    depth = input_dict.get("depth", 1)
    new_dict[f"taxonomy_{count}"] = f"{depth}_depth"
    oobb_details["thickness"] = depth
    count += 1
    extra = input_dict.get("extra", "")
    if extra:
        new_dict[f"taxonomy_{count}"] = extra
        oobb_details["extra"] = extra
        count += 1
    test_id = build_oomp_id(new_dict)
    max_length = 200
    length_total = len(test_id) + len(oomp_id_item) + 1
    oomp_id_include = oomp_id_item
    if length_total > max_length:
        excess_length = length_total - max_length
        oomp_id_include = oomp_id_item[:-excess_length]
    new_dict[f"taxonomy_{count}"] = oomp_id_include
    new_dict["oobb_details"] = oobb_details
    for key in ["width", "height", "depth", "oobb_name", "extra"]:
        new_dict.pop(key, None)
    return new_dict


def write_extras(extras, default_input={}):
    for input_dict in extras:
        oobb = input_dict.get("oobb", False)
        if oobb:
            input_dict = build_oobb_entry(input_dict)

        details = copy.deepcopy(default_input)
        details.update(input_dict)
        oomp_id = build_oomp_id(details)
        if not oomp_id:
            oomp_id = "default_empty"
        folder_path = os.path.join("parts_source", oomp_id)
        os.makedirs(folder_path, exist_ok=True)
        yaml_path = os.path.join(folder_path, "working.yaml")
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(details, f, allow_unicode=True)
        filenames = ["datasheet.pdf", "image.jpg", "diagram.af"]
        oomp_id = build_oomp_id(details)
        for filename in filenames:
            source_path = os.path.join("source_file", f"{oomp_id}_{filename}")
            if os.path.exists(source_path):
                dest_path = os.path.join(folder_path, filename)
                if not os.path.exists(dest_path):
                    with open(source_path, "rb") as src_file:
                        with open(dest_path, "wb") as dst_file:
                            dst_file.write(src_file.read())


def build_oomp_id(d):
    for i in range(1, 16):
        if f"taxonomy_{i}" not in d:
            d[f"taxonomy_{i}"] = ""
    fields = []

    for i in range(1, 16):
        v = d.get(f"taxonomy_{i}", "")
        fields.append(v)
    return_value = "_".join([_normalize_oomp_id_segment(f) for f in fields if f])
    return return_value
