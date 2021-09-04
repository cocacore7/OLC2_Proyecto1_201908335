from Enum.typeExpression import typeExpression

Dominant = [
                #STRING                     #INTEGER                    #FLOAT                      #BOOL                       #CHAR
    #STRING
    [   
                typeExpression.STRING,      typeExpression.STRING,      typeExpression.STRING,      typeExpression.ERROR,       typeExpression.ERROR
    ],
    #INTEGER
    [
                typeExpression.STRING,      typeExpression.INTEGER,     typeExpression.FLOAT,       typeExpression.INTEGER,     typeExpression.CHAR
    ],
    #FLOAT
    [
                typeExpression.STRING,      typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.ERROR
    ],
    #BOOL
    [
                typeExpression.STRING,      typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.INTEGER,     typeExpression.CHAR
    ],
    #CHAR
    [
                typeExpression.STRING,      typeExpression.FLOAT,       typeExpression.FLOAT,       typeExpression.CHAR,        typeExpression.ERROR
    ]
]   