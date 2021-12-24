import random 
import math
import copy
sys_random = random.SystemRandom()
NUMBER_OF_SLOTS=4*18
MAX_HOBBITS=10
ROUNDS=5



def probability(delta,current_cost):
    if delta<0 or current_cost==0:
        return 1
    else:
        return math.exp( -delta / current_cost )


    


# Classe Level representa as etapas que serão percorridas e com isso as combinações geradas ao percorrer as etapas
class Level:
    max_walks=MAX_HOBBITS
    memoize_allowed={}
    memoize_denied={}
#inicializa com a lista dos niveis e hobbits
    def __init__(self,levels_list,hobbits_list,number_of_levels):
        self.levels=levels_list
        self.hobbits=hobbits_list
        self.number_of_levels=number_of_levels
        self.start_combination()
#inicializa as combinações vazias
    def start_combination (self):
        aux=self.random_combination()
        #print("start level\n")
        aux_cost=self.calculate_cost(aux)
        self.temp_combination=aux
        self.temp_cost=aux_cost
        self.best_combination=aux
        self.best_cost=aux_cost
        self.final_combination=aux
        self.final_cost=aux_cost

    def random_combination (self):
        slot=0
        hobbits=[self.max_walks]*4
        hobbits_levels=[0]*NUMBER_OF_SLOTS
        frodo=0
        sam=1
        merry=2
        pippin=3
        i=0
        while True:
            if i==68 and(hobbits[frodo]!=0 or hobbits[sam]!=0 or hobbits[merry]!=0 or hobbits[pippin]!=0):
                i=0
            ##print(i)
            if hobbits[frodo]>0:
                hobbits_levels[frodo+i]=sys_random.randint(0,1)
                if hobbits_levels[frodo+i]==1:
                    hobbits[frodo]-=1
            if hobbits[sam]>0:
                hobbits_levels[sam+i]=sys_random.randint(0,1)
                if hobbits_levels[sam+i]==1:
                    hobbits[sam]-=1
            if hobbits[merry]>0:
                hobbits_levels[merry+i]=sys_random.randint(0,1)
                if hobbits_levels[merry+i]==1:
                    hobbits[merry]-=1
            if hobbits[pippin]>0:
                hobbits_levels[pippin+i]=sys_random.randint(0,1)
                if hobbits_levels[pippin+i]==1:
                    hobbits[pippin]-=1
            if hobbits[frodo]==0 and hobbits[sam]==0 and hobbits[merry]==0 and hobbits[pippin]==0:
                break
            i+=4
        #    for hobbit_index in range(0,3):
      #          for numer_of_walks in range(0,7):
      #              hobbits_levels[slot%self.number_of_levels]=1
      #              slot+=1
        ##print (hobbits_levels)
        #print(" end random combination \n")
        return hobbits_levels
#confere se o vizinhogerado é válido     
    def check_possibility(self,neighbor):
        hobbit=[0,0,0,0]
        string_ints = [str(int) for int in neighbor]
        list_string="".join(string_ints)
        if neighbor==None:
            return False
        if list_string in self.memoize_allowed.keys():
            #print("allowed\n")
            return True
        if list_string in self.memoize_denied.keys():
            return False
        #else, we never seen this combination
        for i in range(0,len(neighbor)-3):
            hobbit[0]+=neighbor[i]
            hobbit[1]+=neighbor[i+1]
            hobbit[2]+=neighbor[i+2]
            hobbit[3]+=neighbor[i+3]
            total=hobbit[0]+hobbit[1]+hobbit[2]+hobbit[3]
            if total==0:
                self.memoize_denied[list_string]="d"
                return False        
            i+=4
        for j in range(0,len(hobbit)):
            if hobbit[j]>MAX_HOBBITS :    
                self.memoize_denied[list_string]="d"   
                return False
        self.memoize_allowed[list_string]="a"
        return True
                # 0 - 0 1 2 3
                # 1 - 4 5 6 7
                # 2 - 8 9 10 11
                # 3 - 12 13 14 15
                # 4 - 16 17 18 19
                # 5 - 20 21 22 23
                # 6 - 24 25 26 27
                # 7 - 28 29 30 31
                # 8 - 32 33 34 35
                # 9 - 36 37 38 39
                # 10- 40 41 42 43
                # 11- 44 45 46 47
                # 12- 48 49 50 51
                # 13- 52 53 54 55
                # 14- 56 57 58 59
                # 15- 60 61 62 63
                # 16- 64 65 66 67
                # 17- 68 69 70 71
#calcula o custo da combinação
    def calculate_cost(self,current):#calculates the total cost of said combination
        #print("calculate cost func\n")
        #print(current)
        total=0
        level_speed=[]
        hobbits_total_speed=1
        j=0
        level_index=0
        while j<len(current)-1:
           # #print("len current \n ")
            ##print(len(current))
            current_speed=0
            #index out of range
            hobbits_total_speed=current[j]*1.5+current[j+1]*1.4+current[j+2]*1.3+current[j+3]*1.2
            if hobbits_total_speed!=0:
                current_speed=self.levels[level_index]/hobbits_total_speed
            j+=4          
            level_index+=1    
            total+=current_speed
        level_speed.append(current_speed)# so para #print
        #print(total)
        return total
#gera vizinho/nova possibilidade
    def generate_neighbor(self):
        #print("Generate new neighbor\n")
        neighborhood_size=10
        i=0
        best_neighborhood=None
      #  best_function=None
        operations=[self.shift_hobbit,self.change_levels,self.move_walking_hobbit,
        self.random_combination,self.move_stopped_hobbit,self.swich_half]
        current_operation=sys_random.choice(operations)
        neighbor=current_operation()
        #print("new neighbot nenerated")
        neighbor_cost=self.calculate_cost(neighbor)
        while not self.check_possibility(neighbor) and neighbor_cost>self.temp_cost:
            #print("Not a valid neighbor, generate new\n ")
            current_operation=sys_random.choice(operations)
            neighbor=current_operation()
            neighbor_cost=self.calculate_cost(neighbor)
        #print(" achou novo vizinho")
        self.temp_combination=neighbor
        self.temp_cost=neighbor_cost
        return 
#retorna os hobbits naquele nível
    def which_level(self,level_list,chosen_level):
        return [level_list[(chosen_level*4)-4],
        level_list[(chosen_level*4)-3],
        level_list[(chosen_level*4)-2],
        level_list[(chosen_level*4)-1]]
#retorn quantos hobbits tem naquele nivel
    def count_on_level(self,level):
        total=0
        for i in range (0,3):
            if level[i]==1:
                total+=1
        return total
#limpa os campos/hobbits daquele nível
    def clear_level(self,level_list,chosen_level):
        level_list[(chosen_level*4)-5]=0
        level_list[(chosen_level*4)-4]=0
        level_list[(chosen_level*4)-3]=0
        level_list[(chosen_level*4)-2]=0
        level_list[(chosen_level*4)-1]=0
        return level_list
# conta o total de hobbits no percurso total
    def count_total_of_hobbits(self, levels_list):
        total=0
        for i in levels_list:
            if i==1:
                total+=1
        return total
# funcao auxiliar de gerar vizinho novo: move um hobbit tendo como base a melhor combinação encontrada
    def shift_hobbit(self):
        #print("func shift hobbit \n")
        best=None
        cost=None
        for i in range(0,ROUNDS):
            temp_hobbits=copy.deepcopy(self.final_combination) #current combination
            line = sys_random.randint(0,3)#max index hobbit
            random_level=sys_random.randint(1,self.number_of_levels)
            hobbit=None
            chosen_level=self.which_level(temp_hobbits,random_level)
            level_cost=self.count_on_level(chosen_level)
            if  level_cost>1:#line<level_cost and
                index=(random_level*4)-4+line
                hobbit=temp_hobbits[index]
                temp_hobbits[index]=0
            else:
            #    hobbit=chosen_level[] #i think this is wrong
                temp_hobbits=self.clear_level(temp_hobbits,random_level)
            if hobbit:
                while True:
                    new_index=random_level%self.count_total_of_hobbits(temp_hobbits)
                    new_chosen_level=self.which_level(temp_hobbits,new_index)
                    new_level_cost=self.count_on_level(new_chosen_level)
                    if new_level_cost<4 and temp_hobbits[index]==0:
                        temp_hobbits[i]=1
                        break
                    random_level=chosen_level+1
            #neighbor=simulated_annealing(self.levels,self.hobbits) #not really sure about this
            cost_neighbor=self.calculate_cost(temp_hobbits)
            if self.final_cost>cost_neighbor:
                best=temp_hobbits
                cost=cost_neighbor
            else:
                best=self.final_combination
                cost=self.final_cost
        temp_hobbits=best
        return temp_hobbits

# funcao auxiliar de gerar vizinho novo: swap de etapas tendo como base a melhor combinação encontrada
    def change_levels(self):
        #print("func change levels \n")
        best=None
        cost=None
        i=0
        while i<ROUNDS:
            temp_hobbits=copy.deepcopy(self.final_combination) 
            level_x=sys_random.randint(1,self.number_of_levels)
            level_y=sys_random.randint(1,self.number_of_levels)
            level_x_hobbits=self.which_level(temp_hobbits,level_x)
            level_y_hobbits=self.which_level(temp_hobbits,level_y)
            j=0
            for x in level_x_hobbits:
                temp_hobbits[(level_y*4)-4+j]=x
                j+=1
            k=0
            for y in level_y_hobbits:
                temp_hobbits[(level_x*4)-4+k]=y #
                k+=1

           # neighbor=simulated_annealing(self.levels,self.hobbits) 
            #cost_neighbor=self.calculate_cost(neighbor)
            cost_neighbor=self.calculate_cost(temp_hobbits)
            if self.final_cost>cost_neighbor:
                best=temp_hobbits
                cost=cost_neighbor
            else:
                best=self.final_combination
                cost=self.final_cost
            i+=1
        temp_hobbits=best
        return temp_hobbits
#retorna uma lista com os hobbits que ainda estão disponiveis pra andar. a disposição do array =[Frodo,Sam,Merry,Pippin]
    def find_not_tired_hobbit(self,neighbor):
        hobbit=[0,0,0,0]
        for i in range(0,len(neighbor)-3):
            hobbit[0]+=neighbor[i]
            hobbit[1]+=neighbor[i+1]
            hobbit[2]+=neighbor[i+2]
            hobbit[3]+=neighbor[i+3]       
            i+=4
        for i in hobbit:
            if i>=MAX_HOBBITS:
                i=0
            else:
                i=1
        return hobbit

# funcao auxiliar de gerar vizinho novo: move um hobbit que ainda pode andar tendo como base a melhor combinação encontrada
    def move_walking_hobbit(self):
        #print("func move walking hobbit\n")
        temp_hobbits=copy.deepcopy(self.final_combination)
        not_tired=self.find_not_tired_hobbit(temp_hobbits)
        not_walking=None
        for i in range(0,3):
            if i==1:
                not_walking=i
        resting_hobbit=sys_random.randint(0,3)
        while not_walking == resting_hobbit:
            resting_hobbit=sys_random.randint(0,3)
        levels_without_hobbits=[]
        #total_hobbits=self.count_total_of_hobbits(temp_hobbits)
        for i in range(self.number_of_levels): #verficar se nao reutiliza o i
            chosen_level=self.which_level(temp_hobbits,i)
            if 1== chosen_level[resting_hobbit] and self.count_on_level(chosen_level)<4:
                levels_without_hobbits.append(i)
        if not levels_without_hobbits:
            levels_without_hobbits=sys_random.randint(1,self.number_of_levels)
        else:
            levels_without_hobbits=sys_random.choice(levels_without_hobbits)#empty
        #gasta hobbit
        temp_hobbits[levels_without_hobbits*4-4+resting_hobbit]=1
        return temp_hobbits # n fiz o sa


    def move_stopped_hobbit(self):
        #print("func move stopped hobbit\n")
        temp_hobbits=copy.deepcopy(self.final_combination)
        random_hobbit_index=sys_random.randint(0,3)
        random_level=sys_random.randint(1,self.number_of_levels)
        level_count=1
        random_hobbit_status=temp_hobbits[(random_level-1)*4+random_hobbit_index]
        available_hobbits=self.find_not_tired_hobbit(temp_hobbits)#verifica se ele ainda pode andar
        if random_hobbit_status==0:# hobbit esta parado
            if available_hobbits[random_hobbit_index]==0:# se ele nao pode andar, tem que tirar de algum lugar
                i=0
                while i<len(temp_hobbits)-1:
                    if level_count!=random_level: # nao pode remover de onde queremos adicionar verifica o nivel
                        if temp_hobbits[i*4]==1: #acha um lugar que ele esta andando
                            temp_hobbits[(random_level-1)*4+random_hobbit_index]=1
                            temp_hobbits[i*4]=0
                            i=len(temp_hobbits)
            else:#se ele pode andar, adiciona ali
                temp_hobbits[(random_level-1)*4+random_hobbit_index]=1
        return temp_hobbits

    def swich_half(self):
        #print("func swich half\n")
        temp_hobbits=copy.deepcopy(self.final_combination)
        half_one=temp_hobbits[:len(temp_hobbits)//2]
        half_two=temp_hobbits[len(temp_hobbits)//2:]
        temp_hobbits=half_two+half_one
        return temp_hobbits












    
def simulated_annealing(walk_to_mordor:Level):
    print("Start Simmulated Annealing\n")
    delta=0
    start_temperature=100.0
    goal_temperature=.1
    cooling_rate=1
    while start_temperature>goal_temperature:
        for i in range (0,20):#iteractions
            walk_to_mordor.generate_neighbor()  #add to temp
            #print("calculate cost SA primeiro\n")
          # walk_to_mordor.best_cost=Level.calculate_cost(walk_to_mordor.best_combination)
            delta=walk_to_mordor.temp_cost-walk_to_mordor.best_cost        
            if delta<0:
                walk_to_mordor.best_combination=walk_to_mordor.temp_combination
                walk_to_mordor.best_cost=walk_to_mordor.temp_cost
        # conferir probabilidade
            elif probability(delta,walk_to_mordor.best_cost)>=(random.uniform(0,100)/100):
                walk_to_mordor.best_combination=walk_to_mordor.temp_combination
                walk_to_mordor.best_cost=walk_to_mordor.best_cost
            #print("calculate cost SA depois elif \n")
            if walk_to_mordor.best_cost<walk_to_mordor.final_cost:
                print("found best final_cost\n")
                walk_to_mordor.final_combination=walk_to_mordor.best_combination
                walk_to_mordor.final_cost=walk_to_mordor.best_cost  
        start_temperature-=cooling_rate
    return walk_to_mordor





hobbits_name=["frodo","sam", "merry", "pippin"]
hobbits_speed=[1.5,1.4,1.3,1.2]
#hobbits={"frodo": 1.5,"sam": 1.4, "merry": 1.3, "pippin":1.2}
#levels={1:0, 2:10, 3:30, 4:60, 5:65, 6:70, 7:75, 8:80, 9:85, 10:90, 11:95, 12:100, 13:110, 14:120, 15:130, 16:140, 17:150 ,18:0}
level_difficulty=[0,10,30,60,65,70,75,80,85,90,95,100,110,120,130,140,150,0]
number_of_levels=18
class_instance=Level(level_difficulty,hobbits_speed,number_of_levels)
simulated_annealing(class_instance)
#print(class_instance.best_cost)
#print(class_instance.final_cost)
#print("out \n")
formatted_float = "{:.2f}".format(class_instance.final_cost)
print("Melhor custo "+ formatted_float)
#imprime_bonito(melhor_combinacao,level_difficulty,hobbits_name)

