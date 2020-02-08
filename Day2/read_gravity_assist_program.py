def read_gravity_assist_program(filename):
    input_file = open(filename, "r")
    gravity_assist_program_csv = input_file.read().replace('\n', '')
    gravity_assist_program_list_of_strings = str.split(gravity_assist_program_csv, ",")
    gravity_assist_program_list_of_ints = [int(x) for x in gravity_assist_program_list_of_strings]
    return(gravity_assist_program_list_of_ints)
