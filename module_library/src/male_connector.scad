include<hexagon_prism_f.scad>

module male_connector(fillet=2,connection_h=20,connection_r=25,screw_r=3){
    difference(){
    translate([0,0,-fillet])
    hexagon_prism_f(fillet,connection_h+fillet,connection_r);
    
    translate([-(connection_r),-(connection_r),-2*(connection_r)])
    cube(2*(connection_r));

    translate([0,0,connection_h/2])
    rotate([90,0,0])
    translate([0,0,-2*(connection_r)])
    cylinder(4*(connection_r),screw_r,screw_r);
    } 
}