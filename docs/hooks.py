# docs/hooks.py

def fix_markdown_spacing(markdown, page, config, files):
    """
    Example hook: adjust spacing in markdown content.
    """
    import re
    # Replace multiple spaces with a single space
    return re.sub(r" {2,}", " ", markdown)
