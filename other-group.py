import fields
import robot
import waypoints
import commands
from time import sleep

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

goal = markers[str(4)]["center"]

field1 = markers[str(30)["center"]
field2 = markers[str(31)["center"]
field3 = markers[str(33)]["center"]

f = fields.field_holder()
w = waypoints.waypoints(f)

w.add_waypoint(goal[0], goal[1], 8)

f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(field1[0], field1[1]), 500, 2))
f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(field2[0], field2[1]), 500, 2))
f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(field3[0], field3[1]), 500, 2))

f.add_field(fields.random_field(1.6))

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
