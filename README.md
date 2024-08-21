# Illumio Coding Exercise

## Description
This Python program parses a file containing flow log data and maps each row to a tag based on a lookup table. The program generates two output files:
- `tag_counts.csv`: Contains the count of matches for each tag.
- `port_protocol_counts.csv`: Contains the count of matches for each port/protocol combination.

## Assumptions
- The program only supports the default log format provided in the exercise.
- Only flow logs with version 2 are supported.
- Protocol numbers are mapped to their respective names (e.g., `6` for TCP, `17` for UDP).
- The lookup table is case-insensitive and must be provided in the correct format.
- Entries in the flow log that do not match the lookup table are tagged as `Untagged`.

## Files Included
- `main.py`: The main Python script that performs the parsing and tagging.
- `lookup_table.csv`: The lookup table used for mapping port/protocol combinations to tags.
- `flow_log.txt`: Sample flow log data to be parsed.
- `tag_counts.csv`: Output file with tag counts.
- `port_protocol_counts.csv`: Output file with port/protocol combination counts.

## How to Run the Program

### Prerequisites
- Python 3.x installed on your local machine.

### Steps to Run
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/IllumioCodingExercise.git
    ```
2. Navigate to the project directory:
    ```bash
    cd IllumioCodingExercise
    ```
3. Run the program:
    ```bash
    python main.py
    ```
4. The output files (`tag_counts.csv` and `port_protocol_counts.csv`) will be generated in the same directory.

## Testing
- The program was tested with various flow log entries to ensure that the tags were correctly assigned and unmatched entries were tagged as `Untagged`.
- Edge cases, such as missing or malformed log lines, were handled by skipping those lines with appropriate logging.

## Analysis
- The program is designed to be lightweight and easy to run on any local machine with Python installed. No external libraries were used to ensure compatibility and ease of use, as per the requirements.
- The logic is straightforward and easy to follow, making it simple to expand the program for further upgrades if needed in the future.
