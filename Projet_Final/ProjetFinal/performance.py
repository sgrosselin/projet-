def performance(density, velocity, weight):
    ## A modifier
    surface_area = 100   # m^2
    lift = weight # vol stationnaire horizontale = vol equilibre
    drag = 0.5 * density * velocity**2 * surface_area
    thrust = drag * 1.1
    return lift, drag, thrust