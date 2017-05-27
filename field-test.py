import fields
import robot
import waypoints
import commands
from time import sleep

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

goal_1 = markers[str(20)]["center"]
goal_2 = markers[str(21)]["center"]
#r_field1 = markers[str(21)]["center"]
#r_field2 = markers[str(23)]["center"]
#r_field3 = markers[str(24)]["center"]
#r_field4 = markers[str(25)]["center"]
f = fields.field_holder()
w = waypoints.waypoints(f)
w.add_waypoint(goal_1[0], goal_1[1])
w.add_waypoint(goal_2[0], goal_2[1])

#f.add_field(fields.linear_counterclockwise_tangential_field(fields.fixed_position_tracker(r_field1[0], r_field1[1]), 800, 6))
#f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(r_field2[0], r_field2[1]), 1000, 4))
#f.add_field(fields.linear_repulsive_field(fields.fixed_position_tracker(r_field3[0], r_field3[1]), 1000, 4))
#f.add_field(fields.linear_counterclockwise_tangential_field(fields.fixed_position_tracker(r_field4[0], r_field4[1]), 1400, 5))
yes = 1
while w.has_waypoint():
    res = commands.where_robot()
    if "center" in res:
        position = commands.where_robot()["center"]
        vector = f.get_field(position[0], position[1])
        yes = robot.follow_vector(vector[0], vector[1], goal)
        if not yes > 0:
            w.go_to_next_waypoint()

commands.close_connection()
