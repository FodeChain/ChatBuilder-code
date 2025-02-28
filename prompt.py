Planner_prompt = '''
Your task is to analyze the input text, determine what kind of robot is required for the task, and output a detailed description of the robot's structure and type based on the analysis.
Please provide the most straightforward and simple plan, such as specifying a manipulator(robotic arm), a wheeled robot, a legged robot , a leg-wheeled robot or other types of non-typical robots. Please focus solely on the structural composition, without involving electromechanical or sensor-related aspects.
If the input contains quantitative constraints such as numbers, it is imperative to first perform calculations based on the dimensions of the parts to deduce the corresponding number of components required.
You can perform a series of calculations based on the requirements and the dimensions of these components to determine the number of parts needed.
You can only use the following components: 
joint, link, chassis, rear_right_wheel, rear_left_wheel, front_right_wheel, front_left_wheel.
The dimensions of these components:
each link: length is 68; width is 65.4;
each joint: length is 68; width is 65.4;
each chassis: length is 122(The length corresponding to the body); width is 139;
each wheel: radius is 49.9;
you can get longer upper arm or lower arm by add more links. But a upper arm or lower arm should consists of at least two links. (The total length of the upper arm or lower arm is 68 multiplied by the total number of links)
you can add more chassises to get more wheels or legs. One chassis can only connect to at most two wheels or legs or leg-wheels. (The total length of the body is 122 multiplied by the total number of chassies)
each wheel must be connected to a different motor. It means wheel must be with a joint.
you can use manipulator(robotic arm) as leg: connect robotic arm to positive or negative x direction of the chassis. each leg should have at least two-degree-of-freedom. The shoulder joint is similar to the hip joint, and the elbow joint is similar to the knee joint. 
A puppy's leg resembles a two-degree-of-freedom robotic arm with two rotary joints, while a spider's leg is akin to a typical three-degree-of-freedom robotic arm. 
You are also encouraged to independently create various other types of legs.
you can also use some predefined high-level components: 
rear_right_mecanum_wheel, rear_left_mecanum_wheel, front_right_mecanum_wheel, front_left_mecanum_wheel,
rear_right_leg, rear_left_leg, front_right_leg, front_left_leg,(leg similar to that of a puppy robot, like wheel, must connect to a motor),
rear_right_leg_wheel, rear_left_leg_wheel, front_right_leg_wheel, front_left_leg_wheel,(leg_wheel similar to that of a puppy robot, like wheel, must connect to a motor),
you can substitute the wheel part(rear_right_wheel, rear_left_wheel, front_right_wheel, front_left_wheel) with these high-level components.

For example:

Input: A robot capable of grasping objects in open spaces.
Output:
a manipulator(robotic arm) with six-degree-of-freedom
part_1: 
//function: a base for the robotic arm
//type: chassis
part_2:
//function: Base Rotation Joint. Allows the robotic arm to rotate around the vertical axis of its base.
//type: joint
part_3: 
//function: Shoulder Joint. Provides the robotic arm with the ability to swing up and down, typically located above the base joint.
//type: joint
part_4: 
//function: Part of the upper arm, which is generally composed of multiple links, this is one of them. 
//type: link
part_5: 
//function: Part of the upper arm, which is generally composed of multiple links, this is one of them.
//type: link
part_6: 
//function: Elbow Joint. Enables the forearm section of the robotic arm to bend and extend.
//type: joint
part_7: 
//function: Part of the lower arm, which is generally composed of multiple links, this is one of them.
//type: link
part_8: 
//function: Part of the lower arm, which is generally composed of multiple links, this is one of them.
//type: link
part_9: 
//function: Wrist Pitch Joint. Controls the upward and downward tilt of the robotic arm's end effector.
//type: joint
part_10: 
//function: Wrist Rotation Joint. Allows the end effector to rotate around its own axis.
//type: joint
part_11: 
//function: Wrist Yaw Joint. Permits the end effector to swing from side to side.
//type: joint

Input: A robot that can navigate through narrow spaces. 
Output:
A mobile robot with four wheels.
part_1:
//function: Part of the main body for the mobile robot, which is generally composed of multiple chassises, this is one of them.
//type: chassis
part_2:
//function: Part of the main body for the mobile robot, which is generally composed of multiple chassises, this is one of them.
//type: chassis
part_3:
//function: motor of rear_right_wheel. drive the rear_right_wheel.
//type: joint
part_4:
//function: rear_right_wheel
//type: rear_right_wheel
part_5:
//function: motor of rear_left_wheel. drive the rear_left_wheel.
//type: joint
part_6:
//function: rear_left_wheel
//type: rear_left_wheel
part_7:
//function: motor of front_right_wheel. drive the front_right_wheel.
//type: joint
part_8:
//function: front_right_wheel
//type: front_right_wheel
part_9:
//function: motor of front_left_wheel. drive the front_left_wheel.
//type: joint
part_10:
//function: front_left_wheel
//type: front_left_wheel
'''

Assembler_prompt = '''
Based on the input text, program and model the robot using OpenSCAD, 
you can only use following components: 
chassis() , link(), joint(), rear_right_wheel(), rear_left_wheel(), front_right_wheel(), front_left_wheel()
you can use arm as leg:connect arm to positive or negative x direction of the chassis.

you can also use some predefined high-level components: 
rear_right_mecanum_wheel(), rear_left_mecanum_wheel(), front_right_mecanum_wheel(), front_left_mecanum_wheel(),
rear_right_leg(), rear_left_leg(), front_right_leg(), front_left_leg(),(leg similar to that of a puppy robot,like wheel, must connect to a motor),
rear_right_leg_wheel(), rear_left_leg_wheel(), front_right_leg_wheel(), front_left_leg_wheel(),(leg_wheel similar to that of a puppy robot,like wheel, must connect to a motor),
you can substitute the wheel part(rear_right_wheel, rear_left_wheel, front_right_wheel, front_left_wheel) with these high-level components.

you can only use following offset-variable: 
rear_right_wheel_negative_x;  
rear_left_wheel_positive_x;      
front_right_wheel_negative_x;  
front_left_wheel_positive_x;   

link_positive_x,
link_negative_x, 
link_positive_z, 
link_negative_z, 

joint_positive_z, 
joint_negative_z,  
joint_positive_x, 
joint_negative_x,  

chassis_positive_z,
chassis_negative_y, 
chassis_positive_y,
chassis_positive_x, 
chassis_negative_x, 

rear_right_mecanum_wheel_negative_x;  
rear_left_mecanum_wheel_positive_x;      
front_right_mecanum_wheel_negative_x;  
front_left_mecanum_wheel_positive_x;

rear_right_leg_wheel_negative_x;  
rear_left_leg_wheel_positive_x;      
front_right_leg_wheel_negative_x;  
front_left_leg_wheel_positive_x;        

rear_right_leg_negative_x;  
rear_left_leg_positive_x;      
front_right_leg_negative_x;  
front_left_leg_positive_x;     

Please strictly follow the example format to write.

For example:
Input: 
a robot arm with six-degree-of-freedom
part_1: 
//function: a base for the robotic arm
//type: chassis
part_2: joint
//function: Base Rotation Joint. Allows the robotic arm to rotate around the vertical axis of its base.
//type: joint
part_3: 
//function: Shoulder Joint. Provides the robotic arm with the ability to swing up and down, typically located above the base joint.
//type: joint
part_4: 
//function: Part of the upper arm, which is generally composed of multiple links, this is one of them. you can get a long arm by add more links. But a arm should consists of at least two links.
//type: link
part_5: 
//function: Part of the upper arm, which is generally composed of multiple links, this is one of them.
//type: link
part_6: 
//function: Elbow Joint. Enables the forearm section of the robotic arm to bend and extend.
//type: joint
part_7: 
//function: Part of the lower arm, which is generally composed of multiple links, this is one of them.
//type: link
part_8: 
//function: Part of the lower arm, which is generally composed of multiple links, this is one of them.
//type: link
part_9: 
//function: Wrist Pitch Joint. Controls the upward and downward tilt of the robotic arm's end effector.
//type: joint
part_10: 
//function: Wrist Rotation Joint. Allows the end effector to rotate around its own axis.
//type: joint
part_11: 
//function: Wrist Yaw Joint. Permits the end effector to swing from side to side.
//type: joint

Output: 
//part_1
//type: chassis
//position: origin position (0,0,0)
//orientation: origin orientation.facing the positive z direction
part_1_x_t = 0; 
part_1_y_t = 0; 
part_1_z_t = 0;
translate([part_1_x_t, part_1_y_t, part_1_z_t])
rotate([0,0,0])
chassis();

//part_2
//type: joint
//position: The negative z direction of part_2 (joint) is connected to the positive z direction of part_1 (chassis). part_2 (joint) has an offset in the positive z direction relative to part_1 (chassis).
//orientation: origin orientation. facing the positive z direction
part_2_x_t = part_1_x_t;
part_2_y_t = part_1_y_t; 
part_2_z_t = part_1_z_t + chassis_positive_z + joint_negative_z;
translate([part_2_x_t, part_2_y_t, part_2_z_t])
rotate([0,0,0])
joint();

//part_3
//type: joint
//position: The negative x direction of part_3 (joint) is connected to the positive z direction of part_2 (joint). part_3 (joint) has an offset in the positive z direction relative to part_2 (joint).
//orientation: facing the negative x direction. rotate -90 degrees around the y-axis.(0,-90,0)
part_3_x_t = part_2_x_t;
part_3_y_t = part_2_y_t; 
part_3_z_t = part_2_z_t + joint_positive_z + joint_negative_x;
translate([part_3_x_t, part_3_y_t, part_3_z_t])
rotate([0,-90,0])
joint();

//part_4
//type: link
//position: The positive x direction of part_4 (link) is connected to the positive z direction of part_3 (joint). part_4 (link) has an offset in the negative x direction relative to part_3 (joint).
//orientation: origin orientation. facing the positive z direction
part_4_x_t = part_3_x_t - link_positive_z - link_positive_x;
part_4_y_t = part_3_y_t; 
part_4_z_t = part_3_z_t;
translate([part_4_x_t, part_4_y_t, part_4_z_t])
rotate([0,0,0])
link();

//part_5
//type: link
//position: The negative z direction of part_5 (link) is connected to the positive z direction of part_4 (link). part_5 (link) has an offset in the positive z direction relative to part_4 (link).
//orientation: origin orientation. facing the positive z direction
part_5_x_t = part_4_x_t;
part_5_y_t = part_4_y_t; 
part_5_z_t = part_4_z_t + joint_positive_z + link_negative_z;
translate([part_5_x_t, part_5_y_t, part_5_z_t])
rotate([0,0,0])
link();

//part_6
//type: joint
//position: The positive x direction of part_6 (joint) is connected to the positive z direction of part_5 (link). part_6 (joint) has an offset in the positive z direction relative to part_5 (link).
//orientation: facing the positive x direction. rotate 90 degrees around the y-axis.(0,90,0)
part_6_x_t = part_5_x_t;
part_6_y_t = part_5_y_t; 
part_6_z_t = part_5_z_t + link_positive_z + joint_positive_x;
translate([part_6_x_t, part_6_y_t, part_6_z_t])
rotate([0,90,0])
joint();

//part_7
//type: link
//position: The negative x direction of part_7 (link) is connected to the positive z direction of part_6 (joint). part_7 (link) has an offset in the positive x direction relative to part_6 (joint).
//orientation: origin orientation. facing the positive z direction
part_7_x_t = part_6_x_t + link_positive_z + link_negative_x;
part_7_y_t = part_6_y_t; 
part_7_z_t = part_6_z_t;
translate([part_7_x_t, part_7_y_t, part_7_z_t])
rotate([0,0,0])
link();

//part_8
//type: link
//position: The negative z direction of part_8 (link) is connected to the positive z direction of part_7 (link). part_8 (link) has an offset in the positive z direction relative to part_7 (link).
//orientation: origin orientation. facing the positive z direction
part_8_x_t = part_7_x_t;
part_8_y_t = part_7_y_t; 
part_8_z_t = part_7_z_t + joint_positive_z + link_negative_z;
translate([part_8_x_t, part_8_y_t, part_8_z_t])
rotate([0,0,0])
link();

//part_9
//type: joint
//position: The negative x direction of part_9 (joint) is connected to the positive z direction of part_8 (link). part_9 (joint) has an offset in the positive z direction relative to part_8 (link).
//orientation: facing the negative x direction. rotate -90 degrees around the y-axis.(0,-90,0)
part_9_x_t = part_8_x_t;
part_9_y_t = part_8_y_t; 
part_9_z_t = part_8_z_t + link_positive_z + joint_negative_x;
translate([part_9_x_t, part_9_y_t, part_9_z_t])
rotate([0,-90,0])
joint();

//part_10
//type: joint
//position: The positive x direction of part_10 (joint) is connected to the positive z direction of part_9 (joint). part_10 (joint) has an offset in the negative x direction relative to part_9 (joint).
//orientation: origin orientation. facing the positive z direction
part_10_x_t = part_9_x_t - joint_positive_z - joint_positive_x;
part_10_y_t = part_9_y_t; 
part_10_z_t = part_9_z_t ;
translate([part_10_x_t, part_10_y_t, part_10_z_t])
rotate([0,0,0])
joint();

//part_11
//type: joint
//position: The negative x direction of part_11 (joint) is connected to the positive z direction of part_10 (joint). part_11 (joint) has an offset in the positive z direction relative to part_10 (joint).
//orientation: facing the negative x direction. rotate -90 degrees around the y-axis.(0,-90,0)
part_11_x_t = part_10_x_t;
part_11_y_t = part_10_y_t; 
part_11_z_t = part_10_z_t + joint_positive_z + joint_negative_x;
translate([part_11_x_t, part_11_y_t, part_11_z_t])
rotate([0,-90,0])
joint();

Input: 
a mobile robot with four wheels.
part_1:
//function: Part of the main body for the mobile robot, which is generally composed of multiple chassises, this is one of them.
//type: chassis
part_2:
//function: Part of the main body for the mobile robot, which is generally composed of multiple chassises, this is one of them.
//type: chassis
part_3:
//function: motor of rear_right_wheel. drive the rear_right_wheel.
//type: joint
part_4:
//function: rear_right_wheel
//type: rear_right_wheel
part_5:
//function: motor of rear_left_wheel. drive the rear_left_wheel.
//type: joint
part_6:
//function: rear_left_wheel
//type: rear_left_wheel
part_7:
//function: motor of front_right_wheel. drive the front_right_wheel.
//type: joint
part_8:
//function: front_right_wheel
//type: front_right_wheel
part_9:
//function: motor of front_left_wheel. drive the front_left_wheel.
//type: joint
part_10:
//function: front_left_wheel
//type: front_left_wheel

Output: \
//part_1
//position: origin position (0,0,0)
//orientation: origin orientation.facing the positive z direction
part_1_x_t = 0; 
part_1_y_t = 0; 
part_1_z_t = 0;
translate([part_1_x_t, part_1_y_t, part_1_z_t])
rotate([0,0,0])
chassis();

//part_2
//position: The negative y direction of part_2 (chassis) is connected to the positive y direction of part_1 (chassis). part_2 (chassis) has an offset in the positive z direction relative to part_1 (chassis).
//orientation: origin orientation.facing the positive z direction
part_2_x_t = part_1_x_t; 
part_2_y_t = part_1_y_t + chassis_positive_y + chassis_negative_y; 
part_2_z_t = part_1_z_t;
translate([part_2_x_t, part_2_y_t, part_2_z_t])
rotate([0,0,0])
chassis();

//part_3
//position: The negative z direction of part_3 (joint) is connected to the positive x direction of part_1 (chassis). part_3 (joint) has an offset in the positive x direction relative to part_1 (chassis).
//orientation: facing the positive x direction. rotate 90 degrees around the y-axis.(0,90,0)
part_3_x_t = part_1_x_t + chassis_positive_x + joint_negative_z; 
part_3_y_t = part_1_y_t; 
part_3_z_t = part_1_z_t;
translate([part_3_x_t, part_3_y_t, part_3_z_t])
rotate([0,90,0])
joint();

//part_4
//position: The negative x direction of part_4 (rear_right_wheel) is connected to the positive z direction of part_3 (joint). part_4 (rear_right_wheel) has an offset in the positive x direction relative to part_3 (joint).
//orientation:  origin orientation.facing the negative x direction
part_4_x_t = part_3_x_t + joint_positive_z + rear_right_wheel_negative_x; 
part_4_y_t = part_3_y_t; 
part_4_z_t = part_3_z_t;
translate([part_4_x_t, part_4_y_t, part_4_z_t])
rotate([0,0,0])
rear_right_wheel();

//part_5
//position: The negative z direction of part_5 (joint) is connected to the negative x direction of part_1 (chassis). part_5 (joint) has an offset in the negative x direction relative to part_1 (chassis).
//orientation: facing the negative x direction. rotate -90 degrees around the y-axis.(0,-90,0)
part_5_x_t = part_1_x_t - chassis_negative_x - joint_negative_z; 
part_5_y_t = part_1_y_t; 
part_5_z_t = part_1_z_t;
translate([part_5_x_t, part_5_y_t, part_5_z_t])
rotate([0,-90,0])
joint();

//part_6
//position: The positive x direction of part_6 (rear_left_wheel) is connected to the positive z direction of part_5 (joint). part_6 (rear_left_wheel) has an offset in the negative x direction relative to part_5 (joint).
//orientation:  origin orientation.facing the positive x direction
part_6_x_t = part_5_x_t - joint_positive_z - rear_left_wheel_positive_x; 
part_6_y_t = part_5_y_t; 
part_6_z_t = part_5_z_t;
translate([part_6_x_t, part_6_y_t, part_6_z_t])
rotate([0,0,0])
rear_left_wheel();

//part_7
//position: The negative z direction of part_7 (joint) is connected to the positive x direction of part_2 (chassis). part_7 (joint) has an offset in the positive x direction relative to part_2 (chassis).
//orientation: facing the positive x direction. rotate 90 degrees around the y-axis.(0,90,0)
part_7_x_t = part_2_x_t + chassis_positive_x + joint_negative_z; 
part_7_y_t = part_2_y_t; 
part_7_z_t = part_2_z_t;
translate([part_7_x_t, part_7_y_t, part_7_z_t])
rotate([0,90,0])
joint();

//part_8
//position: The negative x direction of part_8 (front_right_wheel) is connected to the positive z direction of part_7 (joint). part_8 (front_right_wheel) has an offset in the positive x direction relative to part_7 (joint).
//orientation:  origin orientation.facing the negative x direction
part_8_x_t = part_7_x_t + joint_positive_z + front_right_wheel_negative_x; 
part_8_y_t = part_7_y_t; 
part_8_z_t = part_7_z_t;
translate([part_8_x_t, part_8_y_t, part_8_z_t])
rotate([0,0,0])
front_right_wheel();

//part_9
//position: The negative z direction of part_9 (joint) is connected to the negative x direction of part_2 (chassis). part_9 (joint) has an offset in the negative x direction relative to part_2 (chassis).
//orientation: facing the negative x direction. rotate -90 degrees around the y-axis.(0,-90,0)
part_9_x_t = part_2_x_t - chassis_negative_x - joint_negative_z; 
part_9_y_t = part_2_y_t; 
part_9_z_t = part_2_z_t;
translate([part_9_x_t, part_9_y_t, part_9_z_t])
rotate([0,-90,0])
joint();

//part_10
//position: The positive x direction of part_10 (front_left_wheel) is connected to the positive z direction of part_9 (joint). part_10 (front_left_wheel) has an offset in the negative x direction relative to part_9 (joint).
//orientation:  origin orientation.facing the positive x direction
part_10_x_t = part_9_x_t - joint_positive_z - front_left_wheel_positive_x; 
part_10_y_t = part_9_y_t; 
part_10_z_t = part_9_z_t;
translate([part_10_x_t, part_10_y_t, part_10_z_t])
rotate([0,0,0])
front_left_wheel();
'''