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

    def test_step_two_image_flows_save_without_an_extra_query(self):
        image_flows = [
            (oomp_helper.add_image_chibi_cgi_fun, "initial_generated_image_chibi_cgi_fun.png"),
            (oomp_helper.add_image_laser_cut_logo_full, "initial_generated_image_laser_cut_logo_full.png"),
            (oomp_helper.add_image_chibi, "initial_generated_chibi.png"),
            (oomp_helper.add_icon, "initial_generated_icon.png"),
        ]
        for wrapper, file_name in image_flows:
            with self.subTest(wrapper=wrapper.__name__):
                with patch.object(
                    oomp_helper.oomlout_roboclick,
                    "ai_query_from_prompts",
                    return_value=6,
                ) as query_mock:
                    result = wrapper({"name_space": "fox"}, 5)

                self.assertEqual(result, 6)
                prompts = query_mock.call_args.kwargs["prompts"]
                self.assertEqual(len(prompts), 3)
                self.assertIn("Invoke the tool exactly once", prompts[1]["text"])
                self.assertEqual(
                    prompts[2],
                    {"file_name_image": file_name},
                )
                self.assertNotIn("file_name_image", prompts[1])

    def test_other_image_flows_keep_the_generation_query(self):
        with patch.object(
            oomp_helper.oomlout_roboclick,
            "ai_query_from_prompts",
            return_value=6,
        ) as query_mock:
            oomp_helper.add_image_birthday_banner_frame_vector(
                {"name_space": "test"}, 5, image_detail="fox"
            )

        prompts = query_mock.call_args.kwargs["prompts"]
        self.assertEqual(prompts[-1]["text"], oomp_helper.IMAGE_GENERATE_PROMPT)
        self.assertEqual(
            prompts[-1]["file_name_image"],
            "initial_generated_image_birthday_banner_frame_vector.png",
        )


if __name__ == "__main__":
    unittest.main()
