import ProjetFinal


a = ProjetFinal.Atmosphere(altitude=10000)
density = a.density()

# Calcul de la performance de vol en utilisant la fonction Performance
lift, drag, thrust = ProjetFinal.performance(density=density, velocity=f.speed, weight=100000)

