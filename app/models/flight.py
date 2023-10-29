from croydon.models.storable_model import StorableModel
from croydon.models.fields import StringField, ReferenceField
from croydon.util import uuid4_string
from .user import User


class Flight(StorableModel):

    COLLECTION = "flights"
    KEY_FIELD = "flight_id"

    flight_id = StringField(required=True, unique=True, default=uuid4_string)
    user_id: ReferenceField[User] = ReferenceField(reference_model=User, required=True)
