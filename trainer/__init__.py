from PM import DB_Action


for i in range(1,50):
    DB_Action.removeUserByUserNamer("user{0}".format(i))
    DB_Action.removeUserByUserNamer("trainer{0}".format(i))
    DB_Action.removeUserByUserNamer("admin{0}".format(i))

