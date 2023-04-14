import os




def print_fsm_to_dot(filename, dot_filename):
    # to print fsm: "fsm -pl dot <fsm_file >dot_filename"
    os.system("fsm -pl dot <" + filename + " >" + dot_filename)

def convert_re_to_fsm(re_filename, fsm_filename):
    # to fsm: "re -p  -r pcre \pattern\ \pattern2\ >fsm_file" or "re -p  -r pcre <file_with_patterns >fsm_file"
    os.system("re -p  -r pcre <" + re_filename + " >" + fsm_filename)

def transform_fsm(fsm_filename, new_fsm_filename):
    # to transform fsm: "fsm -GEdm <fsm_file >fsm_file"
    # TODO: add support to iteration
    # TODO: accept argument and formulate the flag accordingly
    # -d Equivalent to -t determinise
    # -G Equivalent to -t glushkovise (position automata)
    # -E remove epsilons
    # -m Equivalent to -t minimise
    # -r Equivalent to -t revers
    os.system("fsm -GEdm <" + fsm_filename + " >" + new_fsm_filename)