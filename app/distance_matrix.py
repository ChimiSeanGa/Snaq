import googlemaps

from .config import GOOG_API_KEY

"""Returns number of meters between origin and destinatation."""
def distance_matrix(origin, destination):
    # FIXME: add error checks; see if response time can be reduced
    gmaps = googlemaps.Client(key=GOOG_API_KEY)
    result = gmaps.distance_matrix(origin, destination)
    return result['rows'][0]['elements'][0]['distance']['value']
