from tkinter import *
import chemistry as chem

#Author Austin Campbell
#Created to fulfill stretch challenge, plus I've been trying to get more comfortable with Tkinter.

#Constants for window colors
BACKGROUND = "#454545"
ENTRY_CLR = "#70706F"
WHITE = "#FFFFFF"
GREEN = "#40FF00"

#Main program
def main_program():

    def clear():
        """Deletes entry boxes ONLY."""
        chemical_entry.delete(0, END)
        num_moles_entry.delete(0, END)
        molar_mass_entry.delete(0, END)
        sample_mass_entry.delete(0, END)


    def get_inputs():
        """Get's user inputs, sends to chemical.py, does primary calculations in there, and sends them back, which
        is then actually sent to the result function"""
        #Get chemical formula, convert to all uppercase
        chemical = chemical_entry.get().upper()
        #Get sample mass and convert it to float.
        sample = float(sample_mass_entry.get())
        chem.main(chemical, sample) #This is just here to still print answers to terminal also
        #Moved from the main() in the chemistry.py
        table = chem.make_periodic_table()
        parsed_formula = chem.parse_formula(chemical, table)
        molar_mass = chem.compute_molar_mass(parsed_formula, table)
        number_of_moles = sample / molar_mass
        #Insert answers into entry boxes
        molar_mass_entry.insert(END, string=molar_mass)
        num_moles_entry.insert(END, string=number_of_moles)

    #Root window.
    calculator = Tk()
    calculator.title("Chemistry Calculator")
    calculator.minsize(width=350, height=250)
    calculator.config(bg=BACKGROUND)

    #Item frame
    item_frame = Frame(calculator, width=300, height=200)
    item_frame.config(bg=BACKGROUND)
    item_frame.grid(column=1, row=3, columnspan=3, rowspan=11)

    #Main labels up top
    main_label = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Chemical Calculator by Austin C.")
    main_label_2 = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Credit to BYUI as it's a school project!")
    sep = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="----------------------------------------")
    sep.grid(column=1, row=2)
    main_label.grid(column=1, row=0)
    main_label_2.grid(column=1, row=1)

    chemical_label = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Chemical Formula for Molecule: ")
    chemical_label.grid(column=1, row=3)
    chemical_entry = Entry(item_frame, fg=WHITE, bg=ENTRY_CLR, width=12)
    chemical_entry.grid(column=2, row=3)

    sample_mass_label = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Sample Mass(g): ")
    sample_mass_label.grid(column=1, row=4)
    sample_mass_entry = Entry(item_frame, fg=WHITE, bg=ENTRY_CLR, width=12)
    sample_mass_entry.grid(column=2, row=4)


    #calculate button
    white_space = Label(item_frame, bg=BACKGROUND, text="     ")
    white_space.grid(column=1, row=5)
    calculate = Button(item_frame, fg=WHITE, bg=BACKGROUND, text="Calculate", command=get_inputs)
    calculate.grid(column=2, row=5)


    #clear button
    clear_button = Button(item_frame, fg=WHITE, bg=BACKGROUND, text="Clear", command=clear)
    clear_button.grid(column=1, row=5)


    #Separator2
    sep2 = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="----------------------------------------")
    sep2.grid(column=1, row=8)


    #Result stuff
    result_1 = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Molar Mass (grams/mole): ")
    result_2 = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Moles: ")
    molar_mass_entry = Entry(item_frame, fg=GREEN, bg=ENTRY_CLR, width=20) #Might not use this
    molar_mass_entry.grid(column=2, row=9)
    num_moles_entry = Entry(item_frame, fg=GREEN, bg=ENTRY_CLR, width=20)
    num_moles_entry.grid(column=2, row=10)
    result_1.grid(column=1, row=9)
    result_2.grid(column=1, row=10)


    calculator.mainloop()


if __name__ == "__main__":
    main_program()