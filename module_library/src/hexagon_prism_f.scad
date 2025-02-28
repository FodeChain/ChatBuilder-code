module hexagon_prism(height=10, radius=5) {
    side_length = radius * cos(30);

    linear_extrude(height=height)
        polygon(points=[
            [radius * cos(0), radius * sin(0)],
            [radius * cos(60), radius * sin(60)],
            [radius * cos(120), radius * sin(120)],
            [radius * cos(180), radius * sin(180)],
            [radius * cos(240), radius * sin(240)],
            [radius * cos(300), radius * sin(300)]
        ]);
}

module hexagon_prism_f(fillet=2,h,r){
    minkowski(){
    translate([0,0,fillet])
    hexagon_prism(h-2*fillet,r-fillet);    
    sphere(fillet);
    }  
    }