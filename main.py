import csv
from collections import defaultdict


# Function to load the lookup table from a CSV file
def load_lookup_table(filepath):
    lookup_table = {}
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['dstport'], row['protocol'].lower())
            lookup_table[key] = row['tag']
    return lookup_table


# Protocol number to name mapping
protocol_mapping = {
    "6": "tcp",
    "17": "udp"
}


# Updated parsing logic to use protocol names
def parse_flow_logs(log_filepath, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(log_filepath, mode='r') as file:
        for line in file:
            line = line.strip()  # Strip leading and trailing whitespace

            # Skip empty lines
            if not line:
                continue

            parts = line.split()

            # Ensure the line has at least 8 parts
            if len(parts) < 8:
                print(f"Skipping invalid line: {line}")
                continue

            dstport = parts[5]
            protocol_num = parts[7]
            protocol = protocol_mapping.get(protocol_num,
                                            protocol_num)  # Use the mapped name or the number if not found
            key = (dstport, protocol.lower())

            # Map the row to a tag using the lookup table
            tag = lookup_table.get(key, 'Untagged')
            tag_counts[tag] += 1

            # Count the port/protocol combination
            port_protocol_counts[key] += 1

    return tag_counts, port_protocol_counts


# Function to write the output to files
def write_output(tag_counts, port_protocol_counts, tag_output_filepath, port_protocol_output_filepath):
    # Write Tag Counts
    with open(tag_output_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])

    # Write Port/Protocol Combination Counts
    with open(port_protocol_output_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])


# Main function to run the program
def main():
    # File paths
    lookup_table_filepath = 'lookup_table.csv'
    flow_log_filepath = 'flow_log.txt'
    tag_output_filepath = 'tag_counts.csv'
    port_protocol_output_filepath = 'port_protocol_counts.csv'

    # Load the lookup table
    lookup_table = load_lookup_table(lookup_table_filepath)

    # Parse the flow logs and map to tags
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_filepath, lookup_table)

    # Write the results to output files
    write_output(tag_counts, port_protocol_counts, tag_output_filepath, port_protocol_output_filepath)


# Run the program
if __name__ == "__main__":
    main()
