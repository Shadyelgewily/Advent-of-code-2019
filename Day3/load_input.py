def load_wires(filename):
    input_file = open(filename, "r")
    wires = []
    for wire in input_file:
        wires_csv = wire.replace('\n', '')
        wires.append( wires_csv.split(",") )

    return(wires)