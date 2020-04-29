import os
import sys
import logging

def main():

    my_input = os.getenv("INPUT_MYINPUT", "default")

    my_output = f"Probando Hello {my_input}"

    print(f"::set-output name=myOutput::{my_output}")
    print(f"::set-output name=myOutput::{my_output}")
    print(f"::set-output name=myOutput::{my_output}")

    print("::set-output name=myOutput::Test message")

if __name__ == "__main__":

    logger = logging.getLogger(__name__)

    main()

    logger.debug("Debug message")
    logger.info("Debug message")
    logger.error("Debug message")
