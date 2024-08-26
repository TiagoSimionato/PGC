CALCULATOR_UI_INFO = f'''{{'buttons': [{{'text': 'DEG', 'tag_name': 'degree mode'}}, {{'text': 'INV', 'tag_name': 'show inverse functions'}}, {{'text': 'RAD', 'tag_name': 'switch to radians'}}, {{'text': 'sin', 'tag_name': 'sine'}}, {{'text': 'cos', 'tag_name': 'cosine'}}, {{'text': 'tan', 'tag_name': 'tangent'}}, {{'text': '%', 'tag_name': 'percent'}}, {{'text': 'ln', 'tag_name': 'natural logarithm'}}, {{'text': 'log', 'tag_name': 'logarithm'}}, {{'text': '√', 'tag_name': 'square root'}}, {{'text': '^', 'tag_name': 'power'}}, {{'text': 'π', 'tag_name': 'pi'}}, {{'text': 'e', 'tag_name': "Euler's number"}}, {{'text': '(', 'tag_name': 'left parenthesis'}}, {{'text': ')', 'tag_name': 'right parenthesis'}}, {{'text': '!', 'tag_name': 'factorial'}}, {{'text': '7', 'tag_name': None}}, {{'text': '8', 'tag_name': None}}, {{'text': '9', 'tag_name': None}}, {{'text': '4', 'tag_name': None}}, {{'text': '5', 'tag_name': None}}, {{'text': '6', 'tag_name': None}}, {{'text': '1', 'tag_name': None}}, {{'text': '2', 'tag_name': None}}, {{'text': '3', 'tag_name': None}}, {{'text': '0', 'tag_name': None}}, {{'text': '.', 'tag_name': 'point'}}, {{'text': '÷', 'tag_name': 'divide'}}, {{'text': '×', 'tag_name': '×'}}, {{'text': '−', 'tag_name': 'minus'}}, {{'text': '+', 'tag_name': 'plus'}}, {{'text': '=', 'tag_name': 'equals'}}], 'textViews': [{{'text': '', 'tag_name': 'No formula'}}, {{'text': '', 'tag_name': 'No result'}}]}}'''

REQUIREMENTS = '''Software Requirements Specification
Calculator

Introduction
Purpose

The purpose of this document is to present a detailed description about how the software of a calculator for phones should work. It describes which functionalities it should have. The document serves as a guide for the stakeholders and software developers alike.

General Description

The Calculator prevê apenas um tipo de usuário, que seria alguém com a necessidade de obter o resultado de uma expressão algébrica qualquer, de forma prática e rápida. Para isso, o software deve ser capaz de ler e avaliar uma expressão algébrica, levando em consideração a ordem de precedência dos operadores e dar suporte não apenas para as operações mais comuns realizadas no dia a dia, mas também operações comuns ao se resolver problemas da matemática ou das ciências naturais. Assim, é contemplada a necessidade não apenas de operações como soma e multiplicação, mas também atalhos para realizar o inverso multiplicativo, elevar um número x por outro y, ou até mesmo elevar x ao quadrado, visto que é a potência mais usual.

Functional Requirements Description

Use cases

- The User types a valid expression and can see a preview of the result

Each valid expression written by the user (it can be interpreted and evaluated) must show a preview of it 's result below the main text box. It 's possible to press the = button and the preview text replaces the expression text and the preview is erased. Valid expressions are made by the correct amount of operators, operands and parenthesis and also their correct order. The amount of operands needed depends on the operators used and their order are defined by the order of precedence used in math. This way, binary operations, such as sum or subtractions, require two operands. Unary operations, such as percentage, only require one.

- The User needs to calculate a sum

The User opens the app and types the operation following the natural order of writing. There is a sequence of digits representing the first operand of the sum, followed by the + symbol and finally another sequence of digits representing the last operand.

- The User needs to calculate a subtraction

The User opens the app and types the operation following the natural order of writing. There is a sequence of digits representing the first operand of the subtraction, followed by the - symbol and finally another sequence of digits representing the last operand.

- The User needs to calculate a multiplication

The User opens the app and types the operation following the natural order of writing. There is a sequence of digits representing the first operand of the multiplication, followed by the x symbol and finally another sequence of digits representing the last operand.

- The user needs to calculate a division

The User opens the app and types the operation following the natural order of writing. There is a sequence of digits representing the first operand of the division, followed by the ÷ symbol and finally another sequence of digits representing the last operand.

- The User needs to calculate percentage

The User opens the app and types the operand. Since this is a  unary operation representing a division by 100, then the User has to press the % symbol. If any other  operand is written, the sign of multiplication should be added before, chaining a multiplication in sequence.

- The User needs to calculate an exponentiation

The User opens the app and types the operation following the natural order of writing. There is a sequence of digits representing the first operand of the exponentiation, followed by the ^ symbol and finally another sequence of digits representing the last operand.

- The User needs to calculate a rooting operation

The User opens the app and types the operation following the natural order of writing. For this operation, the √ symbol has to be pressed first, then write the single operand. The operation refers to the square root.

-The User needs to calculate logarithm

The User opens the app and types the operation following the natural order of writing. For this operation, the log button should be pressed first, then the argument must be written. This operation refers to the logarithm base 10 and the log button open parenthesis automatically. There is also the button ln for the logarithm base e.

- The User needs to calculate a sine

The User opens the app and types the operation following the natural order of writing. For this operation, the sen button should be pressed first, then the argument must be written. The button automatically opens parenthesis.

- The User needs to calculate a cosine

The User opens the app and types the operation following the natural order of writing. For this operation, the cos button should be pressed first, then the argument must be written. The button automatically opens parenthesis.

- The User needs to calculate a tangent

The User opens the app and types the operation following the natural order of writing. For this operation, the tan button should be pressed first, then the argument must be written. The button automatically opens parenthesis.

- The User needs to calculate a factorial

The User opens the app and types the operation following the natural order of writing. For this operation, the operand should be written first, then the button ! should be pressed. If another operand is typed, a multiplication is automatically chained

- The User needs the values of the π or e constants

The User can press the buttons π or e, the two most common irrational constants, and their values are automatically evaluated in the expression. If there are operants before of after the constants, the operations is treated as a multiplication

- The User needs to chain many operations in sequence and they must be solved respecting their order of precedence

The order of precedence, from the heist priority to the lowest, is the following: operations in parentheses, functions that opens parentheses (sine, cosine, logarithm), unary functions (factorial, power of two) and constants, sign inversion, multiplication and division, sum and subtraction.

- The User forgets the result of a recent operation and needs it's result again

Each time the = button is pressed, the current typed expression is saved in the calculator history, as well as its result. To access the calculator history, the User must swipe down the upper area of the screen where the expression text boxes are.
'''

FINAL_QUESTION = 'Your Python function should correctly test the selected feature, making sure it works as expected. The code should use Appium and the python library unittest. Infer what assertions the respective tests need based on the provided information. Every test needs at least one assertion. Whenever the expected result would be a decimal number, use assertAlmostEqual for the assertion with a delta = 0.0001. There should also be a list before the code, containing the previous tested features, plus the selected one.'
