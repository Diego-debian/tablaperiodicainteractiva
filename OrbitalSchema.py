from marshmallow import Schema, fields

class OrbitalSchema(Schema):
    s = fields.Int()
    p = fields.Int()
    d = fields.Int()
    f = fields.Int()

class ElementoSchema(Schema):
    number = fields.Int(required=True)
    symbol = fields.Str(required=True)
    name = fields.Str(required=True)
    category = fields.Str()
    group = fields.Int()
    period = fields.Int()
    atomic_mass = fields.Float()
    electron_config = fields.Str()
    orbitals = fields.Nested(OrbitalSchema)
    discovery = fields.Int()
    discoverer = fields.Str()
    density = fields.Float()
    melt = fields.Float()
    boil = fields.Float()
    phase = fields.Str()
    summary = fields.Str()