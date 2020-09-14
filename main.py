"""Main program.
"""
import warnings

import log

logger = log.get_logger(__name__)


warnings.simplefilter(action="ignore", category=FutureWarning)

if __name__ == "__main__":

    logger.info("Start application.")

    try:

        pass

    except:
        logger.exception("Got exception on main handler")
        raise

    logger.info("Stop application.")
