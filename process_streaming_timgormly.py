# import libraries

import csv
import logging
import socket
import time
import random


# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Set up constants
HOST = 'localhost'
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = 'salaries.csv'
OUTPUT_FILE_NAME = "out9.txt"


# function definitions
def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""
    work_year,experience_level,employment_type,job_title,salary_in_usd,company_size = row
    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{work_year},{experience_level},{employment_type},{job_title},{salary_in_usd},{company_size}]"

    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()
    logging.debug(f"Prepared message: {fstring_message}")
    return MESSAGE



def stream_data(input_file_name, output_file_name, address_tuple):
    # open file for writing
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        reader = csv.reader(input_file)

        # create header from first row before entering for loop for remaining time
        header = next(reader)
        output_file.write(','.join(header) + '\n')
        
        sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


        for row in reader:
            # prepare a binary encoded message using prepare_message_from_row()
            message = prepare_message_from_row(row)

            # send message to address tuple via socket
            sock_object.sendto(message, address_tuple)
            
            # write message to output file
            output_file.write(','.join(row) + '\n')

            # delay at a random interval before next loop
            time.sleep(random.uniform(1, 3))  # Random sleep between 1-3 seconds

if __name__ == "__main__":
    try:
        print("Starting data streaming.")
        stream_data(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)
        print("Streaming complete!")
    except Exception as e:
        print(f"An error occurred: {e}")