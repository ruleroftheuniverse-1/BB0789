"""ChimeraX helper for BB0789 / 7ZBH residue-panel measurements.

Run inside ChimeraX after opening the model:
    open C:/BB0789/bb0789-ftsh/chimerax/04_measure_sites.py

The script adds distance monitors for representative chain A ADP contacts and
Zn coordination. It intentionally keeps to the fixed panel residues used in the
.cxc scripts.
"""

from chimerax.core.commands import run


ADP_DISTANCES = [
    ("/A:215@CA", "/A:701@PB"),
    ("/A:216@OG1", "/A:701@PB"),
    ("/A:218@NZ", "/A:701@PB"),
    ("/A:219@OG1", "/A:701@PA"),
    ("/A:220@CA", "/A:701@PA"),
    ("/A:271@OD1", "/A:701@PB"),
    ("/A:329@CA", "/A:701@C4"),
    ("/A:332@CA", "/A:701@C4"),
    ("/A:379@CB", "/A:701@N6"),
]

ZN_DISTANCES = [
    ("/A:434@NE2", "/A:702@ZN"),
    ("/A:438@NE2", "/A:702@ZN"),
    ("/A:510@OD1", "/A:702@ZN"),
    ("/A:510@OD2", "/A:702@ZN"),
]


def run_measurements(session):
    run(session, "distance delete")
    run(session, "2dlabels delete")

    for residue_atom, ligand_atom in ADP_DISTANCES:
        run(session, f"distance {residue_atom} {ligand_atom}")

    for residue_atom, zinc_atom in ZN_DISTANCES:
        run(session, f"distance {residue_atom} {zinc_atom}")

    run(session, "2dlabels create measure_note text \"Distance monitors: chain A ADP panel and Zn coordination\" xpos 0.03 ypos 0.95 size 20 color black")


run_measurements(session)
