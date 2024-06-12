class AnyText_Kevin:
  def __init__( self ):
    pass

  @classmethod
  def INPUT_TYPES( cls ):
    return {
      "required": {
        "text1": ("STRING", { "default": 'Kevin' }),
        "text2": ("STRING", {"forceInput": True} )
      }
    }

  RETURN_TYPES = ("IMAGE",)
  FUNCTION = "test"
  TITLE = "AnyText-Kevin"

  CATEGORY = "AnyText-kevin"

  def test( self ):
    return "test"

NODE_CLASS_MAPPINGS = {
  "AnyText_Kevin": AnyText_Kevin
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyText_Kevin": "AnyText-Kevin"
}
