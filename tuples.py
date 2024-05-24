def get_coordinate(record):
    tesoro,coordenada = record
    return coordenada
#print(get_coordinate(('Scrimshawed Whale Tooth','2A')))
#print(get_coordinate(('Silver Seahorse','4E')))

def convert_coordinate(coordinate):
    coordinate = tuple(coordinate)
    return coordinate
#print(convert_coordinate("2A"))

def create_record(azara_record, rui_record):
    tesoro, coord1 = azara_record
    ubi, coord2, cuad = rui_record
    num, let = coord2
    coord3 = num+let
    if coord1 == coord3:
        return (tesoro,coord1,ubi,coord2,cuad)
    else:
        return "not a match"
#print(create_record(('Brass Spyglass','4B'),('Abandoned Lighthouse',('4','B'),'Blue')))
#print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
