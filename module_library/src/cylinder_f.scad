module cylinder_f(fillet=2,height,rad1,rad2){
    minkowski(){
    translate([0,0,fillet])
    cylinder(h=height-2*fillet,r1=rad1-fillet,r2=rad2-fillet);
    sphere(fillet);
    }
    }