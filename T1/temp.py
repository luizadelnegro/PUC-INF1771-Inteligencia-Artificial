from pygame.locals import *
import pygame
import glob
 
 
map1 ="""                             
                             
##########################################################...R..RR.....R..R......R.....RR..R....RRR..R..R...RR.....R.R....R..RRRR........R.R...RRR......R.R.R...R......R.R.....R.R........RR.R.........R
#########################################################R....R.....RR.R...R.......R...RR...R........R....R.R.R...RR...............RRR..R.....R.RR...RR.......R....R......R.R.....RR.RR..R.....RRR....R.
########################################################.RRRR.R.RR...R...R..RRR..RRRR.....R.R..R.RR..R.RRR....R.R....R...R...R...R........R...RR.R...............R..R.R..R..R..R..R..R.R...RR.R..RR.R..R
#######################################################RR..R...R.R...R.RRM.MMMMM..R..R...R..MMR....R.RR......R....RR....RMMR...R..R......R.........R.R......R.....RR..R...R...R.RR.......RR.R.RR....R.R.
###################################################.RRRR.....RR...R.....R.MMMMMM.RM...R...RMMMMRR...R....RRR.....RMMMMMMMMMMMMM....R..R..RR.....R......R..R..R..R....R..RRR....RR..R..R..R........R.....
#########################################R....####..R..RR.....R.....R..R...MMMMMMMMMMMMMM..MMMMM..RR.......R.R.MMMMMMMMM...MMMMMMMMMRRRR.........R.......RR.....R..RRR..............RR...R..R...RR..R...
######################################..R.RMM..###R.R...MMM.R.....R...R...RR..MMMMMMMMMMMMMMMMMMMMMR..........MMMMMMMMM.RRMMMMMMMMMMMM....R...R...R..RR..R.RR.........RR.....R..R.RR.R.....R.....R.....R
###################################.RR..MMMM..R######.RMMM........R.R..RR.R..R..R.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.RR.R.RR....R.M......R..R.R...RR..........RRR.MMMMMMM.RMMRR.R.R......R.R..R.R..R.R
################################.RRMMMMMMMMMMMMRRR...RMMM..R.RR....R......RR..R.R.RMMMMMMMMMMM..R.RMMMMMMMMMMMMMMMMMMMM.RR....RR...RR.R...R.RR.....R..........R..MMM.R.MMMMMMMMMMMMR..RR.R...RR.RR..R.R.
##############################R.MMMMMMMMMMMMMM.R.R.MMMMMMMM##MR..RRMMMMM.R.R..R..RR..R..MMMMMMMMM..MMMM..MMM..RMMMMMMMMMMMMMMMM.............R.RRR.R..R.R...R..RRR.M..R.MMMMMMMMMMMMMMMMMMM...R.........R
############################...MMMMMMMMMMMMMMMM..MMMMMMMMM.####..RMMMMMMM.RR.....R.......R.RR.MMM.R.RR.MMM.RRMMMMMMMMMMMMMMMMMMMMMM.RR.....R.R...RR...R....RR....R..RRR.....R..RR...R..RRMMMMR.....R....
############################RMMMMMMMMMMMMMMMMMMR.MMMMMMM.#####....MMMMMMMRR.....RR...R........MMMM.R....R....R.RRVVVVVVVVVMMMMMMMMMMMMMMM.R......R......R.......MMM...........RR..RR......M.MMMMMMM...R.
############################..RMMMMMMMMMMMMMMM...MMMMMM.#####..R...MMMM......M.MM....MM...MMRRMMMM....RRR..........VVVVVVVVVVMMMMMMMMMMMMMM....R..R..R.R......RMMMMMMMMRMMMMMMR...R..RRR..........RM..R.
#############################RRMMMMMMMMMMMMMMMM..MMMMM######R..R.RR.RRR.R.RRMMMMMMMMMMMMMMMMMMMMMM..R...RR.R....R.VVVVVVVVVVVVVVVVVVVVVVVR.MMMR.RRRR....RR....RMMMMMMMMMMMMMMMMMMMMM...MMMM.MRMMM.....R.
############################.MMMMMMMMMMMMMMMMMM..MMMRVVVV.MMMMMMMMMMR....R.MMMMM..MMMMMMMMMMMMMMMMM.R.RR........8VVVVVVVVVVVVVVVVVVVVVVR..MMMMM..R....R.R.R.R...MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM....R...
###########################..MMMMMMMMMMMMMMMMM..VVVV1.V..RMMMMMMMMMR2....MMMM..R.R..RR..VV.R4MMMMMM.R.R..RR..R..RVVVVVVVVVVVVVVVVVVVVVV..MMMMMMM...RR.R.....RR..R..RMMMMMMMMMMMMMMMMMMR.MMMMMMMM........
##########################R.MMMMMMMMMMMMMMMMM...RVVVVVVV. MMMMMRR....VVVVVMMMMM.RVVVVVR.VV.VV..MMMM....R.....R..RVVVVVVVVVVVVVVVVVVVVVVVMMMMMMM..R...RR.RRR.......R..R.........RMMMMM..R....MM...RR.R..R
#########################RVVVVVVVVVVVV...RMMMMMMMMM.I.VV........R....RVVVVMMMMMM.VVVV3VVVVV.VV.MMMMM.RRR..R..R..VVVVVVVVVVVVVVVVVVVVVVVVV.MMMMR....R.R.R.......R.RR....RR....R..R...........R.R.R...R.R.
#########################R.VVVVVVVVVVR..MMMMMMMMMM.......RVVVVVVVVVV.VVVVVVMMMMM.RRVVVVVVVV.VR5RRMM.R.R..R.......VVVVVVVVVVVVVVVVVVVVVVVVVV....R...R...R...RR.....RRRRRR..RR...R...R.R..R.RR.....R..R..R
#########################.RVVVVVVVR.###RMMMM.MMMM.R......RVVVVVVVVVV.VVVVVVMMMMMRR..VVVVV...V...6MM..R.....R.....RRVVVVVVVVVVVVVVVVVVMMMMMVVVVVVV..V.V...R....RRR..RR...RRR.R..RR.R...VVV.VV..R.VVV.....
#########################..VVVVVVR.####R.MMMMMMMMM.R..R....RVVVVVVV...MMMMMMVVMMMM..R.VV..R.RRRMMM7...RR....R..R...R.R.VVVVVVVVVVVVVVMMMMMMMMMMMV.V..VR...R......R.........R.R.RRVVVV.VVVV.VVVVVVVV.R.R.
###########################R..R.######.RMMMMMMMMMMMMR..RR...R.R.VVRRR.RMM..MMMMMMMM....R..MMMMMMMMMMMR...R.R...RR....R.VVVVVVVVVVVVVVVVMMMMRMMMMMVV.VVVVV...R...R...R.......R...VVVVVVVVVVVVVVVVVVVV..R.
###################################..MMMMMMMMMMMMMMMM.R.R.MMM.R.R..R......R.MMMVVMM...RR.MRR..MMMMMMMMMMMM..R...RRR.R.RRVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV...R........R..R.R...RVVVVVVVVVVVVVVVVVVVV....
##################################.MMMMMMMMMMMMMMMMMMMMMMMMM.R...R..........V.VVVVVV...RRR.RR.RMMMMMMMMMMMMVVV..R..R....RVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV.RR.RR..RR.R...R.R...VVVVVVVVVVVVVVVVVVVVVVV..
##################################.MMMMMMMMMMMMMMMMMMMMMMMMMMMMM......R..R.VVVVVVVVV.R.R...R.RMMMMMMMMMVVVVVVV.RRR....R.VVVVVVVVVVVVV....R.VVVVVVVVVVVVVVV.....R..RR.RR.R.....RVVVVVVVVVVVVVVVVVVVVVVV..
##################################R.RMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM..RR....R.VV..R..RR........MMMMMMMMM.RR.VVVV..RR....RVVVVVVVVVV..R..R.R...R...VVVVVVVVV......R..RR......RR.RR..RR....RVVVVVVVVVVVVVR.
####################################...MMMMMMMMMMMMMMMMVVVVVVVVVVVR...R..R..RR..R..R.R...R..MMMMMMMMMMRRVVVVVVV9V...R...R..VVV.R....RRR.....RR..RRR.....R...R.R....RR.RRR...############R.VVVVVVVVV.R.RR
########################################.VVMMMMMMMMMMMMMMVVVVVVV......RR.R..R.R...RRMMMMMMMMMMMMMVVVVVVVVVVVVVVVVR......RR.A...RR.....R.R.R.R..R.....RR..RR...R.MMMMMM...RR##############..VVVVVVVV.....
#########################################...VVMMMMMMMMMMMMMVVV.R....R.R.R.R...R.....MMMMMMMMMMMMMMVVVVVVVVVVVVVV.RRR##....RRR.MMMMMMMMMM....R.R...R.........R..RMMMMMMMMMMR##############.VVVVVVVVV.....
############################################RRMMMMMMMMMMMMMM...R.R..R..R...R.R....RRMMMMMMMMMMMMMMMVVVVVVVR.R.....R#########RMMMMMMMMMMMM.R...R..R..R.....R.......MMMMMM..R############R..VVVVV.R.....R.
#############################################R..VVVMMMMMMMMMMM.R....R..R....R..R...R.RMMMMMMMMMMMR.R..RRRRRR.RRR.R.R#########.MMMMMMMMMMMM.RRR.RR....R.....RRRR.RRMMMMMMMMMR######...#....R..........R..
#################################################.VVMMMMMMMMMMMRR.....R..........R.R.............R.......RR.RR..RR......#####.MMMMMMMMM.RRR.RRR.......R.........R.MMMMMMMMMMMM...R.RR...R.....RR....R...
###################################################.VVVVVV...R...R.R....VVVVR....R..R..MMR.M..R.R....R......R.......R...VVVVVVVVVVVVV....R...RR........RRR...R..RMMMMMMMMMMMMMMMMM..............R..R.RRR
#####################################################..VVVVVV...R....R.RVVVVVVV.....MMMMMMMMMMMMM.....RR..RRRR.R..R..VVVVVVVVVVVVVVVVVVVV.....R.R.R.R....RR..RR..MMMMMMMMMMMMMMMMMR.R.....R.....R.R..R.R
#######################################################......RR..VVVR.RVVVVVVVVV.RRMMMMMMMMMMMMMMMMMMM...R........R.RRVVVVVVVVVVVVVVVVVVVVV.R...RR.RR....R....R..R...RMMMMMMMMMMMMM....RRR.R.....R......
###########################################################.V.VVVVVV...VVVVVVVVV...MMMMMMMMMMMMMMMMMMMMM...R....R.R.....BVVVVVVVVVVVVVVVVVV.....RR..R.MM..RRR......R...R.......R........R..........R....
##########################################################..VVVVVV.RR.RVV.VVVVV.MMMMMMMMMMMMMMMMMMMMMMMMMMR...R.....R....R.....VVVVVVVVVVVVVV.....RC.MMMM..M..R...R.R.....R.R.RR..R.RR.R..RR.R.R...R....
##########################################################..RVVMM..M...........MR..MMMMM..R..MMMMMMMMMMMMMM...R....R.R..R.R...R..........M..MMMMMMMPPMMMMMMMMMMMMMMMM.M..MMM........R...RR.R...RR.......
##########################################################.RMMMMMMMM..RMMMMMMM..MM.MMMM..RMMMMMMMMMMMMMMMMMMMMMR.RRRR.........R.RR..R.RRMM.MMMMMMMR...MMMMMMMMMMMMMMMMMMMMMMMMMM.RR..RR.R..RR...........
#########################################################..MMMMMMMMMRMMRMM..RMMMR.VVVVVV.RMMMMMMMMMVVVVVMMMMMMMMMMM.R...R.....R.R...R..RDMMMMMMMR...R.MMMMMMMMM.HMMMMMMMMMMMMMMMMMMM.........RR...R.....
########################################################..MMMMMMMMMMMMMMMM.RM..MR.MMRVVVV...MMMRR.VVVVVRMMMMMMMMMMMRR.R.R..R..RRR.RVVVVMMMMMMMMM.R......M.MMMM....MMMR.RMMMMMMMM.RMMMMM......RRR...RR...
#######################################################.MMMMMMMM.MMMMM..M..MM.MMMMMMMMVVVV..MMMM.VVVVVV.RMMMMMMMMMMMMMMM..R.......VVVVVMMMMMMM....RR......R.GRRMMMMMMM.MMMMMMMMMMMMMMMMM.RR..R..R...R..R
#####################################################..MMMMMMMMMR.VVVVV.MMMMMMMR..VVVVVVVR.R...VVVVVVV.R.MM...RMMMMMMMMMMMMR..R.RR.###VVMMMMMM...MMR.MMM.RR..RR.MMMMMMMMMM.........RMMMMM..R..R..R...R..
###################################################..MMMMMM.R.VVVVV..MMMMMMMMMMMMMR..VVVVVV.......RRRR.R..MMM.....MMMMMMMMMMM..R...###VVVMMMM.RMMMM..MMMM......MMMMMRR.........R..R...MMMMMMRR.....R...R
#################################################.RM..MM.MM.R.VVVV..MMMMMMMMMMMMMMMMMVVVVVVVV..RR........VVV...RMMMMMMMMMMMMRRR...RR##VMM...MMMMMM.RRRMMMMM......R.....R.R......R....R.R.MMMMMMR...R.R..
#################################################..#..R.##...R.RR....R.R......R........RRVV.V...........R.VVVVVVVM.RR..MMMMMMMMV.R...VVVEM.....F...M..RMR.R......R..R.R###R..R......RRRR..MMMMMMM.....R.
####################################################################################R.....MMMMMRR..RRR.....VVVVVV...MMMMMR....R..RR.R..RMM......MMMMMMMMRMM..R....#######R.R.R....R...R....MMMMMMMM...RR
####################################################################################RRVVVMMMMMMMMRR.R......RVVVVVV.RR.......R..R...R...MMMMMMMR.MRMMR..........############.....R..R..RR.MMMMMMM.R.R....
#####################################################################################RVVVMMMMMMMM.R...R.RR..VVVVVVVVVR.....R.RR...R.R..MMMMMMMMMMMM..MM...R......#######.###....R.....R.R..R.MMMMMM.R...
######################################################################################.VVVMMM.......RRR...RVVVVVVVVVVVVV...RR............R.MMMMMMM.MMM.MMMMM.RR........RRRR.RRMMMMMMMMMRRR...MMMMM......
######################################################################################R.VVVR..####R...R..R.R..VVVVVVVRVV...R.....R....R...R.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM......MMMMMMM...
########################################################################################..#############......R..VVVV.....R.....R....R..RRRR.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR....R.RR..MMMM
#####################################################################################################.R.R..R....RR......R...RR.RR..RR.RR....RMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR.....
##################################################################################################...R....RR.R....R.R..R..R...R.R............R...RRRRMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR.RR...
##################################################################################################RR..R.....R.R.....R...R.R.R..R.R.RR...RRR...R...MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM...RRR...
###################################################################################################R.R....RRRR.R.R.....................R.R.......RMMMMMMMMMMMMMMMMMMMMMM.R........RR............R......R
####################################################################################################..R...R..R.......R.R......R......R....R...R.R...........R...MMMMMR.......R..RR......R.......R.......
#########################################################################################################R.....R..R....RR........R....R.R...RR..R.......RR...R......RR....RRR....R.RR.RR...RR..RRR.....R
###############################################################################################################..R...R.....RRR...RR...R....R.....R..R...R.R....RR.......RR.....RRR.....RR....RR....RR...
######################################################################################################...R.R..R...RR..RRR...R.......R.R......RR.........R..R.....RR.R..R..R.........RRRR.....R....R.RR.R
#####################################################################################################.RR..R..R..R...R.RRR..R...RR.........RR..RR.....R..RR......RR.....RR........R.........R......R..R..
#####################################################################################################.....RRR....RR....RRR..RR...........R.R.....R.........R.RR.R...R.R....RRR...RRRR..RR...R...R.R.R...
####################################################################################################.R.....RR....R.R...R...R..R.......RR....R....RR..RR..RRR.R..RRRRR..RRR.R..R....R.................RR.
###################################################################################################.R..RR..RR.R..R..R...R.RR..RRR.RR.......R..........R...R..R.........R.R......RR.R....R..R.RR.RR....RR
##################################################################################################...MMM...R...R...R.R.......R.......RR..R...RR.R........R...RR.....R..R.RR.RRR.RR......RRR.............
##################################################################################################..MMMMM.R.RR............R...R.........RR.R.R..R.RR..R.RR..R.....R.....R........R.R......RRRR.R.RR.....
#################################################################################################R.MMMMMMMMMR.....R...........R.R..R...RRR...R.RRRR...R...RR......RRR..R....R...R.R..........R...R.R..R.
#################################################################################################.MMMMMMMMMMMRR.R...R...R..R...RR..R..R........R....R.RRR..R...RRR...R.RR.R...R.R...R...R.....RR.......R
#################################################################################################.MMMMMMMMMMM.R.......R.R.RR...R.R...R.RR.R...R..RR.R.R....R.RR..R....R............R.RR..R..R..R......RR
################################################################################################R...MMMMMMMR...R.......R....RR...RR...R....R.R............R..R..R.......R.RRR...RR....R....R...RR....R..
###############################################################################################R.RRR..MMMMRR....RR..R.......R......R..R..R.R..R..............RR..R.R.....R..R.R...R.RR..R.RR..R.RR...RR."""
 
 
def init_display():
    global screen, tile
    screen = pygame.display.set_mode((1800, 900))
    tile = pygame.image.load("agua#.png")
 
 
def tiles(map1):
    global tile
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "#":
                screen.blit(tile, (x * 16 , y * 16 ))
         
                
                
                
 
 
map1 = map1.splitlines()
pygame.init()
init_display()
loop = 1
while loop:
 
    # screen.fill((0, 0, 0))
    tiles(map1)
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
 
    pygame.display.update()
pygame.quit()