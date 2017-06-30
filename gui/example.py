
from indicatorgridworld import *
from racetrack import *
from objectworld import *
from gui import *

def ex(window_size=800, grid_dim=(5, 5), cell_size=1, gamma=0.9, world='indicator_grid', stochastic=False):


    grid_size = max(grid_dim)

    pix_per_grid = (window_size / grid_size)

    if world == 'indicator_grid':

        mdp_gw = IndicatorWorld([], grid_size, cell_size, gamma, stochastic=stochastic) #A generic grid world with indicator reward features

    if world == 'object_world':

        mdp_gw = ObjWorld([], grid_size, cell_size, gamma, stochastic=stochastic) # Object world as given in GPIRL paper

    grid_gui = GuiBoard("MaxEnt IRL", [window_size / grid_size * grid_dim[1],
                                            window_size / grid_size * grid_dim[0]], pix_per_grid)

    grid_gui.render_mdp(mdp_gw, world=world)
    grid_gui.hold_gui() # stops gui from closing and allows interaction using mouse/keyboard

ex(grid_dim= (10,10), world = 'indicator_grid')
