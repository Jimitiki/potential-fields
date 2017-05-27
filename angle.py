import fields
import commands
import mathutils
import math

ADDRESS = ("0.0.0.0", 55555)
commands.open_connection(ADDRESS)

goal = commands.where_markers()[str(20)]["center"]
f = fields.field_holder()
f.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(goal[0], goal[1]), 10))
position = commands.where_robot()["center"]
vector = f.get_field(position[0], position[1])
normal_vector = mathutils.normalize(vector[0], vector[1])
orientation = commands.where_robot()["orientation"]
angle = math.acos(mathutils.dot_product(normal_vector, orientation))

angle = math.atan2(normal_vector[1], normal_vector[0]) - math.atan2(orientation[1], orientation[0])
if angle < 0: angle += 2 * math.pi;
angle -= math.pi

print(mathutils.dot_product(normal_vector, orientation))

print(angle)

commands.close_connection()
