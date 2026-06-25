# BB0789 / 7ZBH Residue Panel

Source structure: PDB 7ZBH, ATP-dependent zinc metalloprotease FtsH (BB0789) from *Borrelia burgdorferi*. The local scripts use the RCSB biological assembly CIF and author residue numbering.

## Residue Groups

| Functional feature | Residues / region | Script color | Notes |
| --- | --- | --- | --- |
| Walker A / P-loop / ADP site | 211-220; especially Gly215, Thr216, Lys218, Thr219, Leu220 | gold | The exact P-loop motif in 7ZBH is `GSPGTGKT` at 212-219. |
| Additional ADP contact | Ala379 | gold | Included with ADP-site geometry. |
| Walker B | Asp271, surrounding 269-274 | gold | The local Walker B sequence is `FIDELD` at 269-274. |
| Pore / threading working target | 329-332 | gold | This maps to `RPDV`; verify visually before using as a strict docking constraint. |
| FVG motif / pore-aromatic feature | 245-247 | gold | Exact `FVG` occurrence in the 7ZBH sequence. |
| Zn catalytic site | His434, His438, Asp510 | red | Direct Zn coordination in the deposited model. |
| HEXXH motif region | His434, Glu435, His438 | red | Local sequence is `HEAGH` at 434-438. |
| Protease-domain hexamer interface | Tyr490, Tyr493, Gln508, Asp561, Lys568 | green | Intersubunit assembly / allosteric target zone. |
| Missing / weak loops | 277-287, 306-310, 396-404, 414-423, 461-475, 538-553 | purple | Some residues are absent from the coordinates; scripts color modeled fragments and flanking anchors. |

## Running

From the `bb0789-ftsh/` directory in ChimeraX:

```text
open chimerax/01_open_clean_label_7zbh.cxc
open chimerax/02_residue_panel.cxc
open chimerax/03_export_standard_views.cxc
```

Optional distance helper:

```text
open chimerax/04_measure_sites.py
```

