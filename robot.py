import command
import fields

def follow_vector(vec_x, vec_y):
    print('following(' + str(vec_x) + ',' + str(vec_y) + ')')

def get_robot_position():
    return (0.0, 0.0)

#set up fields
f = fields.field_holder()
f.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(10, 10), 10))

while True:
    (robot_x, robot_y) = get_robot_position()
    (field_x, field_y) = f.get_field(robot_x, robot_y)
    follow_vector(field_x, field_y)    
    sleep(.5)