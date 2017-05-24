import fields
import robot
import commands

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

goal = commands.where_markers()[str(20)]["center"]
f = fields.field_holder()
f.add_field(fields.constant_repulsive_field(fields.fixed_position_tracker(goal[0], goal[1]), 200, 10))
yes = 1
while yes > 0:
    res = commands.where_robot()
    if "center" in res:
        position = commands.where_robot()["center"]
        vector = f.get_field(position[0], position[1])
        yes = robot.follow_vector(vector[0], vector[1])

commands.close_connection()
