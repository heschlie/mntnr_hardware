"""
Connexion does type validation for all the OpenAPI v2 data types, so we don't
need to do it here. See https://goo.gl/tuEhoz for a list of these data types
and how they map to the OpenAPI schema.

The fields defined on the serializers below simply as 'field' rely on connexion
for type validation via the OpenAPI schema.  Validating again at the serializer
level would only incur unnecessary overhead.

"""


from functools import partial

from strainer import (child, field, serializer)

from mountaineer.strain import email_validator, enum_formatter, enum_validator, url_validator, uuid_validator
from mntnr_hardware.models import CabinetAttachmentEnum, CabinetFastenerEnum


uuid_field = partial(field, validators=[uuid_validator()])
enum_field = partial(field, formatters=[enum_formatter()])


datacenter_serializer = serializer(
    uuid_field('id'),
    field('name'),
    field('vendor'),
    field('address'),
    field('noc_phone'),
    field('noc_email', validators=[email_validator()]),
    field('noc_url', validators=[url_validator()])
)


datacenter_embedded_serializer = serializer(
    uuid_field('id'),
    field('name')
)


cabinet_serializer = serializer(
    uuid_field('id'),
    field('name'),
    child('datacenter', serializer=datacenter_embedded_serializer),
    field('rack_units'),
    field('depth'),
    field('width'),
    enum_field('attachment', validators=[enum_validator(enum=CabinetAttachmentEnum)]),
    enum_field('fasteners', validators=[enum_validator(enum=CabinetFastenerEnum)])
)

