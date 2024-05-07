import re
import requests
import validators
from pathlib import Path
from markmoji import handlers


class HexmapHandler(handlers.MarkmojiHandler):
    """
    Handler for creating a hexagonal map using tiles from 
    [Cuddly Clover on itch.io](https://cuddlyclover.itch.io/fantasy-hex-tiles).

    ### Parameters
    label (str)
    :    Title for the map

    file (str)
    :    Path or link to a csv file created via [Hexmap by Todd Parsons](https://teparsons.github.io/Hexmap/)
    """
    # Hexagon emoji because HEXmap
    emoji = "⬢"
    requirements = "<script src='https://teparsons.github.io/Hexmap/hex.js' async='async'></script>"

    example = "⬢[Kashar](https://teparsons.github.io/Iuncterra/assets/locations/kashar/Kashar.csv)"
    __author__ = "🦊"

    @property
    def html(self):
        # Load data
        if validators.url(self.link):
            data = requests.get(self.link).text
        elif Path(self.link).is_file():
            data = Path(self.link).read_text()
        else:
            data = self.link
        # Construct hexmap
        return (
            f"<h3>{self.label}</h3>\n"
            f"<hex-grid data-tiles='{data}' data-readonly{self.html_params}></hex-grid>\n"
        )


class IPAHandler(handlers.MarkmojiHandler):
    """
    Handler to format text written in International Phonetic Alphabet, adding a link to ipa-reader.xyz
    
    
    #### Parameters
    label (str)
    :    Text to display.

    link (str)
    :    IPA text to pronounce in ipa-reader.xyz. Leave blank to use text from label.
    """
    # Person speaking emoji, because it's a pronunciation guide
    emoji = "🗣️"

    example = "🗣️<aɪpʰieɪ>"
    __author__ = "🦊"

    @property
    def html(self):
        # Get link (use label if none)
        link = self.link
        if not link:
            link = self.label
        # Return in link
        return f"<a class='IPA' href='http://ipa-reader.xyz/?text={self.link}'{self.html_params}>{self.label}</a>"
