grammar reentrancy;

// Parser Rules
sourceUnit: (pragmaDirective | importDirective | contractDefinition)* EOF;

contractDefinition:
    ('contract' | 'interface' | 'library') IDENTIFIER
    ('is' inheritanceSpecifier (',' inheritanceSpecifier)*)?
    '{' contractPart* '}';

contractPart:
    stateVariableDeclaration
    | functionDefinition
    | modifierDefinition
    | eventDefinition
    | vulnerabilityPattern;

vulnerabilityPattern:
    reentrancyPattern
    | integerOverflowPattern
    | uncheckedCallPattern
    | unsafeTransferPattern
    | gasSensitiveOperation;

// Non-left-recursive patterns
reentrancyPattern:
    externalCall (stateUpdateAfterCall | noReentrancyGuard);

stateUpdateAfterCall:
    '{' (statement)* externalCall (statement)* stateUpdate (statement)* '}';

noReentrancyGuard:
    'function' IDENTIFIER parameterList modifierList? returnParameters? 
    '{' (statement)* externalCall (statement)* '}';

integerOverflowPattern:
    arithmeticOperator expressionWithoutSafeMath;

expressionWithoutSafeMath:
    primaryExpression (arithmeticOperator primaryExpression)*;

uncheckedCallPattern:
    lowLevelCall (uncheckedResult | noResultCheck);

unsafeTransferPattern:
    transferOrSend (uncheckedResult | noResultCheck);

gasSensitiveOperation:
    'for' '(' (statement)? ';' expression ';' (statement)? ')' 
    '{' (statement)* (externalCall | transferOrSend) (statement)* '}';

// Base expressions without left recursion
primaryExpression:
    IDENTIFIER
    | NUMBER
    | '(' expression ')'
    | STRINGLITERAL;

expression:
    primaryExpression
    | expression arithmeticOperator expression
    | expression comparisonOperator expression
    | expression logicalOperator expression;

statement:
    expression ';'
    | variableDeclaration ';'
    | '{' statement* '}'
    | ifStatement
    | forStatement
    | whileStatement;

// Base Solidity components
pragmaDirective: 'pragma' IDENTIFIER VERSION ';';
importDirective: 'import' STRINGLITERAL ';';
functionDefinition: 'function' IDENTIFIER parameterList modifierList? returnParameters? block;
stateVariableDeclaration: typeName IDENTIFIER ('=' expression)? ';';
modifierDefinition: 'modifier' IDENTIFIER parameterList? block;
eventDefinition: 'event' IDENTIFIER eventParameterList ';';
parameterList: '(' (parameter (',' parameter)*)? ')';
returnParameters: 'returns' parameterList;
block: '{' statement* '}';

// Lexer Rules
// Vulnerability indicators
EXTERNAL_CALL: '.call' | '.send' | '.transfer' | '.call.value';
UNCHECKED: 'unchecked' '{';
ARITHMETIC_OP: '+=' | '-=' | '*=' | '/=' | '++' | '--' | '+' | '-' | '*' | '/' | '**';
COMPARISON_OP: '==' | '!=' | '<' | '>' | '<=' | '>=';
LOGICAL_OP: '&&' | '||' | '!';
UNSAFE_MATH: ARITHMETIC_OP ~'SafeMath';

// Standard Solidity lexer rules
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
VERSION: [0-9]+ '.' [0-9]+ '.' [0-9]+;
STRINGLITERAL: '"' .*? '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;

// Fragments for complex patterns
fragment arithmeticOperator: ARITHMETIC_OP;
fragment comparisonOperator: COMPARISON_OP;
fragment logicalOperator: LOGICAL_OP;
fragment externalCall: EXTERNAL_CALL '(' argumentList? ')';
fragment lowLevelCall: '.call' '(' argumentList? ')';
fragment transferOrSend: ('.transfer' | '.send') '(' argumentList ')';
fragment stateUpdate: IDENTIFIER '=' expression;
fragment uncheckedResult: ~('require' | 'if' | 'assert');
fragment noResultCheck: ~('success' | 'require' | 'if' | 'assert');
fragment argumentList: expression (',' expression)*;
fragment ifStatement: 'if' '(' expression ')' statement ('else' statement)?;
fragment forStatement: 'for' '(' (statement)? ';' expression ';' (statement)? ')' statement;
fragment whileStatement: 'while' '(' expression ')' statement;
fragment variableDeclaration: typeName IDENTIFIER ('=' expression)?;
fragment typeName: 'uint' | 'int' | 'address' | 'bool' | 'string' | IDENTIFIER;
fragment parameter: typeName ('storage' | 'memory')? IDENTIFIER?;
fragment eventParameterList: '(' (eventParameter (',' eventParameter)*)? ')';
fragment eventParameter: typeName 'indexed'? IDENTIFIER?;
fragment modifierList: (modifierInvocation | stateMutability)*;
fragment modifierInvocation: IDENTIFIER ('(' argumentList? ')')?;
fragment stateMutability: 'pure' | 'view' | 'payable';
fragment inheritanceSpecifier: IDENTIFIER ('(' argumentList? ')')?;