m  = 'muro'
p  = 'ponto'
v  = 'vacuo'
c  = 'caminho'
f  = 'fim'
i  = 'inicio'
e  = 'espinho'
MAPA1 = [
   
    [v , v , v , v , v , v , v , v , v , m , m , m , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , m , f , m , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , m , p , m , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , m , p , m , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , m , p , m , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , m , p , m , v , v , v , v , v ],
    [v , v , v , v , v , v , m , m , m , m , p , m , v , v , v , v , v ],
    [v , v , v , v , v , v , m , p , p , p , p , m , v , v , v , v , v ],
    [v , v , v , v , v , v , m , p , c , m , m , m , v , v , v , v , v ],
    [v , v , v , v , v , v , m , p , c , m , m , v , v , v , v , v , v ],
    [v , v , v , v , v , v , m , p , p , p , m , v , v , v , v , v , v ],
    [v , v , v , v , v , v , m , m , m , p , m , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , m , p , m , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , m , p , m , v , v , v , v , v , v ],
    [v , v , v , v , v , v , m , m , m , p , m , m , m , v , v , v , v ],
    [v , v , v , v , v , v , m , p , p , p , p , p , m , v , v , v , v ],
    [v , v , v , v , v , v , m , p , c , p , m , p , m , v , v , v , v ],
    [v , v , v , v , v , v , m , p , c , p , m , p , m , v , v , v , v ],
    [v , v , v , v , v , v , m , p , p , p , m , p , m , v , v , v , v ],
    [v , v , v , m , m , m , m , m , m , m , m , p , m , v , v , v , v ],
    [v , v , v , m , p , p , p , p , m , v , m , p , m , v , v , v , v ],
    [v , v , v , m , p , m , m , p , m , m , m , p , m , v , v , v , v ],
    [v , v , v , m , p , m , m , p , p , p , p , p , m , v , v , v , v ],
    [v , v , v , m , p , m , m , m , m , m , m , m , m , v , v , v , v ],
    [m , m , m , m , p , m , m , m , m , m , m , m , m , m , m , m , m ],
    [m , p , p , p , p , p , p , p , p , p , m , m , p , p , p , p , m ],
    [m , p , c , c , p , m , m , m , m , p , p , p , p , c , c , p , m ],
    [m , p , c , c , p , m , v , v , m , m , m , m , m , c , c , p , m ],
    [m , p , p , p , p , m , v , v , v , m , c , c , c , c , c , p , m ],
    [m , m , m , m , m , m , v , v , v , m , c , c , c , c , c , p , m ],
    [v , v , v , v , v , v , v , v , v , m , c , c , c , c , i , p , m ],
    [v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , m ],
]

MAPA2 = [
    [v , v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , m , m , m , m , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , m , m , m , m , p , p , p , p , m , m , p , p , p , m , m , v , v ],
    [v , v , v , v , v , v , v , v , v , v , m , p , p , p , p , p , p , p , m , m , p , m , p , m , m , v , v ],
    [v , v , v , v , v , v , v , v , v , v , m , p , m , m , p , c , c , p , m , p , p , m , p , m , m , m , m ],
    [v , v , v , v , v , v , v , v , v , m , m , p , m , m , p , p , p , p , m , p , p , p , p , p , p , m , m ],
    [v , v , v , v , v , v , v , v , v , m , p , p , m , m , p , m , m , m , m , p , c , c , c , c , p , m , m ],
    [m , m , m , m , m , m , m , v , v , m , p , m , m , m , p , p , p , p , p , p , p , p , p , p , p , m , m ],
    [m , c , c , c , c , c , m , v , v , m , p , m , v , m , m , m , m , p , p , p , p , p , p , p , p , m , v ],
    [m , c , c , c , c , c , m , v , v , m , p , m , v , v , v , v , m , m , m , m , m , m , p , m , m , m , v ],
    [m , c , c , i , c , c , m , v , v , m , p , m , m , m , m , m , m , m , m , m , m , m , p , m , v , v , v ],
    [m , m , m , m , m , p , m , v , v , m , p , p , p , m , p , p , p , p , p , p , m , m , p , m , m , m , v ],
    [v , v , v , v , m , p , m , m , m , m , m , m , p , m , p , c , c , p , c , p , m , m , p , m , f , m , v ],
    [v , v , v , v , m , p , m , m , p , p , p , m , p , m , p , c , c , p , c , p , m , m , p , m , p , m , v ],
    [v , v , v , v , m , p , m , m , p , c , p , m , p , m , p , c , c , p , c , p , m , m , p , p , p , m , v ],
    [v , v , v , v , m , p , p , p , p , p , p , m , p , p , p , p , p , p , p , p , m , m , m , m , m , m , v ],
    [v , v , v , v , m , m , m , m , p , m , m , m , m , m , p , c , c , p , m , m , m , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , m , p , p , p , p , p , m , p , c , c , p , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , m , m , m , m , m , p , p , p , p , p , p , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , m , m , p , p , p , p , p , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , v , v , v , v , v , v , v , v ]
]

MAPA3 = [
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , m , m , v , v , v , v , v ,  v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , p , p , p , m , p , p , p , m , m , m , m , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , m , m , m , f , m , p , m , p , m , p , m , p , p , p , p , m , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , m , p , p , p , p , p , m , p , p , p , m , m , m , m , p , m , v , v , v , v , v , v , v ],
    [v , m , m , m , m , m , v , v , v , v , m , p , c , p , c , m , m , m , m , m , m , m , e , m , p , m , v , v , v , v , v , v , v ],
    [v , m , p , p , p , m , m , m , m , m , m , p , m , p , p , p , p , p , m , v , m , p , p , m , p , m , v , v , v , v , v , v , v ],
    [m , m , p , m , p , p , p , p , m , p , p , p , m , p , m , m , m , p , m , v , m , p , p , p , p , m , v , v , v , v , v , v , v ],
    [m , p , p , m , p , p , m , p , m , p , m , m , m , p , m , m , p , p , m , m , m , p , m , m , m , m , m , m , m , v , v , v , v ],
    [m , p , m , m , m , p , p , p , p , p , m , v , m , p , m , p , p , m , m , m , p , p , m , p , p , p , p , m , m , v , v , v , v ],
    [m , p , m , m , m , m , m , m , m , m , m , m , m , m , m , p , p , m , v , m , p , m , m , p , m , m , p , m , m , v , v , v , v ],
    [m , p , p , p , m , v , v , v , v , v , v , m , p , p , p , p , m , m , v , m , p , p , p , p , p , p , p , m , m , v , v , v , v ],
    [m , m , m , p , m , m , m , m , m , m , m , m , p , m , p , p , m , v , v , m , m , m , m , m , m , p , m , m , v , v , v , v , v ],
    [v , e , p , p , p , m , p , p , p , p , p , p , p , m , m , m , m , v , v , v , v , v , m , p , p , p , m , v , v , v , v , v , v ],
    [v , m , p , m , p , m , p , m , p , m , m , m , m , m , v , v , v , v , v , v , v , v , m , p , m , m , m , v , v , v , v , v , v ],
    [v , m , p , p , p , p , p , p , p , m , v , v , v , v , v , v , v , v , m , e , e , e , e , p , m , v , v , v , v , v , v , v , v ],
    [v , m , m , m , m , m , m , m , m , m , v , v , v , v , v , v , v , v , m , c , c , c , c , c , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , c , c , c , c , c , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , c , c , i , c , c , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , v , v , v , v , v , v , v , v ]    
]

MAPAX = [
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v]
]