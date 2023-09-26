#! /usr/bin/env python
"""
Script to generate a simulated star catalogue around Andromeda
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
    return RAS, DECS, RA, DEC

def save_positions_to_file(RAS, DECS, NSRC):
    """Function saving positions in a csv file."""
    # now write these to a csv file for use by my other program
    PATHDIR = '/home/venturae/Desktop/PhD/ADACS_workshop/Monday/mymodule/data/output'
    with open(PATHDIR + '/catalog.csv', 'w') as f:
        print("id,ra,dec", file=f)
        for i in range(len(RAS)):
            print("{0:07d}, {1:12f}, {2:12f}".format(i, RAS[i], DECS[i]), file=f)

def crop_to_circle(ras, decs, ref_ra, ref_dec, radius):
    """
    Crop an input list of positions so that they lie within radius of
    a reference position

    Parameters
    ----------
    ras,decs : list(float)
        The ra and dec in degrees of the data points
    ref_ra, ref_dec: float
        The reference location
    radius: float
        The radius in degrees
    Returns
    -------
    ras, decs : list
        A list of ra and dec coordinates that pass our filter.
    """
    
    ra_out = []
    dec_out = []
    for i in range(len(ras)):
        if (ras[i]-ref_ra)**2 + (decs[i]-ref_dec)**2 < radius**2:
            ra_out.append(ras[i])
            dec_out.append(decs[i])
    return ra_out, dec_out

def main():
    """Main function"""
    NSRC = 1_000
    radius = 1.0
    RAS, DECS, RA, DEC = generate_positions(NSRC)
    RAS_OUT, DECS_OUT = crop_to_circle(RAS, DECS, RA, DEC, radius)
    save_positions_to_file(RAS_OUT, DECS_OUT, NSRC)

#if this is invoked as a script
if __name__ == "__main__": 
    main()
    
