import commands
import fields
import socket
import math
import mathutils

ADDRESS = ("0.0.0.0", 55555)

def follow_vector(vec_x, vec_y):
    normal_vector = mathutils.normalize(vec_x, vec_y)
    orientation = commands.where_robot()["orientation"]
    angle = math.acos(mathutils.dot_product(normal_vector, orientation))
    magnitude = mathutils.magnitude(vec_x, vec_y)
    if angle > 0.1:
        commands.set_speed(3, -3)
        return 1
    elif magnitude > 0.5:
        commands.set_speed(int(magnitude), int(magnitude))
        return 1
    return 0

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
