# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#1
def f_to_c(f_temp):
    return f_temp - 32 * (5/9)
#2
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#3 
def c_to_f(c_temp):
    return c_temp *(9/5) + 32
#4 
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#5
def get_force(mass, acceleration):
    return mass * acceleration
#6
train_force = get_force(train_mass, train_acceleration)
#7
print("The GE train supplies ", train_force, " Newtons of force.")

#8
def get_energy(mass, c = 3*10**8):
    return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies ", bomb_energy, " Joules")
 #11
def get_work(mass, acceleration, distance):
    force = get_force(mass,acceleration)
    return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does ", train_work, "Joules of work over", train_distance, " meters.")
