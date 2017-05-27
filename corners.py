import fields
import robot
import waypoints
import commands
from time import sleep

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

a_field1 = markers[str(20)]["center"]
a_field2 = markers[str(22)]["center"]
a_field3 = markers[str(24)]["center"]
a_field4 = markers[str(27)]["center"]
a_field5 = markers[str(26)]["center"]

r_field = markers[str(25)]["center"]

f = fields.field_holder()
w = waypoints.waypoints(f)

w.add_waypoint(a_field2[0], a_field2[1], 8)
w.add_waypoint(a_field1[0], a_field1[1], 8)
w.add_waypoint(a_field3[0], a_field3[1], 8)
w.add_waypoint(a_field4[0], a_field4[1], 8)

f.add_field(fields.constant_attractive_field(fields.fixed_position_tracker(a_field5[0], a_field5[1]), 700, 4))

f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(r_field[0], r_field[1]), 700, 4))

#f.add_field(fields.random_field(1.2))

at_waypoint = False
while w.has_waypoint():
    res = commands.where_robot()
    if "center" in res:
        position = commands.where_robot()["center"]
        vector = f.get_field(position[0], position[1])
        at_waypoint = robot.follow_vector(vector[0], vector[1], w.get_waypoint())
        if at_waypoint:
            w.go_to_next_waypoint()

commands.close_connection()
