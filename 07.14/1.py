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
    def __init__(self, arguments=None):
        if arguments is None:
            self.arguments = Arguments('Person')
        else:
            self.arguments = arguments

    @property
    def name(self):
        return NameBuilder(self.arguments)

    @property
    def age(self):
        return AgeBuilder(self.arguments)

    def build(self):
        return self.arguments


class NameBuilder(ClassBuilder):
    def __init__(self, arguments):
        super().__init__(arguments)


    def person_name(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


class AgeBuilder(ClassBuilder):
    def __init__(self, arguments):
        super().__init__(arguments)


    def person_age(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


class1 = ClassBuilder() \
    .name \
    .person_name("name", "Vusal") \
    .age \
    .person_age("age", "26") \
    .build()

print(class1)
