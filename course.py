class Course(object):
    def __init__(self,
                 period=None,
                 name=None,
                 teacher_name=None,
                 resource_name=None,
                 resource_url=None):
        self.period = period
        self.name = name
        self.teacher_name = teacher_name
        self.resource_name = resource_name
        self.resource_url = resource_url