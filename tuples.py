"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    _, coordinate = record
    return coordinate


def convert_coordinate(coordinate: str):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return (coordinate[0], coordinate[1])


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    
    az_tesoro, az_coordenada = azara_record
    rui_ubicación, rui_coordenada, rui_cuadrante = rui_record

    if az_coordenada[0] != rui_coordenada[0] or az_coordenada[1] != rui_coordenada[1] :
        return "not a match"

    return (az_tesoro, az_coordenada, rui_ubicación, rui_coordenada, rui_cuadrante)
