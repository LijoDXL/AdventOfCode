import numpy as np
import pandas as pd
from math import ceil,floor


def parse_eq(file,n_fuel=1):
    """Parse the reaction file and returns lists needed to work with
    Parameters:
    ============
        file  :  string
                 path to reaction file
        n_fuel:  int
                 units of FUEL required
    Returns:
    =========
        list
        elements,elements_units,ore_units,eq,units,fuel_eq
    """
    with open(file) as f:
        lines = f.readlines()
    lines = [l.strip()  for l in lines]
    
    # elements are directly derived from ORE
    elements = [l.split(' => ')[1].split()[1] for l in lines if 'ORE' in l ]
    
    # units in which elements can be produced
    elements_units = {l.split(' => ')[1].split()[1]:int(l.split(' => ')[1].split()[0]) for l in lines if 'ORE' in l }
    
    # ORE required for each element
    ore_units = {l.split(' => ')[1].split()[1]:int(l.split(' => ')[0].split()[0]) for l in lines if 'ORE' in l }
    
    # reactions other than for FUEL and ORE
    lines_rest = [l for l in lines if 'ORE' not in l and 'FUEL' not in l]
    
    # FUEL reaction
    fuel_eq_ = [l.split(' => ')[0].split(', ') for l in lines if 'FUEL' in l][0]
    
    # if more than 1 fuel needed (part-2)
    fuel_eq = []
    for chem in fuel_eq_:
        n,c = chem.split()
        n_x = int(n)*n_fuel
        fuel_eq.append(str(n_x)+' '+c)
    
    # reaction equation for each chemical and their units
    eq = {}
    units = {}
    for l in lines_rest:
        formula = l.split(' => ')[0].split(', ')
        n,chem = l.split(' => ')[1].split()
        eq[chem] = formula
        units[chem] = int(n)
    return elements,elements_units,ore_units,eq,units,fuel_eq


def expand(eq_list,eq,units,elements,extra={}):
    """Function to expand reaction to it's first order previous component
    Parameters:
    ============
        eq_list : list
                  reaction to expand
        eq      : dict
                  equation of each chem
        units   : dict
                  unit for each chem
        extra   : dict
                  leftover after reaction
        elements: list
                  element list
    Returns:
    =========
        items: list 
               expanded reaction in the form of a list
        extra: dict
               leftover to carry forward
    """
    items = []
    for c in eq_list:
        n,chem = c.split()
        n = int(n)
        if chem in elements:
            items.append(str(n)+' '+chem) # no expansion needed
        else:
            chem_eq = eq[chem]
            chem_unit = units[chem]
            if chem in extra:
                while extra[chem]>0 and n>0:
                    n = n - 1
                    extra[chem]-=1
                factor = ceil(n/chem_unit)
                extra[chem]+= (factor*chem_unit - n)
            else:
                factor = ceil(n/chem_unit)
                extra[chem] = (factor*chem_unit - n)
            
            chem_exp = []
            for x in chem_eq:
                x_n,x_chem = x.split()
                x_n = int(x_n)
                x_n_multiple = x_n*factor
                chem_exp.append(str(x_n_multiple)+' '+x_chem)
        
            items.extend(chem_exp)
    return items,extra


def expand_full(to_expand,eq,units,elements,extras={}):
    s_list = to_expand
    r_list,extra_chem = expand(s_list,eq,units,elements,extra=extras)
    # repeat till reactions expands to only elements
    while r_list != s_list:
        s_list = r_list
        r_list,extra_chem = expand(s_list,eq,units,elements,extra=extra_chem)
    return r_list,extra_chem


def ore(full_exp_eq,elements,elements_units,ore_units):
    # total elements required
    need = {i:np.sum([float(k.split()[0]) for k in full_exp_eq if k.split()[1]==i]) for i in elements}

    # total ORE required
    tot_ore = np.sum([ceil(need[i]/elements_units[i])*ore_units[i] for i in elements])
    return tot_ore


file_name = 'Day14-input.txt'
elmnts,elmnts_units,oreUnits,equation,chem_units,fuel_eqn = parse_eq(file_name,n_fuel=1)
full_exp_eqn,extras = expand_full(fuel_eqn,equation,chem_units,elmnts,extras={})
tot_ore = ore(full_exp_eqn,elmnts,elmnts_units,oreUnits)

print("Total ORE required is: ",tot_ore)

# ### PART-2
lo = 0
hi = 1e12
while lo < hi: # binary search
    mid = ceil((lo+hi)/2)
    elmnts,elmnts_units,oreUnits,equation,chem_units,fuel_eqn = parse_eq(file_name,n_fuel=mid)
    full_exp_eqn,extras = expand_full(fuel_eqn,equation,chem_units,elmnts,extras={})
    tot_ore = ore(full_exp_eqn,elmnts,elmnts_units,oreUnits)
    if tot_ore <= 1e12:
        lo = mid
    else:
        hi = mid-1
    print(f"range is:({lo},{hi})")
