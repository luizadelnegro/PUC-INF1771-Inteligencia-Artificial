% Utilizaremos uma estrutura de arvore, como exemplificado no enunciado.
% Para a direita, respostas positivas, para a esquerda, respostas
% negativas.
% Toda arvore começa com uma raiz(root) que se desrincha em ramos
% (branches) até seu fim, que são as folhas(leaf).
% Utilizarei a conotação de direita/esquerda para facilitar.
% exemplificando, cada elemento que vai para a direita erá sua estrutura
% e seu caminho, que levará as folhas correspondentes. O mesmo ocorre
% para a direita.
% TO DO: SALvAR usando listing, tell e told
% TO DO: Extrair a logica de verificar com a func verify do exemplo prof
% TO DO: separar palavras com _ nesse arquivo e no txt para melhor
% clareza inicializa branches e leaves

% importação de listing 
:- use_module(library(listing)).

% todos os ramos SIM (esquerda)
:- dynamic leftbranch/2.
% todas as folhas SIM (esquerda)
:- dynamic leftleaf/2.
% todos os ramos NAO (direita)
:- dynamic rightbranch/2.
% todos as folhas NAO (direita)
:- dynamic rightleaf/2.

:- dynamic root/1.

% Recebe o nó em questão e a resposta do jogador
analyse(Node,Answer):-
    write(Node),
    nl,
    read(Answer),
    nl,
    (
        (Answer=yes,nl);
        (Answer=no,nl)
    ).
% percorre arvore de acordo com as respostas
whichnode(Node,Next):-
    write(Node),
    nl,
    read(Answer),
    nl,
    (
        (Answer=yes,leftbranch(Node,NextNode),whichnode(NextNode,Next),!);
        (Answer=yes,not(leftbranch(Node,_)),leftleaf(Node,Next),!);
        (Answer=no,rightbranch(Node,NextNode),whichnode(NextNode,Next),!);
        (Answer=no,not(rightbranch(Node,_)),rightleaf(Node,Next),!)
    ).


% add novo animal a arvore

% salva a base  de dados do jogo
salvar_base:-
	
	tell('arquivoboladao.txt'),
	listing([root,leftbranch,leftleaf,rightbranch,rightleaf]),
	told.

% aprende novos animais

learn(Current):-
    write("Teach me your ways! Which animal it was?"),
    nl,
    read(Animal),
    write("Which question can I make to identify this animal from the previous one?"),
    nl,
    read(Question),
    write("Just to confirm..."),
    write(Question),
    nl,
    read(YesNo),
    (
        (
        leftleaf(Old,Current),
        retract(leftleaf(Old,Current)),
        assertz(leftbranch(Old,Question))
        );
        (
        rightleaf(Old,Current),
        retract(rightleaf(Old,Current)),
        assertz(rightbranch(Old,Question))
        )
    ),
    (
        (YesNo=yes,
        assertz(leftleaf(Question,Animal)),
        assertz(rightleaf(Question,Current))
        );
        (YesNo=no,
        assertz(rightleaf(Question,Animal)),
        assertz(leftleaf(Question,Current))
        )
    ).



% start game - consulta memória
start:- consult('arquivoboladao.txt').

% main loop - Como no exemplo do ead
run:- start,
    write("Welcome to the animal guessing game!"),
    write("Me, the amazing computer, will try to guess which animal you are thinking"),
    write("I'll make the questions and you should answer only with 'yes.' or 'no.'."),
    nl,
    root(StartPoint),
    whichnode(StartPoint, Answer),
    analyse(Answer,Score),
    (
        (Score=yes, write("YAY! I am truly amazing!"),nl,nl);
        (Score=no,  write("Oops I did it again!"),learn(Answer),nl,salvar_base)
    ).
