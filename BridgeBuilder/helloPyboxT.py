from Box2D import *

world = b2World()
groundBody = world.CreateStaticBody(
        position=(0,-10),
        shapes=b2PolygonShape(box=(50,10)),
        )
body = world.CreateDynamicBody(position=(0,4))
box = body.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)
timeStep = 1.0/60
vel_iters, pos_iters = 6,2
# This is our little game loop.
for i in range(60):
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    world.Step(timeStep, vel_iters, pos_iters)

    # Clear applied body forces. We didn't apply any forces, but you
    # should know about this function.
    world.ClearForces()

    # Now print the position and angle of the body.
    x,y = body.position
    print (x,y, body.angle)         
