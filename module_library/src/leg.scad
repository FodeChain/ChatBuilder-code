module leg(){
rotate([0,90,0])
color(c=[94/255,87/255,95/255])
import("src/motor.stl");

rotate([145,0,0])
translate([-15,-15,0]) 
color(c=[94/255,87/255,95/255])
cube([30,30,100]);

rotate([0,90,0])
color(c=[180/255,181/255,182/255])
cylinder(50,10,10);

translate([45,0,0])
rotate([55,0,0])
translate([-5,-5,0]) 
color(c=[180/255,181/255,182/255])
cube([10,10,35]);

translate([35,-20,20])
rotate([145,0,0])
translate([-5,-5,0]) 
color(c=[100/255,100/255,100/255])
cube([10,10,100]);

translate([22,-50,-80])
rotate([-55-90,0,0])
translate([-7.25,-7.25,-40]) 
color(c=[180/255,181/255,182/255])
cube([15.5,15.5,112]);

translate([22,0,-150])
color(c=[180/255,181/255,182/255])
sphere(20);}