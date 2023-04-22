import uuid


class User(object):
    def __init__(self, name, age, skills, uid=None):
        if not uid:
            self.uid = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.skills = skills

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'skills': self.skills,
            'id': self.uid
        }

    @staticmethod
    def from_dict(self, **kv):
        uid = kv.get('id')
        if not id:
            return None
        name = kv.get('name')
        age = kv.get('age')
        skills = kv.get('skills')

        return User(name, age, skills, uid=uid)

