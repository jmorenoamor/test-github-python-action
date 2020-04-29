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

	print("::warning file=app.js,line=1,col=5::Missing semicolon")
	print("::debug file=app.js,line=1::Entered octocatAddition method")
	print("::error file=app.js,line=10,col=15::Something went wrong")

if __name__ == "__main__":

    logger = logging.getLogger(__name__)

    main()

    logger.debug("Debug message")
    logger.info("Debug message")
    logger.error("Debug message")
