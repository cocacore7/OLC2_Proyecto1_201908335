from Enum.typeExpression import typeExpression

Dominant = [
                #STRING                     #INTEGER                    #FLOAT                      #BOOL                       #CHAR                   #NULO
    #STRING
    [   
                typeExpression.STRING,      typeExpression.STRING,      typeExpression.STRING,      typeExpression.ERROR,       typeExpression.ERROR,   typeExpression.ERROR
    ],
    #INTEGER
    [
                typeExpression.STRING,      typeExpression.INTEGER,     typeExpression.FLOAT,       typeExpression.INTEGER,     typeExpression.CHAR,    typeExpression.ERROR
    ],
    #FLOAT
    [
                typeExpression.STRING,      typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.ERROR,   typeExpression.ERROR
    ],
    #BOOL
    [
                typeExpression.STRING,      typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.INTEGER,     typeExpression.CHAR,    typeExpression.ERROR
    ],
    #CHAR
    [
                typeExpression.STRING,      typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.CHAR,        typeExpression.ERROR,   typeExpression.ERROR
    ],
    #NULO
    [
                typeExpression.ERROR,       typeExpression.ERROR,       typeExpression.ERROR,       typeExpression.ERROR,       typeExpression.ERROR,   typeExpression.ERROR
    ]
]   