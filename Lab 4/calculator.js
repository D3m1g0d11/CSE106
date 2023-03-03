class Calculator{
    constructor(previousOperandTextElement, currentOperandTextElement) {
        this.firstNumText = previousOperandTextElement
        this.secondNumText = currentOperandTextElement
        this.clear()
    }

    clear(){
        this.firstNum = ''
        this.secondNum = ''
        this.operation = undefined
    }

    delete(){
        this.secondNum = this.secondNum.toString().slice(0, -1)
    }
    appendNumber(number){
        if(number === '.' && this.secondNum.includes('.')) {
            return
        }
        this.secondNum = this.secondNum.toString() + number.toString()
    }
    calculate(){
        let computation
        const prev  = parseFloat(this.firstNum)
        const curr = parseFloat(this.secondNum)

        if(isNaN(prev) || isNaN(curent)) return
            if(this.operation == '+'){
                computation = prev + curr
            }
            else if(this.operation == '-'){
                computation = prev - curr
            }
            else if(this.operation == 'x'){
                computation = prev * curr
            }
            else if(this.operation == '/'){
                computation = prev / curr
            }

        return computation
    }
    chooseOperation(operation){
        this.operation = operation
        this.firstNum = this.secondNum
        this.secondNum = ''

    }
    updateDisplay(){
        this.secondNumText.innerText = this.secondNum
        this.firstNumText.innerText = this.firstNum
    }
}


const numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operation]')
const equalsButtons = document.querySelector('[data-equals]')
const deleteButton = document.querySelector('[data-delete]')
const allClearButton = document.querySelector('[data-all-clear]')
const previousOperandTextElement = document.querySelector('[data-prev-oper]')
const currentOperandTextElement = document.querySelector('[data-curr-oper]')

const calculator = new Calculator(previousOperandTextElement, currentOperandTextElement)

numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.appendNumber(button.innerText)
        calculator.updateDisplay()
    })
})

operationButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.chooseOperation(button.innerText)
        calculator.updateDisplay()
    })
})

equalsButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.calculate()
        calculator.updateDisplay()
    })
})

allClearButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.clear()
        calculator.updateDisplay()
    })
})


deleteButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.delete()
        calculator.updateDisplay()
    })
})