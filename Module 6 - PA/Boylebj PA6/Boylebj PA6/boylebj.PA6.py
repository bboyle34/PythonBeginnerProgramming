#CIS 221 Programming Assignment 12/3/17
#Brendan Boyle
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

from tkinter import * # Import tkinter


class LoanCalculator:
    def __init__(self):
        global frame1
        global window
        global text1
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title

        Label(window, text = "Annual Interest Rate").grid(row = 1, 
            column = 1, sticky = E)
        Label(window, text = "Number of Years").grid(row = 2, 
            column = 1, sticky = E)
        Label(window, text = "Loan Amount").grid(row = 3, 
            column = 1, sticky = E)
        Label(window, text = "Monthly Payment").grid(row = 4, 
            column = 1, sticky = E)
        Label(window, text = "Total Payment").grid(row = 5, 
            column = 1, sticky = E)

        #Annual Interest Rate
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2, sticky = W)        
        #Number of Years
        self.numberOfYearsVar = StringVar()                 
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2, sticky = W)        
        #Loan Amount
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2, sticky = W)        
        #Monthly Payment
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, padx = 40,  
            sticky = W)        
        #Total Payment    
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable =
            self.totalPaymentVar).grid(row = 5, 
            column = 2, padx = 40, sticky = W)
        #Compute Payment Button
        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 6, column = 1, sticky = E)
        #Save Loan Button
        btSaveLoan = Button(window, text = "Save Loan to File",
            command = self.saveLoan).grid(
                row = 6, column = 2, stick = W, padx = 24.5)
        
        Label(window, text = "$").grid(row = 4, column = 2,
                                       sticky = W, padx = 30)
        Label(window, text = "$").grid(row = 5, column = 2,
                                       sticky = W, padx = 30)
        #create the frame inside the window
        frame1 = Frame(window)
        frame1.grid(row = 7, column = 0, rowspan = 5, columnspan = 4)
        scrollbar = Scrollbar(frame1)
        scrollbar.grid(row = 7, column = 4, rowspan = 5, sticky = N+S+E)
        text1 = Text(frame1, width = 85, height = 20, wrap = WORD,
                     yscrollcommand = scrollbar.set)
        text1.grid(row = 7, column = 0, rowspan = 5, columnspan = 4)
        scrollbar.config(command = text1.yview)
        text1.insert(END,
            "Amortization Schedule \npmt #")
        text1.insert(END,
            "\t\t\tinterest")
        text1.insert(END,
            "\t\tprin pmt")
        text1.insert(END,
            "\t\tremaining prin\n") 
        
        window.mainloop() # Create an event loop
        

    #function for compute payment button
    def computePayment(self):
        try:
            monthlyPayment = self.getMonthlyPayment(
                float(self.loanAmountVar.get()), 
                float(self.annualInterestRateVar.get()) / 1200, 
                int(self.numberOfYearsVar.get()))
            self.monthlyPaymentVar.set(format(monthlyPayment, ',.2f'))
            totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                * int(self.numberOfYearsVar.get())
            self.totalPaymentVar.set(format(totalPayment, ',.2f'))
            
            #set scrollbar and frame
            frame1 = Frame(window)
            frame1.grid(row = 7, column = 0, rowspan = 5, columnspan = 4)
            scrollbar = Scrollbar(frame1)
            scrollbar.grid(row = 7, column = 4, rowspan = 5, sticky = N+S+E)
            text1 = Text(frame1, width = 85, height = 20, wrap = WORD,
                         yscrollcommand = scrollbar.set)
            text1.grid(row = 7, column = 0, rowspan = 5, columnspan = 4)
            scrollbar.config(command = text1.yview)
            text1.insert(END,
                "Amortization Schedule \npmt #")
            text1.insert(END,
                "\t\t\tinterest")
            text1.insert(END,
                "\t\tprin pmt")
            text1.insert(END,
                "\t\tremaining prin\n")

            balance = float(self.loanAmountVar.get())
            monthlyInterestRate = float(self.annualInterestRateVar.get()) / 1200
            monthlyPayment = float(self.loanAmountVar.get()) * monthlyInterestRate / \
                (1 - (pow(1 / (1 + monthlyInterestRate), float(self.numberOfYearsVar.get()) * 12)))
        
            #loop for amortizaiton schedule
            for i in range(1, int(self.numberOfYearsVar.get()) * 12 + 1):
                interest = ((monthlyInterestRate * balance) * 100) / 100.0
                principal = ((monthlyPayment - interest) * 100) / 100.0
                balance = ((balance - principal) * 100) / 100.0
                interest1 = format(interest, ',.2f')
                principal1 = format(principal, ',.2f')
                balance1 = format(balance, ',.2f')
                schedule = (str(i) + "\t\t\t" + '{:>7}'.format("$" + interest1) + "\t\t" + '{:>7}'.format("$" + principal1) + "\t\t" + '{:>12}'.format("$" + balance1) + "\n")
                text1.insert(END,
                             schedule)
        except(ValueError):
            command = self.wrongEntry()
            

    #function for monhtly payment         
    def getMonthlyPayment(self,
            loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
           - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;


    #function for save loan button
    def saveLoan(self):
        import tkinter.simpledialog
        name = tkinter.simpledialog.askstring(
            "Loan Recipient", "Enter the name of the loan recipient")
        if not name == None:
            
            loanAmount1 = (float(self.loanAmountVar.get()))
            loanAmount2 = format(loanAmount1, ',.2f')
            annualInterestRate1 = (float(self.annualInterestRateVar.get()) / 100.0)
            annualInterestRate2 = format(annualInterestRate1, '.2%')
            monthlyPayment1 = (float(self.monthlyPaymentVar.get()))
            monthlyPayment2 = format(monthlyPayment1, ',.2f')
            
            #create a file and design the amortization schedule in it
            outfile = open(name + " loan document.txt", "w")
            outfile.write("\t\tLoan Document for ")
            outfile.write(name)
            outfile.write("\n\t\t---------------------------------------\n\n")
            outfile.write("Loan Amount: $")
            outfile.write(loanAmount2)
            outfile.write("\t\tInterest Rate: ")
            outfile.write(annualInterestRate2)
            outfile.write("\tNbr Years: ")
            outfile.write(self.numberOfYearsVar.get())
            outfile.write("\nMonthly Payment: $")
            outfile.write(monthlyPayment2)
            outfile.write("\t\tTotal Payment: $")
            outfile.write(self.totalPaymentVar.get())
            outfile.write("\n\nAmortization Schedule \npmt #")
            outfile.write("\t\t\tinterest \tprin pmt \tremaining prin\n")

            balance = float(self.loanAmountVar.get())
            monthlyInterestRate = float(self.annualInterestRateVar.get()) / 1200
            monthlyPayment = float(self.loanAmountVar.get()) * monthlyInterestRate / \
                (1 - (pow(1 / (1 + monthlyInterestRate), float(self.numberOfYearsVar.get()) * 12)))
        
            for i in range(1, int(self.numberOfYearsVar.get()) * 12 + 1):
                interest = ((monthlyInterestRate * balance) * 100) / 100.0
                principal = ((monthlyPayment - interest) * 100) / 100.0
                balance = ((balance - principal) * 100) / 100.0
                interest1 = format(interest, ',.2f')
                principal1 = format(principal, ',.2f')
                balance1 = format(balance, ',.2f')
                schedule = (str(i) + "\t\t\t" + '{:>7}'.format("$" + interest1) + "\t\t" + '{:>7}'.format("$" + principal1) + "\t\t" + '{:>12}'.format("$" + balance1) + "\n")
                outfile.write(schedule)
            outfile.close()
            print("File has been saved")
        
        
    #function for wrong entries
    def wrongEntry(self):
        import tkinter.messagebox
        tkinter.messagebox.showerror("Calculation Error",
        "Please make sure to enter numeric values for interest rate, years, and loan amount")
            
        

LoanCalculator()  # Create GUI 
