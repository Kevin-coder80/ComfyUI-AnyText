from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

class AnyText_Kevin:
  def __init__( self ):
    pass

  @classmethod
  def INPUT_TYPES( cls ):
    return {
      "required": {
        "prompt": ("STRING", {"default": "A cake with colorful characters that reads \"EVERYDAY\"", "multiline": True}),
        "mode": (["text-generation"],),
        "image_count": ("INT", {"default": 2, "min": 1, "max": 10}),
        "ddim_steps": ("INT", {"default": 20, "min": 1, "max": 100}),
        "show_debug": ("BOOLEAN", {"default": True}),
        "seed": ("INT", {"default": 0, "min": 0, "max": 99999999}),
        "draw_pos": ("IMAGE",),
      }
    }

  RETURN_TYPES = ("IMAGE",)
  FUNCTION = "test"
  TITLE = "AnyText-Kevin"

  CATEGORY = "AnyText-kevin"

  def test( self, prompt, mode, image_count, ddim_steps, show_debug, seed, draw_pos ):
    print(f"Tasks: {Tasks.translation}")
    ckpt = '/home/liuwei/ai/ComfyUI/models/prompt_generator/nlp_csanmt_translation_zh2en'
    pipe = pipeline(task=Tasks.translation, model='damo/cv_anytext_text_generation_editing', model_revision='v1.1.3', use_fp16=True, use_translator=False, device="cuda")

    print(f"prompt: {prompt}")
    print(f"pipeline: {pipeline}")

    self.params = {
      "show_debug": show_debug,
      "image_count": image_count,
      "ddim_steps": ddim_steps,
    }

    input_data = {
      "prompt": prompt,
      "seed": seed,
      "draw_pos": '/home/liuwei/ai/ComfyUI/input/00078-2449976921.png'
      # "draw_pos": draw_pos
    }

    results, rtn_code, rtn_warning, debug_info = pipe(input_data, mode='text-generation', **self.params)

    print(f"results: {results}")
    print(f"rtn_code: {rtn_code}")
    print(f"rtn_warning: {rtn_warning}")

    if rtn_code < 0:
        raise Exception(f"Error in AnyText pipeline: {rtn_warning}")

    return results

NODE_CLASS_MAPPINGS = {
  "AnyText_Kevin": AnyText_Kevin
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyText_Kevin": "AnyText-Kevin"
}
