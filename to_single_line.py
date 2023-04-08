def transform_regex_file_to_single_line(filename, new_filename):
    # the file is in ascii encoding where each line contains a pcre regex.
    # we want to transform it to a single line with all the regexes separated by one space.

    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [ line for line in lines if line]
        lines = ' '.join(lines)
        with open(new_filename, 'w') as f:
            f.write(lines)

if __name__ == "__main__":
    import os
    transform_regex_file_to_single_line(os.path.join(".","YARA","rules","YARA_rules.txt"), os.path.join(".","YARA","rules","YARA_rules.single_line.txt"))
    transform_regex_file_to_single_line(os.path.join(".","YARA","rules","YARA_wide_rules.txt"), os.path.join(".","YARA","rules","YARA_wide_rules.single_line.txt"))

    transform_regex_file_to_single_line(os.path.join(".","Snort","rules","snort.regex"), os.path.join(".","Snort","rules","snort.single_line.regex"))

    transform_regex_file_to_single_line(os.path.join(".","Protomata","rules","protomata.regex"), os.path.join(".","Protomata","rules","protomata.single_line.regex"))

    transform_regex_file_to_single_line(os.path.join(".","ClamAV","rules","daily-24356.pcre"), os.path.join(".","ClamAV","rules","daily-24356.single_line.pcre"))

    transform_regex_file_to_single_line(os.path.join(".","Brill","rules","regex.txt"), os.path.join(".","Brill","rules","regex.single_line.txt"))



