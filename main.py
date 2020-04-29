import os
import sys
import logging

def main():

    input_parameter = os.getenv("INPUT_PARAMETER")

    print("::debug::Debug message to action")
    print("::warning::Warning message to action")
    print("::error::Error message to action " + input_parameter)

    print("::set-output name=result::OK")

if __name__ == "__main__":

    logger = logging.getLogger(__name__)

    main()

    logger.debug("Debug message")
    logger.info("Info message")
    logger.error("Error message")
