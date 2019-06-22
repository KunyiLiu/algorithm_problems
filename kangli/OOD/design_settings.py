class TypedSettingKey(object):

    def __init__(self, name, type, *properties):
        self.name = name
        self._type = type
        self.properties = properties


a = TypedSettingKey("test", str, "private", "unique")
print(a.properties)
