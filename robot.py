import commands
import fields
import socket
import math
import mathutils
from time import sleep

ADDRESS = ("0.0.0.0", 55555)
BASE_TURN_SPEED = 12
BASE_MOVE_SPEED = 6
ROTATE_DELAY = 0.875 / math.pi / 2

def follow_vector(vec_x, vec_y, goal_pos):
    normal_vector = mathutils.normalize(vec_x, vec_y)
    where = commands.where_robot()
    position = where["center"]
    distance = mathutils.distance(position, goal_pos)
    print(distance)
    if (distance < 50):
        commands.set_speed(0, 0)
        return 0
    orientation = where["orientation"]

    angle = mathutils.signed_angle(normal_vector, orientation)
    magnitude = mathutils.magnitude(vec_x, vec_y)
    angle = angle / (math.pi) + 1
    left = int(round(magnitude * (angle - 0.5)))
    right = int(round(magnitude * (1.5 - angle)))
    print(left, right)
    commands.set_speed(left, right)
    sleep(0.05)
    return 1


def get_robot_position():
    location = commands.where_robot()["center"]

    return location
#set up fields
#f = fields.field_holder()
#position = fields.fixed_position_tracker(10, 10)
#f.add_field(fields.infinate_constant_attractive_field(position, 10))

#while True:
#    (robot_x, robot_y) = get_robot_position()
#    (field_x, field_y) = f.get_field(robot_x, robot_y)
#    follow_vector(field_x, field_y)
#    sleep(.5)
