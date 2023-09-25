#! /usr/bin/env python
"""
Script to generate a simulated star catalogue
"""
import math as mh
import random as rd

def generate_positions(NSRC):
    """Function generating star catalogue."""
    # Determine Andromeda location in ra/dec degrees

    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    D, M, S = DEC.split(':')
    DEC = int(D)+int(M)/60+float(S)/3600

    H, M, S = RA.split(':')
    RA = 15*(int(H)+int(M)/60+float(S)/3600)
    RA = RA/mh.cos(DEC*mh.pi/180)

    # make 1000 stars within 1 degree of Andromeda
    RAS = []
    DECS = []
    for i in range(NSRC):
        RAS.append(RA + rd.uniform(-1, 1))
        DECS.append(DEC + rd.uniform(-1, 1))
    return RAS, DECS

def save_positions_to_file(RAS, DECS, NSRC):
    """Function saving positions in a csv file."""
    # now write these to a csv file for use by my other program
    PATHDIR = '/home/venturae/Desktop/PhD/ADACS_workshop/Monday/mymodule/data/output'
    with open(PATHDIR + '/catalog.csv', 'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print("{0:07d}, {1:12f}, {2:12f}".format(i, RAS[i], DECS[i]), file=f)

def main():
    """Main function"""
    NSRC = 1_000
    RAS, DECS = generate_positions(NSRC)
    save_positions_to_file(RAS, DECS, NSRC)

#if this is invoked as a script
if __name__ == "__main__": 
    main()
    