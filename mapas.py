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
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , m , m , v , v , v , v , v , v , v , v , v , v ],
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
    [v , m , i , p , p , p , p , p , p , m , v , v , v , v , v , v , v , v , m , e , e , e , e , p , m , v , v , v , v , v , v , v , v ],
    [v , m , m , m , m , m , m , m , m , m , v , v , v , v , v , v , v , v , m , c , c , c , c , c , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , c , c , c , c , c , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , c , c , c , c , c , m , v , v , v , v , v , v , v , v ],
    [v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , v , m , m , m , m , m , m , m , v , v , v , v , v , v , v , v ]    
]

MAPA3 = [
    [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, v, v, v, v, v, v, v, v, m, m, m, m, m, m, m, v, v, v, v, v, v, v],
    [m, f, p, p, p, p, p, p, p, m, p, m, p, p, m, p, p, m, m, m, m, m, m, m, m, m, m, p, p, p, p, p, m, m, m, m, m, m, v, v],
    [m, m, m, m, m, p, m, m, p, m, p, m, p, p, m, m, p, p, p, p, p, p, p, p, p, p, p, p, m, m, m, p, p, p, p, p, p, m, m, v],
    [m, p, p, p, m, p, m, p, p, p, p, e, p, p, p, p, m, m, m, m, m, m, m, m, m, m, m, m, m, p, p, m, m, m, m, m, p, p, m, m],
    [m, p, m, p, m, p, m, m, m, m, m, p, m, m, p, p, m, p, p, p, p, p, p, p, p, p, p, p, m, p, p, p, p, p, p, m, m, p, p, m],
    [m, p, m, p, m, p, p, p, p, p, m, p, p, p, m, p, m, m, m, m, m, m, m, m, m, m, m, p, m, p, m, m, m, m, p, p, m, p, p, m],
    [m, p, m, p, m, m, m, m, m, p, m, p, p, p, m, p, p, p, p, p, p, p, p, p, p, p, m, p, m, p, m, p, p, e, m, p, m, m, p, m],
    [m, p, m, p, p, p, p, p, p, p, e, m, m, m, m, m, m, m, m, m, p, m, m, m, p, m, m, p, m, p, m, p, m, m, m, p, m, p, p, m],
    [m, p, m, m, m, m, m, m, m, p, p, p, p, p, m, e, p, p, p, p, p, m, e, p, p, m, p, p, m, p, m, p, m, p, p, p, m, m, p, m],
    [m, p, m, p, p, p, p, p, m, m, m, m, m, p, m, m, m, m, m, m, m, m, m, m, m, m, p, m, m, p, m, p, m, p, p, m, p, p, p, m],
    [m, p, m, p, e, p, p, p, p, p, p, p, m, p, m, p, p, p, p, p, p, m, p, m, e, m, p, p, p, p, p, p, m, p, m, p, p, m, p, m],
    [m, p, m, p, e, m, m, m, m, m, m, p, m, p, m, p, m, m, m, m, p, m, p, m, p, m, p, m, m, m, m, m, m, p, m, e, e, m, p, m],
    [m, p, m, p, e, m, p, p, p, p, p, p, m, p, m, p, m, p, e, m, p, m, p, m, m, m, p, m, p, p, p, p, p, p, p, m, m, m, p, m],
    [m, p, m, p, e, m, p, e, p, p, m, m, m, p, m, p, m, p, e, m, p, m, p, p, p, m, p, m, p, m, m, m, m, m, m, m, p, p, p, m],
    [m, p, m, p, e, m, p, p, p, m, p, p, p, p, m, p, m, p, e, m, p, m, p, m, p, m, p, m, p, m, p, p, p, p, p, p, p, m, m, m],
    [m, p, m, p, e, m, p, p, m, p, p, m, p, m, m, p, m, p, e, m, p, m, p, m, p, p, p, m, p, m, p, p, m, p, m, m, p, m, p, m],
    [m, p, m, p, e, m, p, m, p, p, m, p, p, m, c, m, m, p, m, m, p, m, p, m, m, m, m, m, p, m, m, p, m, p, m, p, p, m, p, m],
    [m, p, m, p, e, m, m, p, p, m, p, p, m, p, p, p, m, p, p, p, p, m, p, p, p, p, p, p, p, e, m, p, m, p, m, m, p, m, p, m],
    [m, p, m, p, e, m, p, p, m, m, p, m, p, p, p, p, m, m, m, m, m, m, p, m, p, m, m, m, m, m, p, p, m, p, m, p, p, m, p, m],
    [m, p, m, p, e, m, p, m, p, p, p, p, p, p, c, p, p, m, p, p, p, m, p, m, p, m, p, p, p, m, p, m, m, m, m, p, m, m, p, m],
    [e, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, m],
    [m, p, m, p, m, p, e, m, p, m, p, m, p, p, p, p, p, m, p, m, p, m, e, m, p, p, p, m, p, m, p, m, m, m, m, m, m, m, p, m],
    [m, p, m, p, m, p, m, m, p, m, p, m, p, m, m, m, m, m, p, m, p, m, m, p, p, m, m, m, p, m, p, p, p, p, p, p, p, m, p, m],
    [m, p, m, p, m, p, p, p, p, m, p, m, p, m, e, m, e, m, p, m, p, p, p, p, m, m, p, p, p, m, m, m, m, p, m, m, m, m, p, m],
    [m, p, m, p, m, m, p, m, p, m, p, m, p, p, p, p, p, p, p, m, m, m, m, m, m, p, p, m, p, p, p, e, m, p, m, p, p, p, p, m],
    [m, p, m, p, m, p, p, m, p, m, p, m, m, m, p, m, p, m, m, m, p, p, p, p, p, p, m, m, m, m, m, m, m, p, m, p, m, m, m, m],
    [m, p, m, p, m, p, m, m, p, m, p, m, p, p, p, p, p, p, p, m, p, m, m, m, m, p, p, e, m, p, p, p, m, p, m, p, p, p, p, m],
    [m, p, m, p, m, p, p, m, p, p, p, m, p, m, p, m, p, m, p, m, p, p, p, p, p, m, m, m, m, p, m, p, m, p, m, m, m, p, p, m],
    [m, p, m, p, m, m, p, m, m, m, m, m, p, m, p, m, p, m, p, m, m, m, m, m, p, p, m, e, m, p, m, p, p, p, p, p, m, e, e, m],
    [m, p, m, p, m, p, p, p, p, p, p, m, p, m, p, m, p, m, p, p, p, p, p, m, m, p, m, p, m, p, m, m, m, m, m, p, m, m, m, m],
    [m, p, m, p, m, p, m, m, m, m, p, m, p, m, p, m, p, m, m, m, m, m, p, p, p, p, m, p, p, p, p, p, p, p, m, p, p, p, p, m],
    [m, p, m, p, m, p, p, p, p, m, p, m, p, m, p, p, p, p, p, p, p, e, m, m, m, m, m, p, m, m, m, m, m, p, m, m, m, m, p, m],
    [m, p, m, p, m, p, m, m, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p, p, m, m, p, p, p, p, m, v, m, p, p, p, p, m, p, m],
    [m, p, m, p, m, p, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p, p, m, m, p, m, m, p, p, m, m, m, m, m, p, m, p, m],
    [m, p, m, p, m, m, m, m, p, m, p, m, p, p, p, p, p, m, p, m, p, m, p, p, p, p, p, e, m, m, p, m, p, p, p, m, p, m, p, m],
    [m, p, m, p, p, p, p, p, p, m, p, m, m, m, m, m, m, m, p, m, p, p, m, p, m, m, m, p, p, m, p, m, p, m, p, p, p, m, p, m],
    [m, p, m, p, m, m, m, m, m, m, p, m, e, p, p, p, p, p, p, m, m, p, p, p, m, p, p, p, p, p, p, m, p, m, m, m, m, m, p, m],
    [m, p, p, p, p, p, p, p, p, p, p, m, m, m, m, m, m, m, m, m, m, m, m, m, p, p, p, p, m, m, m, m, p, m, p, p, p, m, i, m],
    [m, e, m, m, m, m, m, m, m, m, p, p, p, p, p, p, p, p, p, p, p, p, p, p, p, m, m, m, m, m, p, p, p, p, p, m, m, p, m, m],
    [m, m, m, v, v, v, v, v, v, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, v, v, v, m, m, m, m, m, m, m, m, m, m, m],

]