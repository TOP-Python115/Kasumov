## ==========  1  ========== ##

## классы должны быть документированы
class Arguments:
    indent_length = 4
    
    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __init__(self, title=""):
        self.title = title
        self.inst_fields = {}

    def __str__(self):
        lines = ()
        ## в конце заголовка класса должно быть двоеточие
        lines += (f'class {self.title}',)
        tab = ' ' * self.__class__.indent_length
        if self.inst_fields:
            lines += (f'{tab}def __init__(self):', )
            for name, value in self.inst_fields.items():
                lines += (f'{tab * 2}{name} = {value}', )
        else:
            lines += (f'{tab}pass', )
        return '\n'.join(lines)


## классы должны быть документированы
class ClassBuilder:
    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __init__(self, arguments=None):
        if arguments is None:
            self.arguments = Arguments('Person')
        else:
            self.arguments = arguments

    ## свойства должны быть документированы и аннотированы (помимо self)
    @property
    def name(self):
        return NameBuilder(self.arguments)
    
    @property
    def age(self):
        return AgeBuilder(self.arguments)
    
    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def build(self):
        return self.arguments


## классы должны быть документированы
class NameBuilder(ClassBuilder):
    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __init__(self, arguments):
        super().__init__(arguments)

    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def person_name(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


## классы должны быть документированы
class AgeBuilder(ClassBuilder):
    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __init__(self, arguments):
        super().__init__(arguments)

    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def person_age(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


## в целом всё верно
## только напомню, что комбинированный строитель используется для многокомпонентных сложноструктурированных объектов; соответствено, отдельные классы строителей почти всегда подразумевают работу с несколькими атрибутами создаваемого объекта, либо с одним, но вложенным; а для одного простого атрибута создавать отдельный класс строителя смысла не имеет


class1 = ClassBuilder() \
    .name \
    .person_name("name", "Vusal") \
    .age \
    .person_age("age", "26") \
    .build()

print(class1)



## ==========  2  ========== ##

## классы должны быть документированы
class Arguments:
    indent_length = 4
    
    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
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


## классы должны быть документированы
class ClassBuilder:
    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __init__(self):
        self.arguments = Arguments()

    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def build(self):
        return self.arguments


## классы должны быть документированы
class NameBuilder(ClassBuilder):
    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def person_name(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


## классы должны быть документированы
class AgeBuilder(NameBuilder):
    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def person_age(self, field_name, field_value):
        self.arguments.inst_fields[field_name] = field_value
        return self


## не хватает TitleBuilder — как итог, у результирующего класса нет имени
## остальное верно


class1 = AgeBuilder() \
    .person_age("age", "26") \
    .person_name("name", "Vusal") \
    .build()

print(class1)
