include<male_connector.scad>
include<cylinder_f.scad>

module roller_single(){
    color([235/255,46/255,46/255])
    import("src/roller.stl");
    }

module wheel_hub(connection_h,connection_r,screw_r,wheel_r=125,wheel_thickness){
    color([85/255,78/255,78/255])
    scale([wheel_r/27,wheel_r/27,wheel_r/27])
    import("src/wheel_hub.stl");
    
    color([85/255,78/255,78/255])
    rotate([0,90,0])    
    translate([0,0,-wheel_thickness/2]) 
    scale([wheel_r/27,wheel_r/27,wheel_thickness/25])   
    cylinder_f(5,25,15,15);
    
    color([85/255,78/255,78/255])
    rotate([0,-90,0])
    translate([0,0,wheel_thickness/2])
    male_connector(connection_h=connection_h,connection_r=connection_r,screw_r=screw_r); 

    }
    
module roller_pair_all(){
    for (i=[0:1:9]){
        
        rotate([36*i,0,0])
        union(){
        roller_single();

        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();}
        }
    }

module roller_pair_1(){

        rotate([36*1,0,0])
        roller_single();

        rotate([36*0,0,0])
        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();
    }
    
module roller_pair_2(){

        rotate([36*2,0,0])
        roller_single();

        rotate([36*1,0,0])
        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();
    }
    
module roller_pair_3(){

        rotate([36*3,0,0])
        roller_single();

        rotate([36*2,0,0])
        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();
    }

module roller_pair_4(){

        rotate([36*4,0,0])
        roller_single();

        rotate([36*3,0,0])
        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();
    }
    
module roller_pair_5(){
    
        rotate([36*5,0,0])
        roller_single();

        rotate([36*4,0,0])
        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();
    }
    
module roller_pair_6(){
     
        rotate([36*6,0,0])
        roller_single();
  
        rotate([36*5,0,0])
        mirror([0,0,1])
        mirror([1,0,0])
        roller_single();
    }
    
module roller_pair_7(){
 
    rotate([36*7,0,0])
    roller_single();
 
    rotate([36*6,0,0])
    mirror([0,0,1])
    mirror([1,0,0])
    roller_single();
}

module roller_pair_8(){
   
    rotate([36*8,0,0])
    roller_single();
   
    rotate([36*7,0,0])
    mirror([0,0,1])
    mirror([1,0,0])
    roller_single();
}

module roller_pair_9(){
  
    rotate([36*9,0,0])
    roller_single();
   
    rotate([36*8,0,0])
    mirror([0,0,1])
    mirror([1,0,0])
    roller_single();
}

module roller_pair_10(){
  
    rotate([36*10,0,0])
    roller_single();
  
    rotate([36*9,0,0])
    mirror([0,0,1])
    mirror([1,0,0])
    roller_single();
}


module mecanum_wheel(display=true,fillet,wheel_thickness,wheel_r=125,connection_h=20,connection_r=25,screw_r=3){

    union(){
    if (display == true) 
        {
         scale([wheel_r/27,wheel_r/27,wheel_r/27])
         roller_pair_all();
         wheel_hub(connection_h=connection_h,connection_r=connection_r,screw_r=screw_r,wheel_r=wheel_r,wheel_thickness=wheel_thickness);
        }
    if (display == 1) 
        {
         scale([wheel_r/27,wheel_r/27,wheel_r/27])
         roller_pair_1();}
    if (display == 2) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_2();}
    if (display == 3) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_3();}
    if (display == 4) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_4();}
    if (display == 5) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_5();}
    if (display == 6) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_6();}
    if (display == 7) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_7();}
    if (display == 8) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_8();}
    if (display == 9) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_9();}
    if (display == 10) 
        {scale([wheel_r/27,wheel_r/27,wheel_r/27])
            roller_pair_10();}
    if (display == 11) 
        {wheel_hub(connection_h=connection_h,connection_r=connection_r,screw_r=screw_r,wheel_r=wheel_r,wheel_thickness=wheel_thickness);}
    }
}