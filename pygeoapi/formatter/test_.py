from pygeoapi.formatter.base import BaseFormatter, FormatterSerializationError

class TestFormatter(BaseFormatter):
    """Test plugin formatter"""

    def __init__(self, formatter_def: dict):
        """
        Initialize object

        :param formatter_def: formatter definition

        :returns: `pygeoapi.formatter.csv_.TestFormatter`
        """

        geom = False
        if 'geom' in formatter_def:
            geom = formatter_def['geom']

        super().__init__({'name': 'test', 'geom': geom})
        self.mimetype = ' application/zip;'