#q7_generate_payroll.py
       
#get input
name = input("Enter name:")
hours = input("Enter number of hours worked weekly:")
pay_rate = input("Enter hourly pay rate:")
cpf = input("Enter CPF contribution rate(%):")

def process_input():
    global hours, pay_rate, cpf
    try:
        hours = float(hours)
        pay_rate = float(pay_rate)
        cpf = float(cpf)
        return True
    except ValueError:
        return False
if process_input():
    
    #formula
    gross_pay = hours * pay_rate
    cpf_contribution = (cpf/100) *gross_pay
    net_pay = gross_pay - cpf_contribution

#output
    print("\nPayroll statement for {0}\nNumber of hours worked in week: {1:.2f}\nHourly pay rate: ${2:.2f}\nGross pay: ${3:.2f}\nCPF contribution at {4:.0f}%: ${5:.2f}\n\nNet pay: ${6:.2f}".format(name, hours, pay_rate, gross_pay, cpf, cpf_contribution, net_pay))
else:
    print("Invalid input")
