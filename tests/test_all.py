from markmoji.tests import BaseHandlerTests
from markmoji_ttrpg.handlers import HexmapHandler, IPAHandler


class TestHexmapHandler(BaseHandlerTests):
    handler = HexmapHandler


class TestIPAHandler(BaseHandlerTests):
    handler = IPAHandler
