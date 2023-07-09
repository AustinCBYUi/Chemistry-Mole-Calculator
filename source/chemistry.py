from formula import parse_formula
from tkinter import *

#Author - BYUi / Austin Campbell?!
#Moved application into this file to help instructor in grading.
#Tests work, program runs, and only need this one file instead of both how I had it!
#Thank you!


MOLE = 6.02214076 * 10 ** 23

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:

    #Always forget to put the zeroed variable outside the loop..
    #Spent too much time trying to find the bug here, this was it being inside the loop.
    total_molar_mass = 0

    for item in symbol_quantity_list:
        each_element = item

        # Separate the inner list into symbol and quantity.
        symbol = each_element[SYMBOL_INDEX] #0 in the list,
        quantity = each_element[QUANTITY_INDEX] #1 in the list

        #If the symbol is in the periodic table dictionary, the new variable is dictionary_symbol
        if symbol in periodic_table_dict:
            #In which it checks the actual periodic table dictionary with the [symbol] as each
            #symbol from the symbol_quantity_list.
            dictionary_symbol = periodic_table_dict[symbol]
        #If it's not, you'll get this print.
        else:
            print("Symbol doesn't exist?")

        # Get the atomic mass for the symbol from the dictionary.
        atomic_mass = dictionary_symbol[ATOMIC_MASS_INDEX]

        # Multiply the atomic mass by the quantity.
        do_math = atomic_mass * quantity

        # Add the product into the total molar mass.
        total_molar_mass += do_math #?

    # Return the total molar mass.
    return total_molar_mass


#Just makes the periodic table of elements in the form of a dictionary.
def make_periodic_table():
    periodic_table_dict = {
            # symbol: [name, atomic_mass]
            "Ac":  ["Actinium", 227],
            "Ag":  ["Silver", 107.8682],
            "Al":  ["Aluminum", 26.9815386],
            "Ar":  ["Argon",	39.948],
            "As":  ["Arsenic",	74.9216],
            "At":  ["Astatine",	210],
            "Au":  ["Gold",	196.966569],
            "B":   ["Boron",	10.811],
            "Ba":  ["Barium",	137.327],
            "Be":  ["Beryllium",	9.012182],
            "Bi":  ["Bismuth",	208.9804],
            "Br":  ["Bromine",	79.904],
            "C":   ["Carbon",	12.0107],
            "Ca":  ["Calcium",	40.078],
            "Cd":  ["Cadmium",	112.411],
            "Ce":  ["Cerium",	140.116],
            "Cl":  ["Chlorine",	35.453],
            "Co":  ["Cobalt",	58.933195],
            "Cr":  ["Chromium",	51.9961],
            "Cs":  ["Cesium",	132.9054519],
            "Cu":  ["Copper",	63.546],
            "Dy":  ["Dysprosium",	162.5],
            "Er":  ["Erbium",	167.259],
            "Eu":  ["Europium",	151.964],
            "F":   ["Fluorine",	18.9984032],
            "Fe":  ["Iron",	55.845],
            "Fr":  ["Francium",	223],
            "Ga":  ["Gallium",	69.723],
            "Gd":  ["Gadolinium",	157.25],
            "Ge":  ["Germanium",	72.64],
            "H":   ["Hydrogen",	1.00794],
            "He":  ["Helium",	4.002602],
            "Hf":  ["Hafnium",	178.49],
            "Hg":  ["Mercury",	200.59],
            "Ho":  ["Holmium",	164.93032],
            "I":   ["Iodine",	126.90447],
            "In":  ["Indium",	114.818],
            "Ir":  ["Iridium",	192.217],
            "K":   ["Potassium",	39.0983],
            "Kr":  ["Krypton",	83.798],
            "La":  ["Lanthanum",	138.90547],
            "Li":  ["Lithium",	6.941],
            "Lu":  ["Lutetium",	174.9668],
            "Mg":  ["Magnesium",	24.305],
            "Mn":  ["Manganese",	54.938045],
            "Mo":  ["Molybdenum",	95.96],
            "N":   ["Nitrogen",	14.0067],
            "Na":  ["Sodium",	22.98976928],
            "Nb":  ["Niobium",	92.90638],
            "Nd":  ["Neodymium",	144.242],
            "Ne":  ["Neon",	20.1797],
            "Ni":  ["Nickel",	58.6934],
            "Np":  ["Neptunium",	237],
            "O":   ["Oxygen",	15.9994],
            "Os":  ["Osmium",	190.23],
            "P":   ["Phosphorus",	30.973762],
            "Pa":  ["Protactinium",	231.03588],
            "Pb":  ["Lead",	207.2],
            "Pd":  ["Palladium",	106.42],
            "Pm":  ["Promethium",	145],
            "Po":  ["Polonium",	209],
            "Pr":  ["Praseodymium",	140.90765],
            "Pt":  ["Platinum",	195.084],
            "Pu":  ["Plutonium",	244],
            "Ra":  ["Radium",	226],
            "Rb":  ["Rubidium",	85.4678],
            "Re":  ["Rhenium",	186.207],
            "Rh":  ["Rhodium",	102.9055],
            "Rn":  ["Radon",	222],
            "Ru":  ["Ruthenium",	101.07],
            "S":   ["Sulfur",	32.065],
            "Sb":  ["Antimony",	121.76],
            "Sc":  ["Scandium",	44.955912],
            "Se":  ["Selenium",	78.96],
            "Si":  ["Silicon",	28.0855],
            "Sm":  ["Samarium",	150.36],
            "Sn":  ["Tin",	118.71],
            "Sr":  ["Strontium",	87.62],
            "Ta":  ["Tantalum",	180.94788],
            "Tb":  ["Terbium",	158.92535],
            "Tc":  ["Technetium",	98],
            "Te":  ["Tellurium",	127.6],
            "Th":  ["Thorium",	232.03806],
            "Ti":  ["Titanium",	47.867],
            "Tl":  ["Thallium",	204.3833],
            "Tm":  ["Thulium",	168.93421],
            "U":   ["Uranium",	238.02891],
            "V":   ["Vanadium",	50.9415],
            "W":   ["Tungsten",	183.84],
            "Xe":  ["Xenon",	131.293],
            "Y":   ["Yttrium",	88.90585],
            "Yb":  ["Ytterbium",	173.054],
            "Zn":  ["Zinc",	65.38],
            "Zr":  ["Zirconium",	91.224]
    }

    return periodic_table_dict


#For the stretch challenge I created a Tkinter GUI for the program, so I removed the main() function here as it now
#uses the mainapplication() function in the application.py file.
#It still performs the actions required.

#I am keeping this main() function in for the grading rubric.


#Now takes these inputs from application.py
def main(chemical_formula, sample_mass):
#     # Get a chemical formula for a molecule from the user.
#     # chemical_formula = input("Formula for molecule: ")

#     # Get the mass of a chemical sample in grams from the user.
#     # sample_mass = float(input("Mass of Sample in grams: "))

#     # Call the make_periodic_table function and
#     # store the periodic table in a variable.
    table = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    parsed_formula = parse_formula(chemical_formula, table)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(parsed_formula, table)

    # Compute the number of moles in the sample.
    number_of_moles = sample_mass / molar_mass

    # Print the molar mass.
    print(f"{molar_mass} grams/mole")

    # Print the number of moles.
    print(f"{number_of_moles} moles")

#GUI Stuff

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
        main(chemical, sample) #This is just here to still print answers to terminal also
        #Moved from the main() in the chemistry.py
        table = make_periodic_table()
        parsed_formula = parse_formula(chemical, table)
        molar_mass = compute_molar_mass(parsed_formula, table)
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

    sample_mass_label = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Sample Mass: ")
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
    result_1 = Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Molar Mass: ")
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