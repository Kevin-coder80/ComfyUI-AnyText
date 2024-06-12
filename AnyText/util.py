class AnyText_Kevin:
  def __init__( self ):
    pass

  @classmethod
  def INPUT_TYPES( cls ):
    return {
      "required": {}
    }

  RETURN_TYPES = {}
  RETURN_NAMES = {}
  FUNCTION = "test"

  CATEGORY = "image/AnyText_kevin"

  def test( self ):
    return "test"

NODE_CLASS_MAPPINGS = {
  "AnyText_Kevin": AnyText_Kevin
}

NODE_DISPLAY_NAME_MAPPINGS = {
  "FirstNode": "My first node"
}
