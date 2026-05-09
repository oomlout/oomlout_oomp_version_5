import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

if "oomlout_roboclick" not in sys.modules:
    sys.modules["oomlout_roboclick"] = types.SimpleNamespace(ai_query_from_prompts=None)

import oomp_helper


class PromptHelperTests(unittest.TestCase):
    def test_get_prompt_directories_filters_for_prompt_folders(self):
        prompt_directories = oomp_helper.get_prompt_directories()

        self.assertIn("image_birthday_banner_frame_vector", prompt_directories)
        self.assertIn("image_sticker_design_vinyl", prompt_directories)
        self.assertEqual(prompt_directories, sorted(prompt_directories, key=str.lower))

    def test_birthday_banner_wrapper_targets_its_folder(self):
        part = {"name_space": "maya birthday"}

        with patch.object(oomp_helper, "_add_default_prompt_image", return_value=8) as helper_mock:
            result = oomp_helper.add_image_birthday_banner_frame_vector(
                part=part,
                count=7,
                mode_ai_wait="fast",
                image_detail="star theme",
            )

        self.assertEqual(result, 8)
        helper_mock.assert_called_once_with(
            part=part,
            count=7,
            prompt_folder="image_birthday_banner_frame_vector",
            mode_ai_wait="fast",
            image_detail="star theme",
        )

    def test_add_all_default_prompt_images_discovers_and_runs_each_prompt(self):
        part = {"name_space": "maya birthday"}
        prompt_folders = [
            "image_birthday_banner_frame_vector",
            "image_sticker_design_vinyl",
            "image_enamel_pin_design",
        ]
        calls = []

        def fake_add_default_prompt_image(**kwargs):
            calls.append(kwargs)
            return kwargs["count"] + 1

        with patch.object(oomp_helper, "get_prompt_directories", return_value=prompt_folders):
            with patch.object(
                oomp_helper,
                "_add_default_prompt_image",
                side_effect=fake_add_default_prompt_image,
            ):
                result = oomp_helper.add_all_default_prompt_images(
                    part=part,
                    count=3,
                    mode_ai_wait="slow",
                    image_detail="star theme",
                )

        self.assertEqual(result, 6)
        self.assertEqual(
            [call["prompt_folder"] for call in calls],
            prompt_folders,
        )
        self.assertEqual([call["count"] for call in calls], [3, 4, 5])
        self.assertTrue(all(call["image_detail"] == "star theme" for call in calls))


if __name__ == "__main__":
    unittest.main()