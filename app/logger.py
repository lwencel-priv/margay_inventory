"""Main logger."""

import logging

# create logger
main_logger = logging.getLogger("MAIN")
main_logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s]: %(message)s")

# add formatter to ch
stream_handler.setFormatter(formatter)

# add ch to logger
main_logger.addHandler(stream_handler)