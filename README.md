For PCSX2 use `SLUS_20312_0.ps2`:
-   place it in the `memcards` folder
-   go into Settings > Memory Cards
-   click on the eject button on one of the Memory Cards
-   right click on `SLUS_20312_0.ps2` (if it doesn't appear in the list click the Refresh button)
-   Use for Port 1/2

For OPL use `SLUS_203.12_0.bin`:
-   while hovering ffx in OPL, press Triangle for Options
-   Configure VMC, create a new Virtual Memory Card by selecting `<not set>` and pressing X
-   press Create, press OK once it finishes
-   exit OPL or turn off the PS2
-   navigate to your OPL folder, open the VMC folder
-   replace the Memory Card you just created with `SLUS_203.12_0.bin`, rename it if the memory card you created had a different name

The `saves` folder contains the individual saves as .psu files.

The python script `ffx_ps2_save_names_editor.py` was used to overwrite the names in the savefiles, it tries to change the internal name of the files in the `saves` folder one by one using the names provided in the `saves_names.txt` file (one line for each save).

Tool used to import/export saves from memory cards https://github.com/ps2dev/mymc
