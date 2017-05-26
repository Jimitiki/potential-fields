import fields
import robot
import commands
from time import sleep

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

goal = markers[str(20)]["center"]
r_field1 = markers[str(21)]["center"]
r_field2 = markers[str(23)]["center"]
r_field3 = markers[str(24)]["center"]
r_field4 = markers[str(25)]["center"]
f = fields.field_holder()
f.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(goal[0], goal[1]), 11))
f.add_field(fields.linear_counterclockwise_tangential_field(fields.fixed_position_tracker(r_field1[0], r_field1[1]), 800, 6))
f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(r_field2[0], r_field2[1]), 1000, 4))
f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(r_field3[0], r_field3[1]), 1000, 4))
f.add_field(fields.linear_counterclockwise_tangential_field(fields.fixed_position_tracker(r_field4[0], r_field4[1]), 1400, 5))
yes = 1
while yes > 0:
    res = commands.where_robot()
    if "center" in res:
        position = commands.where_robot()["center"]
        vector = f.get_field(position[0], position[1])
        yes = robot.follow_vector(vector[0], vector[1], goal)

commands.close_connection()
