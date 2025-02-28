include<src/mecanum_wheel.scad>;
include<src/leg_wheel.scad>;
include<src/leg.scad>;

module front_left_mecanum_wheel(){
    rotate([0,0,180])
    mecanum_wheel(display=true,fillet=0.1,wheel_thickness=10,wheel_r=55,connection_h=18,connection_r=8,screw_r=1.0);
    }

module front_right_mecanum_wheel(){
    mirror([1,0,0])
    rotate([0,0,180])
   mecanum_wheel(display=true,fillet=0.1,wheel_thickness=10,wheel_r=55,connection_h=18,connection_r=8,screw_r=1.0);
    }
    
module rear_left_mecanum_wheel(){
    mirror([1,0,0])
     mecanum_wheel(display=true,fillet=0.1,wheel_thickness=10,wheel_r=55,connection_h=18,connection_r=8,screw_r=1.0);
    }

module rear_right_mecanum_wheel(){
       mecanum_wheel(display=true,fillet=0.1,wheel_thickness=10,wheel_r=55,connection_h=18,connection_r=8,screw_r=1.0);
    }
   
module front_left_leg_wheel(){
    mirror([1,0,0])
    leg_wheel();
    }

module front_right_leg_wheel(){
    leg_wheel();
    }
    
module rear_left_leg_wheel(){
    mirror([1,0,0])
    leg_wheel();
    }

module rear_right_leg_wheel(){
    leg_wheel();
    }

module front_left_leg(){
    mirror([1,0,0])
     leg();
    }

module front_right_leg(){
    leg();
    }
    
module rear_left_leg(){
    mirror([1,0,0])
    leg();
    }

module rear_right_leg(){
    leg();
    }
    
module rear_right_wheel(){
    color(c=[188/255,177/255,181/255])
    import("src/wheel.stl");
    }

module rear_left_wheel(){
    color(c=[188/255,177/255,181/255])
    mirror([1,0,0])
    import("src/wheel.stl");
    }

module front_right_wheel(){
    color(c=[188/255,177/255,181/255])
    import("src/wheel.stl");
    }

module front_left_wheel(){
    color(c=[188/255,177/255,181/255])
    mirror([1,0,0])
    import("src/wheel.stl");
    }

module link(){
    color(c=[177/255,177/255,181/255])
    import("src/link.stl");
    }

module joint(){
    color(c=[94/255,87/255,95/255])
    import("src/motor.stl");
    }

module chassis(){
    color(c=[0.5,0.5,0.5])
    import("src/chassis.stl");
    }
  
// offset variable  
rear_right_mecanum_wheel_negative_x = 13.8;  
rear_left_mecanum_wheel_positive_x = 13.8;      
front_right_mecanum_wheel_negative_x = 13.8;  
front_left_mecanum_wheel_positive_x = 13.8;
    
rear_right_leg_wheel_negative_x = 33;  
rear_left_leg_wheel_positive_x = 33;      
front_right_leg_wheel_negative_x = 33;  
front_left_leg_wheel_positive_x = 33;        
    
rear_right_leg_negative_x = 33;  
rear_left_leg_positive_x = 33;      
front_right_leg_negative_x = 33;  
front_left_leg_positive_x = 33;     
   
rear_right_wheel_negative_x = 7.5;  
rear_left_wheel_positive_x = 7.5;      
front_right_wheel_negative_x = 7.5;  
front_left_wheel_positive_x = 7.5;   
    
link_positive_x = 32.7;
link_negative_x = 32.7;
link_positive_z = 35;
link_negative_z = 33;

joint_positive_z = 35;
joint_negative_z = 33;  
joint_positive_x = 32.7;
joint_negative_x = 32.7;     
    
chassis_positive_z = 36.75;
chassis_negative_y = 60;
chassis_positive_y = 62;
chassis_positive_x = 69.5;
chassis_negative_x = 69.5;   