class Arguments:
    indent_length = 4

    def __init__(self, title=""):
        self.title = title
        self.inst_fields = {}

    def __str__(self):
        lines = ()
        lines += (f'class {self.title}',)
        tab = ' ' * self.__class__.indent_length
        if self.inst_fields:
            lines += (f'{tab}def __init__(self):',)
            for name, value in self.inst_fields.items():
                lines += (f'{tab * 2}{name} = {value}',)
        else:
            lines += (f'{tab}pass',)
        return '\n'.join(lines)


class ClassBuilder:
    def __init__(self):
        self.arguments = Arguments()

    def build(self):
        return self.arguments


class NameBuilder(ClassBuilder):
    def person_name(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


class AgeBuilder(NameBuilder):
    def person_age(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


class1 = AgeBuilder() \
    .person_age("age", "26") \
    .person_name("name", "Vusal") \
    .build()

print(class1)
