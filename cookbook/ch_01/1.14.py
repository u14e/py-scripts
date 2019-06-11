# @Author: u14e
# @Time  : 2019/3/2 11:41
# @description: 排序对象


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def run():
    print(sorted(users, key=lambda u: u.user_id))

    from operator import attrgetter
    print(sorted(users, key=attrgetter('user_id')))


if __name__ == '__main__':
    users = [User(23), User(3), User(99)]
    run()
