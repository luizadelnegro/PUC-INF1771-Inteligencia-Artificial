import pygame
from pygame.draw import line
import sa
import a_estrela
import time


SCREEN_WIDTH=1800
SCREEN_HEIGHT=600
WIDTH=7
HEIGHT=7
MARGIN=1
ROWS=71
COLUMNS=200
FPS=60
MAPA='/home/luiza/Documents/Git/t1-senhor-dos-aneis-time-time/mapa5.txt'
CAMINHO=(255,0,0)
dict_cor={'.': (128,128,128),#cinza
        'R':(51,25,0),# marrom 
        'V':(0,51,0),#verde escuro
        'M':(51,51,0),
        'P':(0,0,0),#preto
        '#':(0,0,128),#azul
        'I': (255,255,0),#amaelo
        '1': (255,255,0)#amarelo
        } #etapa fucsia#caminho =vermelho
class Board:
    def __init__(self,mapa):
        self.file_name=mapa
        self.board=self.read_from_file(mapa)
        self.board_colors=[]
       

## INICIALIZA O MAPA##
    def read_from_file(self,map):
        try:
            file = open('mapa5.txt', 'r')
        except:
            exit(1)
        new_map,start,finish = self.read_map(file)
        file.close()
        return new_map

    def read_map(self,file):
        new_map=self.start_empty_map(COLUMNS,ROWS)
        start=[]#[width, height]
        finnish=[]
        for i in range(ROWS):
            line=file.readline()
            for j in range(COLUMNS):
                new_map[i][j]=line[j]
                if new_map[i][j]=="1":
                    start.append(i)
                    start.append(j)
                if new_map[i][j]=="I":
                    finnish.append(i)
                    finnish.append(j)
        #print(start)
        #print(finnish)
        return new_map,start,finnish

    def start_empty_map(self,width,height):
        new_map = []
        for i in range(height):
            new_map.append([])
            for j in range(width):
                new_map[i].append(0)
        return new_map


## DESENHA

    def draw_map(self,screen):
        screen.fill((0,0,0))
        mapa_aux=self.board
        linhas=len(self.board)
        colunas=len(self.board[0])
        for i in range(linhas):
            for j in range(colunas):
                element=mapa_aux[i][j]
                cor=dict_cor.get(element,(153,0,153))
                pygame.draw.rect(screen,cor,[(MARGIN+WIDTH)*j+MARGIN,(MARGIN+HEIGHT)*i+MARGIN,WIDTH,HEIGHT])
        pygame.display.flip()

    def show_path(self,screen,path):
        print("show_path")
        level=0
        for i in path:
            for j in range(len(i)):
                time.sleep(0.2)
                self.print_ponto(screen,i[j].x,i[j].y)


    def print_ponto(self,screen,linha,coluna):
        pygame.event.get()
        pygame.draw.rect(screen, (255,0,0),[(MARGIN+WIDTH) * linha + MARGIN,(MARGIN + HEIGHT) * coluna + MARGIN, WIDTH, HEIGHT])
        pygame.display.flip()

def main():
    hobbits_speed=[1.5,1.4,1.3,1.2]
    level_difficulty=[0,10,30,60,65,70,75,80,85,90,95,100,110,120,130,140,150,0]
    number_of_levels=18
    
    #a estrela
    print("Inicio A*\n")
    middle_earth = a_estrela.terra_media('mapa5.txt')
    middle_earth.extrair_mapas()
    final_path=middle_earth.calcula_caminho()
    print("Fim A*\n")

    print("Ini S.A")
    #sim annealing
    class_instance=sa.Level(level_difficulty,hobbits_speed,number_of_levels)
    sa.simulated_annealing(class_instance)
    print("Fim S.A")
    formatted_float = "{:.2f}".format(class_instance.final_cost)
    print("Melhor custo "+ formatted_float)


    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('TRAB 1 IA')
    
    board=Board(MAPA)
    board.draw_map(screen)
    board.show_path(screen,final_path)

    return

main()


