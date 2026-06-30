# Running ChimeraX Scripts

ChimeraX resolves relative paths from its current working directory, not from the location of the `.cxc` script being executed. That means commands like `open structures/7zbh_bioassembly.cif` or `save output.png` can break or write files somewhere unexpected if ChimeraX was launched from another directory.

These scripts avoid that problem by using absolute Windows-safe forward-slash paths rooted at:

```text
C:/BB0789/bb0789-ftsh
```

Run the workflow in ChimeraX with:

```text
open C:/BB0789/bb0789-ftsh/chimerax/01_open_clean_label_7zbh.cxc
open C:/BB0789/bb0789-ftsh/chimerax/02_residue_panel.cxc
open C:/BB0789/bb0789-ftsh/chimerax/03_export_standard_views.cxc
```

Optional measurement helper:

```text
open C:/BB0789/bb0789-ftsh/chimerax/04_measure_sites.py
```

Screenshots are exported to:

```text
C:/BB0789/bb0789-ftsh/outputs
```
