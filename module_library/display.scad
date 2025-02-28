$vpd= 3000;
$vpt=[600,0,-50];

include<module_library.scad>;

chassis();

translate([200,0,0])
link();

translate([400,0,0])
joint();

translate([600,0,0])
front_right_wheel();

translate([800,0,0])
front_right_leg();

translate([1000,0,0])
front_right_leg_wheel();

translate([1200,0,0])
front_right_mecanum_wheel();