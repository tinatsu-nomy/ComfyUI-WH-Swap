class WidthHeightSwap:
    """
    Simple Width / Height INT passthrough node.

    The actual swap operation is handled by the frontend JavaScript,
    which swaps the widget values before the workflow is queued.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": (
                    "INT",
                    {
                        "default": 1024,
                        "min": 1,
                        "max": 16384,
                        "step": 1,
                    },
                ),
                "height": (
                    "INT",
                    {
                        "default": 1024,
                        "min": 1,
                        "max": 16384,
                        "step": 1,
                    },
                ),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"
    CATEGORY = "utils/size"

    def get_size(self, width, height):
        return (int(width), int(height))


NODE_CLASS_MAPPINGS = {
    "WidthHeightSwap": WidthHeightSwap,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WidthHeightSwap": "Width / Height Swap",
}
